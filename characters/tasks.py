# tasks_builder.py
import asyncio
from typing import Optional, Tuple
from contextlib import asynccontextmanager
from .dispatcher import TaskManager, Task, TaskStatus
from .request import Character


class QuestBuilder:
    def __init__(self, manager: TaskManager, character: Character):
        self.manager = manager
        self.char = character

    @asynccontextmanager
    async def chain(
        self,
        priority: bool = True,
        stop_on_error: bool = True,
        task_group_id: Optional[str] = None,
    ):
        old_priority = self.manager._ctx_priority
        old_link = self.manager._ctx_link
        old_prefix = None

        if task_group_id:
            old_prefix = self.manager.push_prefix(task_group_id)

        self.manager.set_context(priority=priority, link=stop_on_error)

        try:
            yield
        finally:
            self.manager.set_context(priority=old_priority, link=old_link)
            if task_group_id and old_prefix:
                self.manager.pop_prefix(old_prefix)

    async def move(self, map_id: int) -> Optional[int]:
        tid = self.manager.get_next_id()
        task = Task(
            task_id=tid,
            name=f"Move to {map_id}",
            action=self.char.move,
            args=(map_id,),
        )
        completed_task = await self.manager.add_task(task)
        return completed_task.error_code

    async def gather(
        self, resource_code: str, quantity: int
    ) -> Tuple[int, Optional[int]]:
        """
        Добывает пока не получится или не выйдет ошибка.
        Возвращает кортеж: (сколько успешно добыто, код ошибки или None).
        """
        success_count = 0

        for i in range(quantity):
            tid = self.manager.get_next_id()
            task = Task(
                task_id=tid,
                name=f"Gather {resource_code}",
                action=self.char.gather,
                args=(),
            )
            completed_task = await self.manager.add_task(task)

            if completed_task.error_code is not None:
                # Прерываем цикл при первой ошибке
                return success_count, completed_task.error_code

            success_count += 1

        return success_count, None

    async def drop_bank(self) -> Optional[int]:
        tid = self.manager.get_next_id()
        task = Task(
            task_id=tid,
            name="Drop bank items",
            action=self.char.bank,
            kwargs={"code": "all", "quantity": 0, "action": "deposit"},
        )
        completed_task = await self.manager.add_task(task)
        return completed_task.error_code

    async def smart_mining_cycle(
        self,
        resource_code: str,
        total_needed: int,
        work_map: int = 277,
        bank_map: int = 334,
        max_fails: int = 3,
    ):
        """
        Простая логика:
        1. Идем на work_map.
        2. Добываем total_needed.
        3. Если ошибка 497 -> Банк (ПРИОРИТЕТ) -> Возврат (ПРИОРИТЕТ) -> Продолжаем добывать остаток.
        4. Иная ошибка -> Стоп.
        """
        remaining = total_needed

        while remaining > 0:
            await self.move(work_map)

            count, err_code = await self.gather(resource_code, remaining)
            remaining -= count

            if err_code is None:
                break

            if err_code == 497:
                async with self.chain(priority=True, stop_on_error=True):
                    await self.move(bank_map)
                    await self.drop_bank()
                    await self.move(work_map)
                continue

        return total_needed
