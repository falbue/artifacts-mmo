import asyncio
import aiohttp
from characters import Character
from characters import TaskManager
from characters import QuestBuilder


async def main():
    # 2. Инициализируем персонажа (замени 'MyHero' на имя своего чара)
    char = await Character.create("oleg")

    if not char:
        print("❌ Не удалось загрузить персонажа!")
        return

    # 3. Создаем менеджер задач и билдер
    manager = TaskManager(name="MiningBot")
    builder = QuestBuilder(manager, char)

    # 4. Запускаем обработчик очередей
    await manager.start()

    try:
        print("🚀 Запуск умной добычи...")

        # 5. Вызываем твою функцию
        # total_needed=300 -> добудет 300 штук, даже если придется ходить в банк 10 раз
        total_mined = await builder.smart_mining_cycle(
            resource_code="copper_ore",
            total_needed=300,
            work_map=277,
            bank_map=334,
            max_fails=3,
        )

    except KeyboardInterrupt:
        print("\n⚠️ Остановка пользователем...")
    finally:
        # 6. Корректная остановка
        await manager.stop()
        # Сессию закроет контекстный менеджер (async with) автоматически


if __name__ == "__main__":
    asyncio.run(main())
