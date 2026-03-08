import asyncio
from characters import Character, TaskManager, QuestBuilder


async def main():
    char = Character("oleg")
    manager = TaskManager()
    tasks = QuestBuilder(manager, char)
    await manager.start()
    # await tasks.gather("copper_ore", 1)
    await tasks.drop_bank()
    await char.close()


if __name__ == "__main__":
    asyncio.run(main())
