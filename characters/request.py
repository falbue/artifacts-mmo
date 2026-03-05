import asyncio
import aiohttp
import helpers
from helpers import utils

from aiohttp import TCPConnector
from aiohttp.resolver import ThreadedResolver

HOST = "https://api.artifactsmmo.com"

log = helpers.setup_logger(
    "CHARACTER", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL
)


class Character:
    def __init__(self, name: str, session: aiohttp.ClientSession | None = None) -> None:
        self.name = name
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
        """Закрываем сессию, только если создали её сами"""
        if self._own_session and not self.session.closed:
            await self.session.close()
            log.debug(f"{self.name} отключён")

    @classmethod
    async def create(
        cls, name: str, session: aiohttp.ClientSession | None = None
    ) -> "Character | None":
        instance = cls(name, session)

        try:
            async with instance.session.get(
                f"{HOST}/characters/{instance.name}",
                headers=instance.header,
            ) as response:
                raw_character = await response.json()
        except Exception as e:
            log.error(f"Ошибка сети при загрузке персонажа {instance.name}: {e}")
            if instance._own_session:
                await instance.close()
            return None

        if raw_character.get("error"):
            log.error(
                f"Ошибка при загрузке персонажа {instance.name}: {raw_character['error']}"
            )
            if instance._own_session:
                await instance.close()
            return None

        instance.params = raw_character.get("data", {})
        return instance

    async def action(self, url: str, body: dict | list | None = None) -> dict:
        base_url = f"{HOST}/my/{self.name}/action{url}"

        async with self.session.post(
            base_url, headers=self.header, json=body
        ) as response:
            if response.status == 200:
                data = await response.json()

            elif response.status == 499:
                time_sleep = utils.difference_time(
                    str(self.params.get("cooldown_expiration", ""))
                )
                log.debug(f"{self.name} в кулдауне на {time_sleep} сек.")
                await asyncio.sleep(time_sleep)

                async with self.session.post(
                    base_url, headers=self.header, json=body
                ) as resonse:
                    data = await resonse.json()
            else:
                error = utils.localize_error(str(response.status))
                log.warning(f"{response.status} {error}")
                return {"error": response.status}

        return data.get("data", {})

    async def move(self, map_id: int) -> None | int:
        body = {"map_id": map_id}
        data = await self.action("/move", body)
        if data.get("error") is None:
            log.debug(f"{self.name} переместился на {map_id}")
            self.params = data.get("character", {})
            return
        return int(data.get("error", 0))

    async def gather(self) -> None | int:
        data = await self.action("/gathering")
        if data.get("error") is None:
            log.debug(f"{self.name} добыл ресурс")
            self.params = data.get("character", {})
            return
        return int(data.get("error", 0))

    async def bank(
        self,
        code: str,
        quantity: int = 1,
        action: str = "deposit",
        list_items: list | None = None,
    ) -> None:
        if action not in ["deposit", "withdraw"]:
            log.error(f"Неверное действие для банка: {action}")
            return

        type_item = "item"

        if list_items is not None:
            body = list_items
        elif code == "gold":
            body = {
                "quantity": self.params.get("gold", 0) if quantity == 0 else quantity
            }
            type_item = "gold"
        elif quantity == 0 and code == "all" and action == "deposit":
            inventory = self.params.get("inventory", [])
            body = [
                {"code": item.get("code"), "quantity": item.get("quantity", 0)}
                for item in inventory
                if item.get("code")
            ]
        elif (quantity == 0 or code == "all") and action == "withdraw":
            log.error("Невозможно взять всё из банка")
            return
        else:
            body = [{"code": code, "quantity": quantity}]

        data = await self.action(f"/bank/{action}/{type_item}", body)
        if data is not None:
            log.debug(f"{self.name} использовал банк ({quantity} {code} {action})")
            self.params = data.get("character", {})

    async def craft(self, code: str, quantity: int = 1) -> None:
        body = {"code": code, "quantity": quantity}
        data = await self.action("/crafting", body)
        if data is not None:
            log.debug(f"{self.name} создал {quantity} {code}")
            self.params = data.get("character", {})


async def create_character(
    name: str, skin: str = "men1", session: aiohttp.ClientSession | None = None
) -> Character | None:
    """
    Асинхронное создание персонажа.
    Если session не передан — Character создаст свою собственную.
    """
    url = f"{HOST}/characters/create"
    headers = {"Authorization": f"Bearer {helpers.config.AUTH}"}
    body = {"name": name, "skin": skin}

    # Создаём персонажа (сессия создастся внутри, если не передана)
    character = Character(name, session=session)

    try:
        async with character.session.post(url, headers=headers, json=body) as response:
            if response.status != 200:
                error = utils.localize_error(str(response.status))
                log.error(f"Ошибка при создании персонажа {name}: {error}")
                if character._own_session:
                    await character.close()
                return None
            log.debug(f"Персонаж {name} успешно создан")

        # Инициализируем данные персонажа
        async with character.session.get(
            f"{HOST}/characters/{name}", headers=character.header
        ) as response:
            raw_character = await response.json()

        if raw_character.get("error"):
            log.error(
                f"Ошибка при загрузке данных персонажа {name}: {raw_character['error']}"
            )
            if character._own_session:
                await character.close()
            return None

        character.params = raw_character.get("data", {})
        return character

    except Exception as e:
        log.error(f"Непредвиденная ошибка при создании персонажа {name}: {e}")
        if character._own_session:
            await character.close()
        return None
