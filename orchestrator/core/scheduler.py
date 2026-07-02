import asyncio
from asyncio import Queue
from orchestrator.models.task import Task, TaskStatus
from orchestrator.utils.logger import setup_logger

log = setup_logger("SCHEDULER")


class Scheduler:
    """Планировщик задач на основе очереди"""

    def __init__(self, characters: list):
        self.characters = {char.name: char for char in characters}
        self.all_tasks: dict[str, Task] = {}
        self.task_queues: dict[str, Queue] = {char.name: Queue() for char in characters}
        self.new_task_event = asyncio.Event()

    async def run(self):
        """Основной цикл: разблокирует задачи и распределяет по очередям"""
        while True:
            try:
                ready_tasks = [
                    t
                    for t in self.all_tasks.values()
                    if t.status == TaskStatus.READY and not t.blocked_by
                ]

                for task in ready_tasks:
                    character = self._find_available_character(task)
                    if character:
                        await self.task_queues[character.name].put(task)
                        task.status = TaskStatus.RUNNING
                        log.debug(
                            f"Задача поставлена в очередь {character.name}: {task}"
                        )

                try:
                    await asyncio.wait_for(self.new_task_event.wait(), timeout=0.5)
                    self.new_task_event.clear()
                except asyncio.TimeoutError:
                    pass

            except Exception as e:
                log.error(f"Ошибка в планировщике: {e}")
                await asyncio.sleep(1)

    def _find_available_character(self, task: Task):
        """Найти свободного персонажа подходящего класса"""
        for char in self.characters.values():
            if char.role == task.assignee_class and char.is_available() <= 0:
                return char
        return None

    def add_tasks(self, tasks: list[Task]):
        """Добавить задачи и уведомить планировщик"""
        for task in tasks:
            self.all_tasks[task.id] = task
            if not task.blocked_by:
                task.status = TaskStatus.READY
                log.debug(f"Добавлена задача: {task}")

        self.new_task_event.set()

    def notify_task_done(self, character_name: str, task: Task):
        """Задача завершена — разблокируем зависимые"""
        log.info(f"Завершена: {task}")

        newly_ready = []
        for t in self.all_tasks.values():
            if task.id in t.blocked_by:
                t.blocked_by.remove(task.id)
                if not t.blocked_by:
                    t.status = TaskStatus.READY
                    newly_ready.append(t)

        if newly_ready:
            self.new_task_event.set()

    def get_task_stats(self) -> dict:
        """Статистика по задачам."""
        total = len(self.all_tasks)
        pending = sum(
            1 for t in self.all_tasks.values() if t.status == TaskStatus.PENDING
        )
        ready = sum(1 for t in self.all_tasks.values() if t.status == TaskStatus.READY)
        running = sum(
            1 for t in self.all_tasks.values() if t.status == TaskStatus.RUNNING
        )
        done = sum(1 for t in self.all_tasks.values() if t.status == TaskStatus.DONE)
        failed = sum(
            1 for t in self.all_tasks.values() if t.status == TaskStatus.FAILED
        )

        return {
            "total": total,
            "pending": pending,
            "ready": ready,
            "running": running,
            "done": done,
            "failed": failed,
        }
