import asyncio
from characters import Character, TaskManager, QuestBuilder

async def main():
    configs = [
        ("oleg", "iron_ore", 1869),
        ("valera", "ash_wood", 5899),
        ("ivan", "gudgeon", 6000),
        ("kaban", "sunflower", 6000),
    ]
    sessions, tasks = [], []
    try:
        for name, res, qty in configs:
            char = await Character.create(name)
            if not char:
                return
            manager = TaskManager(name=char.params["name"])
            await manager.start()
            builder = QuestBuilder(manager, char)
            sessions.append((char, manager))
            tasks.append(builder.gathering(res, qty))

        print(await asyncio.gather(*tasks))
    except Exception as e:
        print(e)
    finally:
        for char, manager in sessions:
            await manager.stop()
            await char.close()

if __name__ == "__main__":