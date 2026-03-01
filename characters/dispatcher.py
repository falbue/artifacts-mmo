from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Callable, Any

import helpers

from .main import Character

log = helpers.setup_logger(
    "DISPATCHER", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL
)


@dataclass
class Task:
    """Одна задача в очереди персонажа."""

    title: str
    run: Callable[[], None]


class CharacterWorker:
    def __init__(self, name: str) -> None:
        """Создаёт воркера для конкретного персонажа по имени."""

        self.character = Character(name)
        self.name = name
        self._queue: deque[Task] = deque()
        self._next_priority = False

    def _enqueue_task(self, task: Task, priority: bool | None = None) -> None:
        """Внутренний метод постановки задачи в очередь с учётом внешнего приоритета."""

        use_priority = self._next_priority if priority is None else priority
        self._next_priority = False
        if use_priority:
            self._queue.appendleft(task)
            return
        self._queue.append(task)

    def enqueue(self, task: Task) -> None:
        """Добавляет задачу в конец очереди."""

        self._enqueue_task(task, priority=False)

    def enqueue_priority(self, task: Task) -> None:
        """Добавляет задачу в начало очереди (высокий приоритет)."""

        self._enqueue_task(task, priority=True)

    def enqueue_call(
        self,
        action: Callable[..., None],
        *args: Any,
        priority: bool = False,
        **kwargs: Any,
    ) -> None:
        """
        Вызывает action(*args, **kwargs), помечая задачи этого вызова приоритетом.

        Так можно задавать приоритет извне без отдельного параметра в каждой функции.
        """

        self._next_priority = priority
        try:
            action(*args, **kwargs)
        finally:
            self._next_priority = False

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

    def gather_resource(self, map_id: int, quantity: int) -> None:
        """
        Добавляет составную задачу добычи ресурса в очередь.

        Внутри выполняет:
        1) перемещение на map_id,
        2) quantity раз добычу через gathering().
        """

        def _run() -> None:
            self.character.move(map_id)
            for _ in range(max(quantity, 0)):
                self.character.gathering()

        task = Task(
            title=f"Ресурс добыт:{map_id}:{quantity}",
            run=_run,
        )
        self._enqueue_task(task)

    def run_next(self) -> bool:
        """Выполняет одну следующую задачу из очереди. Возвращает True, если задача была."""

        if not self._queue:
            return False

        task = self._queue.popleft()
        log.debug(f"{self.name} выполняет задачу {task.title}")
        task.run()
        return True

    def run_step(self) -> bool:
        """Шаг выполнения воркера: сейчас это выполнение одной задачи."""
        return self.run_next()

    def run(self, max_steps: int | None = None) -> int:
        """Выполняет очередь задач без лимита или не более max_steps шагов."""

        steps_done = 0
        while (max_steps is None or steps_done < max_steps) and self.run_step():
            steps_done += 1
        return steps_done
