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
        self.cooldown = {"seconds": 0, "expiration": ""}

    def action(self, url: str, body: dict | None = None) -> dict | None:
        if self.cooldown.get("seconds", 0) == 0:
            self.cooldown = self.check_cooldown()
        base_url = f"{HOST}/my/{self.name}/action{url}"
        response = requests.post(base_url, headers=self.header, json=body)

        if response.status_code == 499:
            time_sleep = utils.difference_time(str(self.cooldown.get("expiration", "")))
            log.debug(f"{self.name} в кулдауне на {time_sleep} сек.")
            time.sleep(time_sleep)
            response = requests.post(base_url, headers=self.header, json=body)
        data = response.json()

        if response.status_code != 200 or data.get("error"):
            error_data = data.get("error", {})
            code = error_data.get("code", data.get("code", 0))
            error = utils.localize_error(code)
            if error is None:
                message = error_data.get("message", data.get("message", ""))
                error = f"{code} {message}".strip()
            log.warning(error)
            return None

        return data.get("data", {})

    def move(self, map_id) -> dict[str, int | str] | None:
        body = {"map_id": map_id}
        data = self.action("/move", body)
        if data is None:
            return
        log.debug(f"{self.name} переместился на {map_id}")
        if data.get("cooldown"):
            cooldown = {
                "seconds": data["cooldown"].get("total_seconds", 0),
                "expiration": data["cooldown"].get("expiration", ""),
            }
            self.cooldown = cooldown
        return self.cooldown

    def gathering(self) -> dict[str, int | str] | None:
        data = self.action("/gathering")
        if data is None:
            return
        log.debug(f"{self.name} приступил к добыче ресурса")
        if data.get("cooldown"):
            cooldown = {
                "seconds": data["cooldown"].get("total_seconds", 0),
                "expiration": data["cooldown"].get("expiration", ""),
            }
            self.cooldown = cooldown
        return self.cooldown

    def check_cooldown(self) -> dict[str, int | str]:
        response = requests.get(f"{HOST}/my/characters", headers=self.header)
        data = response.json()
        if response.status_code == 200:
            data = data.get("data", [])
            for char in data:
                if char.get("name") == self.name:
                    self.cooldown = {
                        "seconds": char.get("cooldown", 0),
                        "expiration": char.get("cooldown_expiration", ""),
                    }
                    return self.cooldown

        else:
            error_data = data.get("error", {})
            code = error_data.get("code", data.get("code", 0))
            error = utils.localize_error(code)
            if error is None:
                message = error_data.get("message", data.get("message", ""))
                error = f"{code} {message}".strip()
            log.warning(error)
        return {"seconds": 0, "expiration": ""}
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
