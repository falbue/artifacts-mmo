from .utils.request import request_mmo as request


class Character:
    def __init__(self, name: str, token: str):
        self.name = name
        self.token = token
        if self.token is None or self.token == "":
            raise ValueError("Токен не задан")

    def move(self, x=None, y=None, map_id=None):
        if map_id is not None:
            body = {"map_id": map_id}
        else:
            body = {"x": x, "y": y}
        return request(f"/my/{self.name}/action/move", body=body, TOKEN=self.token)

    def gathering(self):
        return request(f"/my/{self.name}/action/gathering", TOKEN=self.token, body=True)

    def rest(self):
        return request(f"/my/{self.name}/action/rest", TOKEN=self.token, body=True)

    def fight(self):
        return request(f"/my/{self.name}/action/fight", TOKEN=self.token, body=True)
