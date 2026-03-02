from __future__ import annotations

from collections import deque
from typing import Callable, Any

import helpers

from .main import Character
from .tasks import Task

log = helpers.setup_logger(
    "DISPATCHER", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL
)


class CharacterWorker:
    def __init__(self, name: str) -> None:
        """Создаёт воркера для конкретного персонажа по имени."""

        self.character = Character(name)
        self.name = name
        self._queue: deque[Task] = deque()

    def _enqueue_task(self, task: Task, priority: bool = False) -> None:
        """Внутренний метод постановки задачи в очередь."""

        if priority:
            self._queue.appendleft(task)
            return
        self._queue.append(task)

    def task(
        self,
        builder: Callable[..., Task],
        *args: Any,
        priority: bool = False,
        **kwargs: Any,
    ) -> Task:
        """Создаёт задачу через builder(...) и сразу ставит её в очередь."""

        new_task = builder(self.character, *args, **kwargs)
        self._enqueue_task(new_task, priority=priority)
        return new_task

    def top(self, builder: Callable[..., Task], *args: Any, **kwargs: Any) -> Task:
        """Обёртка для добавления задачи в начало очереди."""

        return self.task(builder, *args, priority=True, **kwargs)

    def is_idle(self) -> bool:
        """Проверяет, есть ли задачи в очереди."""

        return len(self._queue) == 0

    def queue_size(self) -> int:
        """Возвращает текущее количество задач в очереди."""

        return len(self._queue)

    def inventory_quantity(self, code: str) -> int:
        """Возвращает количество предмета code в инвентаре персонажа."""

        inventory = self.character.params.get("inventory", [])
        for item in inventory:
            if item.get("code") == code:
                return item.get("quantity", 0)
        return 0

    def run_next(self) -> bool:
        """Выполняет одну следующую задачу из очереди. Возвращает True, если задача была."""

        if not self._queue:
            return False

        task = self._queue.popleft()
        log.debug(f"{self.name} выполняет задачу {task.title}")
        plan = task.run()
        if plan is None:
            return True

        if plan.top:
            for top_task in reversed(plan.top):
                self._enqueue_task(top_task, priority=True)

        if plan.back:
            for back_task in plan.back:
                self._enqueue_task(back_task, priority=False)
        return True

    def run(self, max_steps: int | None = None) -> int:
        """Выполняет очередь задач без лимита или не более max_steps шагов."""

        steps_done = 0
        while (max_steps is None or steps_done < max_steps) and self.run_next():
            steps_done += 1
        return steps_done
