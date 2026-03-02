from __future__ import annotations

from dataclasses import dataclass
from math import ceil
from typing import Callable

from .main import Character
from helpers import utils
from helpers import setup_logger
from helpers.config import config

log = setup_logger("TASKS", config.LOG_PATH, config.LOG_LEVEL)


@dataclass
class Task:
    """Одна задача в очереди персонажа."""

    title: str
    run: Callable[[], TaskPlan | None]


@dataclass
class TaskPlan:
    """План постановки следующих задач после выполнения текущей."""

    top: list[Task] | None = None
    back: list[Task] | None = None


def drop_bank(character: Character, _return=True) -> Task:
    """Задача для сброса всего инвентаря в банк."""

    map_id = 334
    return_position = character.params.get("map_id")
    banks = utils.find_map("bank")
    if banks is not None:
        bank = utils.find_nearest_map(character.params, banks)
        if bank:
            map_id = bank

    def _run() -> TaskPlan | None:
        character.move(map_id)
        character.bank("all", quantity=0, action="deposit")
        if _return and return_position:
            character.move(return_position)
        return None

    return Task(
        title="Сброс инвентаря в банк",
        run=_run,
    )


def withdraw_bank(character: Character, list_items: list) -> Task:
    find_bank = utils.find_map("bank")
    if find_bank is not None:
        map_id = utils.find_nearest_map(character.params, find_bank)
    else:
        map_id = 334
    if map_id is None:
        map_id = 334

    keep_codes: set[str] = set()
    for item in list_items:
        code = item.get("code")
        if isinstance(code, str) and code:
            keep_codes.add(code)

    drop_items: list[dict[str, int | str]] = []
    for item in character.params.get("inventory", []):
        code = item.get("code")
        quantity = item.get("quantity", 0)
        if not isinstance(code, str) or not code:
            continue
        if code in keep_codes:
            continue
        if quantity <= 0:
            continue
        drop_items.append({"code": code, "quantity": quantity})

    def _run() -> TaskPlan | None:
        character.move(map_id)
        if drop_items:
            character.bank(code="", quantity=0, action="deposit", list_items=drop_items)
        character.bank(code="", quantity=0, action="withdraw", list_items=list_items)
        return None

    return Task(
        title="Взять ресурсы из банка",
        run=_run,
    )


def gather(
    character: Character,
    map_id: int,
    quantity: int,
) -> Task:
    """Создаёт возобновляемую задачу добычи с корректной очередью при полном инвентаре."""

    remaining = max(quantity, 0)
    task: Task

    def _run() -> TaskPlan | None:
        nonlocal remaining

        if remaining <= 0:
            return None

        if character.params.get("map_id") != map_id:
            character.move(map_id)

        error = character.gathering()
        if error == 497:
            return TaskPlan(top=[drop_bank(character), task])

        remaining -= 1
        if remaining > 0:
            return TaskPlan(top=[task])
        return None

    task = Task(
        title=f"Добыть {quantity} ресурса на карте {map_id}",
        run=_run,
    )
    return task


def craft(
    character: Character,
    code: str,
    quantity: int,
) -> Task:
    """Создаёт задачу для крафта предметов."""

    craft_item = utils.find_item(code)
    if not craft_item:
        log.warning(
            f"Невозможно создать задачу крафта: предмет с кодом {code} не найден"
        )
        return Task(
            title=f"Ошибка: предмет {code} не найден",
            run=lambda: None,
        )

    if craft_item.get("craft") is None:
        log.warning(
            f"Невозможно создать задачу крафта: предмет с кодом {code} не крафтится"
        )
        return Task(
            title=f"Ошибка: предмет {code} не крафтится",
            run=lambda: None,
        )

    craft_items = utils.calc_items(craft_item["craft"]["items"])
    craft_items *= quantity
    inventory_max_items = character.params.get("inventory_max_items", 0)
    if inventory_max_items > 0 and craft_items > inventory_max_items:
        chunks = ceil(craft_items / inventory_max_items)
        if chunks > 1:
            base_quantity = quantity // chunks
            remainder = quantity % chunks

            if base_quantity <= 0:
                log.warning(
                    f"Невозможно разбить крафт {code}: quantity={quantity}, chunks={chunks}"
                )
                return Task(
                    title=f"Ошибка: невозможно разбить крафт {code}",
                    run=lambda: None,
                )

            split_tasks: list[Task] = []

            def _make_chunk_task(chunk_quantity: int) -> Task:
                def _run_chunk() -> TaskPlan | None:
                    return TaskPlan(top=[craft(character, code, chunk_quantity)])

                return Task(
                    title=f"Подзадача крафта: {chunk_quantity} {code}",
                    run=_run_chunk,
                )

            for idx in range(chunks):
                chunk_quantity = base_quantity + (1 if idx < remainder else 0)
                if chunk_quantity > 0:
                    split_tasks.append(_make_chunk_task(chunk_quantity))

            def _run_split() -> TaskPlan | None:
                return TaskPlan(top=split_tasks)

            return Task(
                title=f"Скрафтить {quantity} {code} по частям ({chunks} раз)",
                run=_run_split,
            )

    skill = craft_item["craft"]["skill"]
    map_data = utils.find_map(skill)
    if map_data:
        map_id = utils.find_nearest_map(character.params, map_data)
        if map_id is None:
            map_id = character.params.get("map_id", 334)
    else:
        log.warning(
            f"Невозможно создать задачу крафта: карты с ресурсом {skill} не найдены"
        )
        return Task(
            title=f"Ошибка: карты с ресурсом {skill} не найдены",
            run=lambda: None,
        )

    inventory = utils.dict_quantity_items(character.params.get("inventory", []))
    list_item = utils.dict_quantity_items(craft_item["craft"]["items"])

    bank_withdraw: list[dict[str, int | str]] = []
    gather_items: dict[str, int] = {}

    for item_code, item_qty in list_item.items():
        required = item_qty * quantity
        in_inventory = inventory.get(item_code, 0)
        missing = required - in_inventory
        if missing <= 0:
            continue

        bank_qty = utils.check_bank_item(item_code) or 0
        available_in_bank = min(bank_qty, missing)

        if available_in_bank > 0:
            bank_withdraw.append({"code": item_code, "quantity": available_in_bank})

        remain_missing = missing - available_in_bank
        if remain_missing > 0:
            log.warning(
                f"Недостаточно ресурсов в инвентаре/банке для крафта {quantity} {code}: нужен {item_code} x{remain_missing}"
            )
            gather_items[item_code] = remain_missing

    top_tasks: list[Task] = []

    if gather_items:
        for item_code, item_qty in gather_items.items():
            sub_item = utils.find_item(item_code)
            if sub_item is None:
                continue
            if sub_item["craft"] is None:
                sub_code = utils.find_drop_code(sub_item["code"])
                if sub_code:
                    sub_map = utils.find_map(sub_code)
                    if sub_map:
                        sub_map_id = utils.find_nearest_map(character.params, sub_map)
                        if sub_map_id:
                            top_tasks.append(gather(character, sub_map_id, item_qty))
            else:
                top_tasks.append(craft(character, item_code, item_qty))

    if bank_withdraw:
        top_tasks.append(withdraw_bank(character, bank_withdraw))

    planned = False
    task: Task

    def _run() -> TaskPlan | None:
        nonlocal planned

        if not planned and top_tasks:
            planned = True
            return TaskPlan(top=[*top_tasks, task])

        if character.params.get("map_id") != map_id:
            character.move(map_id)
        character.craft(code, quantity)
        return None

    task = Task(
        title=f"Скрафтить {quantity} {code}",
        run=_run,
    )
    return task
