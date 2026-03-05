# dispatcher.py
import asyncio
import logging
from typing import Optional, List, Any, Awaitable, Callable
from dataclasses import dataclass, field
from enum import Enum
import time

log = logging.getLogger("DISPATCHER")


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class Task:
    task_id: str  # Уникальный ID (например, "1", "1.2")
    name: str
    action: Callable[..., Awaitable[Any]]
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)
    priority: bool = False
    dependency: Optional["Task"] = None
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error_code: Optional[int] = None  # Код ошибки от API
    error_exception: Optional[Exception] = None


class TaskManager:
    def __init__(self, name: str = "DefaultManager"):
        self.name = name
        self._queue: asyncio.Queue[Task] = asyncio.Queue()
        self._priority_queue: List[Task] = []
        self._is_running = False
        self._worker_task: Optional[asyncio.Task] = None
        self._lock = asyncio.Lock()

        # Контекст
        self._ctx_priority: bool = False
        self._ctx_link: bool = False
        self._last_task: Optional[Task] = None

        # Генератор ID
        self._id_counter = 0
        self._current_prefix = ""

    async def start(self):
        if self._is_running:
            return
        self._is_running = True
        self._worker_task = asyncio.create_task(self._process_loop())

    async def stop(self):
        self._is_running = False
        if self._worker_task:
            self._worker_task.cancel()
            try:
                await self._worker_task
            except asyncio.CancelledError:
                pass

    def set_context(self, priority: bool, link: bool):
        self._ctx_priority = priority
        self._ctx_link = link
        if not link:
            self._last_task = None

    def get_next_id(self) -> str:
        """Генерирует следующий ID. Если есть префикс (вложенность), добавляет его."""
        self._id_counter += 1
        if self._current_prefix:
            return f"{self._current_prefix}.{self._id_counter}"
        return str(self._id_counter)

    def push_prefix(self, prefix: str):
        """Входит в режим вложенной генерации ID"""
        old_prefix = self._current_prefix
        self._current_prefix = prefix
        return old_prefix

    def pop_prefix(self, old_prefix: str):
        """Выходит из режима вложенности"""
        self._current_prefix = old_prefix
        self._id_counter = (
            0  # Сбрасываем счетчик для новой ветки? Или оставляем глобальным?
        )
        # Лучше сбрасывать локальный счетчик внутри префикса, но глобальный counter пусть растет.
        # Для простоты: просто восстанавливаем префикс. Счетчик пусть будет глобальным уникальным суффиксом.
        # Исправление: чтобы ID были красивыми (3.1, 3.2), счетчик лучше сбрасывать при входе в префикс,
        # но тогда нужно хранить состояние стека.
        # Упрощенный вариант: используем глобальный счетчик всегда, просто добавляем префикс.
        # ID будет: 3.105, 3.106. Это тоже уникально.
        # Если нужны красивые 3.1, 3.2 - нужен стек счетчиков. Сделаем проще:
        self._current_prefix = old_prefix

    async def add_task(self, task: Task) -> Task:
        # Применяем контекст
        if self._ctx_priority:
            task.priority = True

        if self._ctx_link and task.dependency is None and self._last_task:
            task.dependency = self._last_task

        if self._ctx_link:
            self._last_task = task

        async with self._lock:
            if task.priority:
                self._priority_queue.insert(0, task)
            else:
                await self._queue.put(task)

        # Ждем выполнения задачи и возвращаем результат
        return await self._wait_for_task(task)

    async def _wait_for_task(self, task: Task) -> Task:
        """Ждет завершения конкретной задачи"""
        while task.status in [TaskStatus.PENDING, TaskStatus.RUNNING]:
            await asyncio.sleep(0.05)
        return task

    async def _process_loop(self):
        while self._is_running:
            task = await self._get_next_task()
            if task is None:
                await asyncio.sleep(0.05)
                continue

            # Проверка зависимостей
            if task.dependency:
                if task.dependency.status != TaskStatus.COMPLETED:
                    task.status = TaskStatus.SKIPPED
                    if task.dependency.error_code:
                        task.error_code = task.dependency.error_code
                    continue

            task.status = TaskStatus.RUNNING
            try:
                # Вызываем метод персонажа
                # Ожидаем, что метод возвращает None (успех) или int (код ошибки)
                result = await task.action(*task.args, **task.kwargs)

                if result is None:
                    task.status = TaskStatus.COMPLETED
                    task.result = result
                else:
                    # Считаем любое не-None значение кодом ошибки
                    task.status = TaskStatus.FAILED
                    task.error_code = int(result) if isinstance(result, int) else 999

            except Exception as e:
                task.status = TaskStatus.FAILED
                task.error_exception = e
                task.error_code = 999  # Системная ошибка
                log.error(
                    f"[{self.name}] Исключение в {task.task_id}: {e}", exc_info=True
                )

    async def _get_next_task(self) -> Optional[Task]:
        async with self._lock:
            if self._priority_queue:
                return self._priority_queue.pop(0)
            if not self._queue.empty():
                return await self._queue.get()
            return None
