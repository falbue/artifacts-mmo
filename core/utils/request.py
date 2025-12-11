import requests
import json


def request_mmo(
    command="", body: bool | dict | None = None, TOKEN="", localize="ru"
) -> dict:
    """ "Отправляет запрос к API Artifacts MMO и возвращает ответ в виде словаря"""
    if command.startswith("/"):
        command = command[1:]

    if body:
        if body is True:
            response = requests.post(
                f"https://api.artifactsmmo.com/{command}",
                headers={"Authorization": f"Bearer {TOKEN}"},
            )
        else:
            response = requests.post(
                f"https://api.artifactsmmo.com/{command}",
                headers={"Authorization": f"Bearer {TOKEN}"},
                json=body,
            )
    else:
        response = requests.get(
            f"https://api.artifactsmmo.com/{command}",
            headers={"Authorization": f"Bearer {TOKEN}"},
        )

    data = response.json()
    if data.get("error"):
        error_code = response.status_code

        with open(
            f"core/utils/localize/{localize}/error.json", "r", encoding="utf-8"
        ) as file:
            errors = json.load(file)
        error_message = errors.get(f"{response.status_code}") or data["error"]
        return {"error": {"code": error_code, "message": error_message}}
    return data
