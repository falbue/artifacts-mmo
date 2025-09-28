import requests
import json
import time

from .. import config
from . import logger
from . import utils

logger = logger.setup(config.DEBUG, "REQUESTS", config.LOG_PATH)

TOKEN = config.TOKEN

def process_command(command_body, body):
    command_body = command_body.replace("'", '"')
    command_elements = command_body.split(",")
    body_elements = body.split(",")
    if len(command_elements) != len(body_elements):
        return
    try:
        body_dict = json.loads(command_body)
    except Exception as e:
        return
    for i, key in enumerate(body_dict.keys()):
        if i < len(body_elements):
            body_dict[key] = body_elements[i].strip()
        else:
            break
    
    return body_dict
    

def request_mmo(command="", body=None):
    if command.startswith('/'):
        command = command[1:]

    base_command = command.split("/")
    if base_command[0] == "my":
        name = base_command[1]
        if name not in ["characters", "bank"]:
            data = request_mmo(f"/characters/{name}")
            cooldown = utils.check_cooldown(data["data"]["cooldown_expiration"])
            if cooldown > 0:
                logger.debug(f"{name} в кулдауне на {cooldown} сек.")
                time.sleep(cooldown)

            if base_command[2] == 'action' and base_command[3] == "move" and len(body) > 1 and isinstance(body, list):
                character = data['data']
                body = utils.nearest_object(body, {"x":character["x"],"y":character["y"]})


    if body:
        if body == True:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"})
        else:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"}, json=body)
    else:
        response = requests.get(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"})

    data = response.json()
    error_int = 0
    if data.get('error'):
        with open(utils.error_path, 'r', encoding='utf-8') as file:
            errors = json.load(file)
            error_int = response.status_code
            error = errors.get(f"{response.status_code}")
            if error is None:
                error = f"Неизвестная ошибка: {response.status_code}"
        if error_int  in [490, 499, 485]:
            logger.error(f"{error} {command}")
        else:
            error_message = f"{error_int} {error} {command} {body}"
            logger.error(error_message)
            raise Exception(error_message)
        data = error_int
    return data

utils.set_server_time_offset(request_mmo()["data"]["server_time"])