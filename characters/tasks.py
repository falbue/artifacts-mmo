from typing import Optional, Tuple
from contextlib import asynccontextmanager
from .manager import TaskManager, Task
from .request import Character
from objects import maps
from helpers import logger
from helpers import config
from helpers import utils

log = logger.setup_logger("TASKS", config.LOG_PATH, config.LOG_LEVEL)


async def find_bank(character: Character) -> int | None:
    banks = await maps.find_map("bank")
    if banks is None:
        return
    bank_map = maps.find_nearest_map(character.params, banks)
    if bank_map is None:
        return
    return bank_map


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
            name=f"Перемещение на {map_id}",
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
                name=f"Добыча {resource_code}",
                action=self.char.gather,
                args=(),
            )
            completed_task = await self.manager.add_task(task)
            print(completed_task)

            if completed_task.error_code is not None:
                return success_count, completed_task.error_code

            success_count += 1

        return success_count, None

    async def drop_bank(self) -> Optional[int]:
        bank_map = await find_bank(self.char)
        if bank_map is None:
            return 999
        await self.move(bank_map)
        tid = self.manager.get_next_id()
        task = Task(
            task_id=tid,
            name="Сбросить предметы в банк",
            action=self.char.bank,
            kwargs={"code": "all", "quantity": 0, "action": "deposit"},
        )
        completed_task = await self.manager.add_task(task)
        return completed_task.error_code

    async def withdraw_bank(self, data: list) -> Optional[int]:
        bank_map = await find_bank(self.char)
        if bank_map is None:
            return

        async with self.chain(priority=True, stop_on_error=True):
            await self.move(bank_map)

        tid = self.manager.get_next_id()
        task = Task(
            task_id=tid,
            name="Взять предметы из банка",
            action=self.char.bank,
            kwargs={
                "code": "",
                "quantity": 0,
                "list_items": data,
                "action": "withdraw",
            },
        )
        completed_task = await self.manager.add_task(task)
        return completed_task.error_code

    async def crafting(self, code: str, quantity: int):
        craft = await maps.find_craftable(code)
        if craft is None:
            return

        if self.char.params.get("level", 0) < craft.get("level", 0):
            log.warning(f"Недостаточный уровень для крафта {code}")
            return

        skill = craft.get("skill")
        if skill is None:
            log.warning(f"Навык для крафта {code} не найден")
            return

        items = craft.get("items", [])
        if not items:
            log.warning(f"Ресурсы для крафта {code} не найдены")
            return

        max_items = self.char.params.get("inventory_max_items", 1)
        items_per_craft = utils.calc_items(items)

        if items_per_craft * quantity > max_items:
            total_items_needed = items_per_craft * quantity
            recycle = -(-total_items_needed // max_items)

            craft_qty_per_step = quantity // recycle
            remainder = quantity % recycle

            for i in range(recycle):
                current_qty = craft_qty_per_step + (
                    remainder if i == recycle - 1 else 0
                )
                await self.crafting(code, current_qty)
                return

        raw_inventory = self.char.params.get("inventory", [])
        inventory = utils.dict_quantity_items(raw_inventory)
        get_bank = [
            {
                "code": item["code"],
                "quantity": item["quantity"] - inventory.get(item["code"], 0),
            }
            for item in items
            if inventory.get(item["code"], 0) < item["quantity"]
        ]

        if get_bank:
            result = await self.withdraw_bank(get_bank)
            if result is not None:
                async with self.chain(priority=True, stop_on_error=True):
                    await self.drop_bank()
                    await self.withdraw_bank(get_bank)

        maps_ = await maps.find_map(skill)
        if maps_ is None:
            return

        map_id = maps.find_nearest_map(self.char.params, maps_)
        if map_id is None:
            return
        await self.move(map_id)

        tid = self.manager.get_next_id()
        task = Task(
            task_id=tid,
            name=f"Крафт {code}",
            action=self.char.craft,
            kwargs={"code": code, "quantity": quantity},
        )
        completed_task = await self.manager.add_task(task)
        return completed_task.error_code

    async def gathering(self, resource_code: str, quantity: int):
        remaining = quantity

        work_map = await maps.find_map_resource(self.char.params, resource_code)
        if work_map is None:
            return

        banks = await maps.find_map("bank")
        if banks is None:
            return

        while remaining > 0:
            await self.move(work_map)

            count, err_code = await self.gather(resource_code, remaining)
            remaining -= count

            if err_code is None:
                break

            if err_code == 497:
                async with self.chain(priority=True, stop_on_error=True):
                    await self.drop_bank()
                    await self.move(work_map)
                continue

        return quantity
