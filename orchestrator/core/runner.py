import asyncio
from orchestrator.models.task import TaskStatus, TaskType
from orchestrator import setup_logger
from orchestrator.utils.helpers import check_gather

log = setup_logger("RUNNER")


async def character_loop(character, scheduler):
    """
    Основной цикл персонажа
    """
    task_queue = scheduler.task_queues[character.name]

    while True:
        try:
            cooldown = character.is_available()
            if cooldown > 0:
                log.debug(f"{character.name} ждёт кулдаун {cooldown}s")
                await asyncio.sleep(cooldown + 0.1)
                continue

            try:
                task = task_queue.get_nowait()
            except asyncio.QueueEmpty:
                await asyncio.sleep(0.1)
                continue

            done = await execute_task_tick(character, task)

            if done:
                task.status = TaskStatus.DONE
                scheduler.notify_task_done(character.name, task)
                log.info(f"{character.name} Задача завершена: {task}")
            else:
                await task_queue.put(task)

        except Exception as e:
            log.error(f"{character.name} Ошибка в цикле: {e}")
            await asyncio.sleep(1)


async def execute_task_tick(character, task) -> bool:
    """
    Выполнить один такт текущей задачи.

    Один такт = один HTTP-запрос к API.

    Returns:
        True если задача полностью завершена, False если нужны ещё такты.
    """

    if task.type == TaskType.MOVE:
        return await tick_move(character, task)

    elif task.type == TaskType.GATHER:
        return await tick_gather(character, task)

    elif task.type == TaskType.CRAFT:
        return await tick_craft(character, task)

    elif task.type == TaskType.COMBAT:
        return await tick_combat(character, task)

    elif task.type == TaskType.DEPOSIT:
        return await tick_deposit(character, task)

    elif task.type == TaskType.WITHDRAW:
        return await tick_withdraw(character, task)

    else:
        log.error(f"{character.name} Неизвестный тип задачи: {task.type}")
        return False


async def tick_move(character, task) -> bool:
    map_id = task.target_location
    await character.move(map_id)

    log.info(f"{character.name} переместился на карту {map_id}")
    return True


async def tick_gather(character, task) -> bool:
    """Собрать один ресурс. Может не выпасть (шанс < 100%)"""
    response = await character.gather()
    quantity = check_gather(response, task.resource)

    if quantity > 0:
        task.quantity_done += quantity
        log.debug(
            f"{character.name} собрал {task.resource}: {task.quantity_done}/{task.quantity_total}"
        )
    else:
        log.debug(f"{character.name} ресурс не выпал, повторяю")

    return task.is_done()


async def tick_craft(character, task) -> bool:
    """Скрафтить один предмет"""
    await character.craft(task.resource)

    task.quantity_done += 1
    log.debug(
        f"{character.name} Скрафтил {task.resource}: {task.quantity_done}/{task.quantity_total}"
    )

    return task.is_done()


async def tick_combat(character, task) -> bool:
    """Напасть на моба. Может не выпасть дроп (шанс < 100%)"""
    # TODO: получить target_id из task или найти ближайшего моба
    target_id = getattr(task, "target_id", 1)

    response = await character.combat(target_id)

    # Проверить результат боя
    if response.get("data", {}).get("fight", {}).get("xp_gained"):
        task.quantity_done += 1
        log.debug(
            f"{character.name} Победил моба: {task.quantity_done}/{task.quantity_total}"
        )
    else:
        log.warning(f"{character.name} Бой не удался")

    return task.is_done()


async def tick_deposit(character, task) -> bool:
    """Положить ресурсы в банк."""
    await character.bank_deposit(task.resource, task.quantity_total)

    log.info(f"{character.name} Положил в банк {task.quantity_total}x {task.resource}")
    return True


async def tick_withdraw(character, task) -> bool:
    """Взять ресурсы из банка."""
    success = await character.bank_withdraw(task.resource, task.quantity_total)

    if success:
        log.info(
            f"{character.name} Взял из банка {task.quantity_total}x {task.resource}"
        )
        return True
    else:
        log.warning(f"{character.name} Не удалось взять из банка {task.resource}")
        return False
