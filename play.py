import asyncio
from characters.main import Character


async def main():
    name = await Character.create("valera")
    if name is None:
        return
    await name.move(277)
    await name.move(334)
    await name.bank("copper_bar", 1)
    await name.bank("all", 0, "deposit")
    await name.bank("copper_bar", 1, "withdraw")


asyncio.run(main())
