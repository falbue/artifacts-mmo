import asyncio

from orchestrator.core.runner import character_loop
from orchestrator.core.scheduler import Scheduler
from orchestrator import client
from orchestrator.models import Character
from orchestrator.models.task import Task, TaskType
from orchestrator.utils.config import config

# ИСПРАВЛЕНО: правильное написание роли
lumberjack = Character(config.LAMBERJACK_NAME, "Lumberjack")


async def main():
    await client.init()

    # Проверить что персонаж существует
    await lumberjack.check()
    print(f"Персонаж: {lumberjack.name}, level: {getattr(lumberjack, 'level', '?')}")

    # Создать простую задачу для теста
    task = Task(
        type=TaskType.MOVE,
        resource="map_move",
        quantity_total=1,
        target_location=274,
        assignee_class="Lumberjack",  # Должно совпадать с ролью персонажа
    )

    # Создать планировщик
    scheduler = Scheduler([lumberjack])
    scheduler.add_tasks([task])

    # ИСПРАВЛЕНО: только один вызов scheduler.run()
    await asyncio.gather(
        character_loop(lumberjack, scheduler),
        scheduler.run(),
    )

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
