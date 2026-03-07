import aiohttp
import helpers
from helpers import utils

from aiohttp import TCPConnector
from aiohttp.resolver import ThreadedResolver

HOST = "https://api.artifactsmmo.com"

log = helpers.setup_logger("ACCOUNT", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL)


class Account:
    def __init__(self, session: aiohttp.ClientSession | None = None) -> None:
        self._own_session = session is None

        connector = TCPConnector(resolver=ThreadedResolver())

        self.session = (
            session
            if session is not None
            else aiohttp.ClientSession(connector=connector)
        )

        self.header = {"Authorization": f"Bearer {helpers.config.AUTH}"}
        self.params: dict = {}

    async def close(self) -> None:
        if self._own_session and not self.session.closed:
            await self.session.close()

    async def request(self, url: str, body: dict | list | None = None) -> dict:
        base_url = f"{HOST}/my{url}"

        async with self.session.post(
            base_url, headers=self.header, json=body
        ) as response:
            if response.status == 200:
                data = await response.json()
            else:
                error = utils.localize_error(str(response.status))
                log.warning(f"{response.status} {error}")
                return {"error": response.status}

        return data

    async def bank_items(self, size: int = 50, code: str | None = None) -> dict:
        url = f"/bank/items?size={size}"
        if code is not None:
            url += f"&item_code={code}"
        result = await self.request(url)
        return result.get("data", [])
