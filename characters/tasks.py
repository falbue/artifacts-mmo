from typing import Optional, Tuple
from contextlib import asynccontextmanager
from .dispatcher import TaskManager, Task
from .request import Character
from objects import maps
from helpers import logger
from helpers import config

log = logger.setup_logger("TASKS", config.LOG_PATH, config.LOG_LEVEL)


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

    async def crafting(self, code: str, quantity: int):
        data = await maps.find_craftable(code)
        if data is None:
            return

        if self.char.params.get("level", 0) < data.get("level", 0):
            log.warning(f"Недостаточный уровень для крафта {code}")
            return

    async def gathering(self, resource_code: str, quantity: int):
        remaining = quantity

        work_map = await maps.find_map_resource(self.char.params, resource_code)
        if work_map is None:
            return

        banks = await maps.find_map("bank")
        if banks is None:
            return
        bank_map = maps.find_nearest_map(self.char.params, banks)
        if bank_map is None:
            return

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

        return quantity
