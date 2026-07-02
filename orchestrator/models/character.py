import asyncio
from datetime import datetime, timezone
import math

from orchestrator import client, setup_logger
from orchestrator.api_client import check_time_diff

log = setup_logger("CHARACTER")


class Character:
    def __init__(self, name, role):
        self.name: str = name.split(":")[0]
        self.role: str = role
        self.skin: str = name.split(":")[1]
        self.client = client
        self.cooldown: int = 0
        self.cooldown_expiration: str = ""
        self.time_diff: int = asyncio.run(check_time_diff())

    def _unpack_to_self(self, data):
        if data.get("data", {}).get("character"):
            character = data["data"]["character"]
        else:
            character = data

        for key, value in character.items():
            if key != "inventory":
                setattr(self, key, value)

        if "inventory" in character:
            self.inventory = character["inventory"]

    def is_available(self):
        """
        Проверка доступности персонажа

        Returns:
            0 если свободен
            положительное число — сколько секунд ждать
        """
        cooldown = datetime.fromisoformat(
            self.cooldown_expiration.replace("Z", "+00:00")
        )
        local_time = datetime.now(timezone.utc)
        diff_seconds = (cooldown - local_time).total_seconds()

        if diff_seconds <= 0:
            return 0

        return math.ceil(diff_seconds)

    async def create(self):
        data = {"name": self.name, "skin": self.skin}
        response = await self.client.post("/characters/create", data)
        if response["status"] != 200:
            await self.client.close()
        log.info(f"Персонаж {self.name} создан")
        return response

    async def check(self):
        response = await self.client.get(f"/characters/{self.name}")
        if response["status"] != 200:
            response = await self.create()
        self._unpack_to_self(response["data"])
        log.debug(f"Данные персонажа {self.name} получены")
        return

    async def move(self, map_id: int):
        response = await self.client.post(
            f"/my/{self.name}/action/move", {"map_id": map_id}
        )
        if response["status"] == 200:
            self._unpack_to_self(response)
            log.debug(f"{self.name} переместился на карту {map_id}")
        return

    async def gather(self):
        response = await self.client.post(f"/my/{self.name}/action/gathering")
        if response["status"] == 200:
            self._unpack_to_self(response)
            log.debug(f"{self.name} добыл")
        return response["data"]
