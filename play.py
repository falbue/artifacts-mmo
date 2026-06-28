import asyncio

from orchestrator import client
from orchestrator.models import Character
from orchestrator.utils.config import config

lamberjack = Character(config.LAMBERJACK_NAME, "lamberjack")


async def main():
    await client.init()

    await lamberjack.check()
    await lamberjack.move(376)

    await client.close()
    return


asyncio.run(main())
