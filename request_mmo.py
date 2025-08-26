import requests
import json
import os
import re
import time

import os
from dotenv import load_dotenv
import logger

logger = logger.setup(True)

load_dotenv()

TOKEN = os.getenv("TOKEN")

package_dir = os.path.dirname(os.path.abspath(__file__))
localize_path = os.path.join(package_dir, "localize_ru.json")
error_path = os.path.join(package_dir, "errors_ru.json")

def translate_data(data):
    with open(localize_path, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    if isinstance(data, list):
        return [translate_data(item) for item in data]
    elif isinstance(data, dict):
        return {translations.get(k, k): translate_data(v) for k, v in data.items()}
    else:
        return data

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
    

def request_mmo(command="", body=None, cooldown=None):
    if (type(cooldown) in (int, float)) and cooldown > 0:
        logger.debug(f"Ожидание завершения кулдауна. Осталось: {cooldown} сек")
        time.sleep(cooldown)
    if command.startswith('/'):
        command = command[1:]
    if body:
        if body == True:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"})
        else:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"}, json=body)
    else:
        response = requests.get(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {TOKEN}"})

    data = response.json()
    data = translate_data(data)
    error_int = 0
    if data.get('error'):
        with open(error_path, 'r', encoding='utf-8') as file:
            errors = json.load(file)
            error_int = response.status_code
            error = errors.get(f"{response.status_code}")
            if error is None:
                error = f"Неизвестная ошибка: {response.status_code}"
        if error_int  in [490, 499]:
            logger.debug(f"{error} {command}")
        else:
            logger.error(f"{error_int} {error} {command} {body}")
        data = error_int
    if cooldown == True:
        if error_int == 490:
            return 0
        if error_int == 499:
            return 60
        if isinstance(data, dict):
            return int(data["data"]["Кулдаун"]["remaining_seconds"])
        else:
            return 0
    return data