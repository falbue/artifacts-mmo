from .utils.request import request_mmo as request
import functools


def update_character(func):
    """Декоратор для автоматического обновления данных персонажа после выполнения метода"""

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        data = func(self, *args, **kwargs)
        # Обновляем данные персонажа из ответа
        if isinstance(data, dict) and "character" in data:
            self.character = data["character"]
        return data

    return wrapper


class Character:
    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token
        if self.token is None or self.token == "":
            raise ValueError("Токен не задан")

        response = request(f"/my/{self.name}", TOKEN=self.token)
        if "error" in response:
            raise ValueError(f"Ошибка при получении персонажа: {response['error']}")

        data = response.get("data")
        if not data:
            raise ValueError(f"Персонаж с именем '{self.name}' не найден")

        for item in data:
            if item.get("name") == self.name:
                self.character = item

    def info(self):
        return self.character

    @update_character
    def move(self, x=None, y=None, map_id=None):
        if map_id is not None:
            body = {"map_id": map_id}
        else:
            body = {"x": x, "y": y}
        return request(f"/my/{self.name}/action/move", body=body, TOKEN=self.token)

    @update_character
    def gathering(self):
        return request(f"/my/{self.name}/action/gathering", TOKEN=self.token, body=True)

    @update_character
    def rest(self):
        return request(f"/my/{self.name}/action/rest", TOKEN=self.token, body=True)

    @update_character
    def fight(self):
        return request(f"/my/{self.name}/action/fight", TOKEN=self.token, body=True)
