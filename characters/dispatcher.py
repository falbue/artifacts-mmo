from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable

import helpers

from .main import Character

log = helpers.setup_logger(
    "DISPATCHER", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL
)


@dataclass
class Task:
    title: str
    run: Callable[[], None]


@dataclass
class MaterialRequest:
    requester: str
    code: str
    quantity: int


class CharacterWorker:
    def __init__(self, name: str) -> None:
        self.character = Character(name)
        self.name = name
        self._queue: deque[Task] = deque()

    def enqueue(self, task: Task) -> None:
        self._queue.append(task)

    def enqueue_priority(self, task: Task) -> None:
        self._queue.appendleft(task)

    def is_idle(self) -> bool:
        return len(self._queue) == 0

    def queue_size(self) -> int:
        return len(self._queue)

    def inventory_quantity(self, code: str) -> int:
        inventory = self.character.params.get("inventory", [])
        for item in inventory:
            if item.get("code") == code:
                return item.get("quantity", 0)
        return 0

    def task_move(self, map_id: int) -> Task:
        return Task(
            title=f"move:{map_id}",
            run=lambda: self.character.move(map_id),
        )

    def task_gathering(self) -> Task:
        return Task(
            title="gathering",
            run=self.character.gathering,
        )

    def task_bank(self, code: str, quantity: int, action: str = "deposit") -> Task:
        return Task(
            title=f"bank:{action}:{code}:{quantity}",
            run=lambda: self.character.bank(code, quantity, action),
        )

    def task_craft(self, code: str, quantity: int = 1) -> Task:
        return Task(
            title=f"craft:{code}:{quantity}",
            run=lambda: self.character.craft(code, quantity),
        )

    def enqueue_recipe(self, steps: list[dict], repeat: int = 1) -> None:
        if repeat <= 0:
            return

        for _ in range(repeat):
            for step in steps:
                action = step.get("action")

                if action == "move":
                    self.enqueue(self.task_move(step["map_id"]))
                elif action == "gather":
                    times = int(step.get("times", 1))
                    for _ in range(max(times, 0)):
                        self.enqueue(self.task_gathering())
                elif action == "bank":
                    self.enqueue(
                        self.task_bank(
                            step["code"],
                            int(step.get("quantity", 1)),
                            step.get("bank_action", "deposit"),
                        )
                    )
                elif action == "craft":
                    self.enqueue(
                        self.task_craft(
                            step["code"],
                            int(step.get("quantity", 1)),
                        )
                    )
                else:
                    raise ValueError(f"Неизвестный шаг рецепта: {action}")

    def run_next(self) -> bool:
        if not self._queue:
            return False

        task = self._queue.popleft()
        log.debug(f"{self.name} выполняет задачу {task.title}")
        task.run()
        return True


class TeamCoordinator:
    def __init__(
        self, bank_map_id: int, resource_nodes: dict[str, int] | None = None
    ) -> None:
        self.bank_map_id = bank_map_id
        self.resource_nodes = resource_nodes or {}
        self.workers: dict[str, CharacterWorker] = {}
        self.pending_requests: deque[MaterialRequest] = deque()

    def add_worker(self, name: str) -> CharacterWorker:
        worker = CharacterWorker(name)
        self.workers[name] = worker
        return worker

    def request_material(self, requester: str, code: str, quantity: int) -> None:
        if quantity <= 0:
            return

        request = MaterialRequest(requester=requester, code=code, quantity=quantity)
        self.pending_requests.append(request)
        self._try_assign_requests()

    def inject_bank_topup(
        self,
        worker_name: str,
        code: str,
        quantity: int,
        return_map_id: int | None = None,
    ) -> None:
        worker = self.workers[worker_name]

        if return_map_id is not None:
            worker.enqueue_priority(worker.task_move(return_map_id))
        worker.enqueue_priority(worker.task_bank(code, quantity, "deposit"))
        worker.enqueue_priority(worker.task_move(self.bank_map_id))

    def _try_assign_requests(self) -> None:
        if not self.pending_requests:
            return

        unresolved: deque[MaterialRequest] = deque()

        while self.pending_requests:
            request = self.pending_requests.popleft()
            if not self._assign_request(request):
                unresolved.append(request)

        self.pending_requests = unresolved

    def _assign_request(self, request: MaterialRequest) -> bool:
        donor = self._find_inventory_donor(
            code=request.code,
            quantity=request.quantity,
            exclude_name=request.requester,
        )
        if donor is not None:
            self.inject_bank_topup(donor.name, request.code, request.quantity)
            return True

        helper = self._find_idle_helper(exclude_name=request.requester)
        node_map_id = self.resource_nodes.get(request.code)
        if helper is None or node_map_id is None:
            return False

        helper.enqueue_priority(
            helper.task_bank(request.code, request.quantity, "deposit")
        )
        helper.enqueue_priority(helper.task_move(self.bank_map_id))
        for _ in range(request.quantity):
            helper.enqueue_priority(helper.task_gathering())
        helper.enqueue_priority(helper.task_move(node_map_id))
        return True

    def _find_inventory_donor(
        self,
        code: str,
        quantity: int,
        exclude_name: str,
    ) -> CharacterWorker | None:
        for name, worker in self.workers.items():
            if name == exclude_name:
                continue
            if worker.inventory_quantity(code) >= quantity:
                return worker
        return None

    def _find_idle_helper(self, exclude_name: str) -> CharacterWorker | None:
        for name, worker in self.workers.items():
            if name == exclude_name:
                continue
            if worker.is_idle():
                return worker
        return None

    def run_step(self) -> bool:
        self._try_assign_requests()

        has_work = False
        for worker in self.workers.values():
            if worker.run_next():
                has_work = True
        return has_work

    def run(self, max_steps: int = 1000) -> int:
        steps_done = 0
        while steps_done < max_steps and self.run_step():
            steps_done += 1
        return steps_done
