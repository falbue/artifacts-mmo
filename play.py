import asyncio

from orchestrator import client, setup_logger
from orchestrator.models import Character
from orchestrator.utils.config import config
from orchestrator.core.scheduler import Scheduler
from orchestrator.core.resolver import DependencyResolver
from orchestrator.core.move_planner import MovePlanner
from orchestrator.core.task_manager import TaskManager

log = setup_logger("TEST")
miner = Character(config.MINER_NAME, "miner")


async def main():
    await client.init()

    await miner.check()
    log.info(f"Персонаж: {miner.name}, level: {getattr(miner, 'level', '?')}")

    scheduler = Scheduler([miner])
    resolver = DependencyResolver(client)
    move_planner = MovePlanner(client)

    task_manager = TaskManager(
        characters=[miner],
        scheduler=scheduler,
        resolver=resolver,
        move_planner=move_planner,
        achievement_planner=None,
    )

    goal = {"type": "craft", "item": "copper_bar", "quantity": 1}

    try:
        # Запустить scheduler и runner как отдельные задачи
        scheduler_task = asyncio.create_task(scheduler.run())
        runner_task = asyncio.create_task(miner_loop(miner, scheduler))

        # Выполнить цель
        await task_manager.execute_goal(goal)

        # После завершения цели — отменить бесконечные циклы
        scheduler_task.cancel()
        runner_task.cancel()

        try:
            await scheduler_task
            await runner_task
        except asyncio.CancelledError:
            log.info("Scheduler и Runner остановлены")

    except Exception as e:
        log.error(f"Ошибка: {e}", exc_info=True)
    finally:
        await client.close()


async def miner_loop(character, scheduler):
    """Цикл персонажа."""
    from orchestrator.core.runner import character_loop

    await character_loop(character, scheduler)


if __name__ == "__main__":
    asyncio.run(main())
