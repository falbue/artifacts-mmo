import asyncio
from characters import Character
from characters import TaskManager
from characters import QuestBuilder


async def main():
    char = await Character.create("valera")
    if char is None:
        return
    manager = TaskManager(name=char.params["name"])
    builder = QuestBuilder(manager, char)

    await manager.start()

    try:
        result = await builder.gathering("ash_wood", 300)

        print(result)
    except Exception as e:
        print(e)
    finally:
        await manager.stop()
        await char.close()


if __name__ == "__main__":
    asyncio.run(main())
