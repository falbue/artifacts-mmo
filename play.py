import asyncio
from characters.request import Character
from helpers import utils

utils.synchronize_time()


async def main():
    name = await Character.create("valera")
    if name is None:
        return
    await name.move(277)
    await name.move(334)
    await name.bank("copper_bar", 1)
    await name.bank("all", 0, "deposit")
    await name.bank("copper_bar", 1, "withdraw")
    await name.close()


asyncio.run(main())
