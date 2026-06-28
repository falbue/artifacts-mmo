import asyncio

from orchestrator import client
from orchestrator.models import Character
from orchestrator.utils.config import config

lamberjack = Character(config.LAMBERJACK_NAME, "lamberjack")


async def main():
    await client.init()

    await lamberjack.check()
    await lamberjack.move(274)
    await asyncio.sleep(lamberjack.cooldown)
    await lamberjack.move(277)
    await asyncio.sleep(lamberjack.cooldown)
    await lamberjack.gather()

    await client.close()


asyncio.run(main())
