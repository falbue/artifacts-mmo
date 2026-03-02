import time

import requests
import helpers
from helpers import utils

HOST = "https://api.artifactsmmo.com"

log = helpers.setup_logger(
    "CHARACTER", helpers.config.LOG_PATH, helpers.config.LOG_LEVEL
)


class Character:
    def __init__(self, name: str) -> None:
        self.name = name
        self.header = {"Authorization": f"Bearer {helpers.config.AUTH}"}

        raw_character = requests.get(f"{HOST}/characters/{name}").json()
        if raw_character.get("error"):
            log.error(f"Ошибка при загрузки персонажа {name}: {raw_character['error']}")
            return None
        self.params = raw_character.get("data", {})

    def action(self, url: str, body: dict | list | None = None) -> dict:
        base_url = f"{HOST}/my/{self.name}/action{url}"
        response = requests.post(base_url, headers=self.header, json=body)

        if response.status_code == 499:
            if self.params.get("cooldown_expiration"):
                time_sleep = utils.difference_time(
                    str(self.params.get("cooldown_expiration", ""))
                )
                log.debug(f"{self.name} в кулдауне на {time_sleep} сек.")
                time.sleep(time_sleep)
            response = requests.post(base_url, headers=self.header, json=body)
            if response.status_code == 499:
                time.sleep(5)
                response = requests.post(base_url, headers=self.header, json=body)
        data = response.json()

        if response.status_code != 200 or data.get("error"):
            error_data = data.get("error", {})
            code = error_data.get("code", data.get("code", 0))
            error = utils.localize_error(code)
            if error is None:
                message = error_data.get("message", data.get("message", ""))
                error = f"{code} {message}".strip()
            log.warning(f"{self.name} {code} {error}")
            return {"error": code}

        return data.get("data", {})

    def move(self, map_id: int) -> None | int:
        body = {"map_id": map_id}
        data = self.action("/move", body)
        if data.get("error") is None:
            log.debug(f"{self.name} переместился на {map_id}")
            self.params = data.get("character", {})
            return
        return int(data.get("error", 0))

    def gathering(self) -> None | int:
        data = self.action("/gathering")
        if data.get("error") is None:
            log.debug(f"{self.name} добыл ресурс")
            self.params = data.get("character", {})
            return
        return int(data.get("error", 0))

    def bank(self, code: str, quantity: int = 1, action: str = "deposit") -> None:
        """
        :param code: Код предмета. Если указать gold, будет работа с золотом. all, все предметы (только с deposit)
        :param quantity: Количество передаваемых предметов. 0 - всё количество предмета
        :param action: Положить или взять с банка (deposit, withdraw)
        """
        if action not in ["deposit", "withdraw"]:
            log.error(f"Неверное действие для банка: {action}")
            return
        type_item = "item"
        if code == "gold":
            if quantity == 0:
                body = {quantity: self.params.get("gold", 0)}
            else:
                body = {"quantity": quantity}
            type_item = "gold"
        elif quantity == 0 and code == "all" and action == "deposit":
            inventory = self.params.get("inventory", [])
            body = []
            for item in inventory:
                if item.get("code"):
                    body.append(
                        {
                            "code": item.get("code"),
                            "quantity": item.get("quantity", 0),
                        }
                    )
        elif quantity == 0 or code == "all" and action == "withdraw":
            log.error("Невозможно взять всё из банка")
            return
        else:
            body = [{"code": code, "quantity": quantity}]
        data = self.action(f"/bank/{action}/{type_item}", body)
        if data is not None:
            log.debug(f"{self.name} использовал банк ({quantity} {code} {action})")
            self.params = data.get("character", {})

    def craft(self, code: str, quantity: int = 1) -> None:
        body = {"code": code, "quantity": quantity}
        data = self.action("/crafting", body)
        if data is not None:
            log.debug(f"{self.name} создал {quantity} {code}")
            self.params = data.get("character", {})


def create_character(name: str, skin: str = "men1") -> Character | None:
    url = f"{HOST}/characters/create"
    headers = {"Authorization": f"Bearer {helpers.config.AUTH}"}
    body = {"name": name, "skin": skin}
    response = requests.post(url, headers=headers, json=body)

    if response.status_code != 200:
        error = utils.localize_error(str(response.status_code))
        log.error(f"Ошибка при создании персонажа {name}: {error}")
        return None

    log.debug(f"Персонаж {name} успешно создан")
    return Character(name)
