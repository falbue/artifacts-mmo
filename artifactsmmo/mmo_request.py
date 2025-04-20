import requests
import json
import os
import re

package_dir = os.path.dirname(os.path.abspath(__file__))
commands_path = os.path.join(package_dir, "commands.json")
localize_path = os.path.join(package_dir, "localize_ru.json")
error_path = os.path.join(package_dir, "errors_ru.json")

def translate_data(data):
    with open(localize_path, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    
    if isinstance(data, list):
        return [translate_data(item) for item in data]
    elif isinstance(data, dict):
        translated_dict = {}
        for k, v in data.items():
            # Переводим ключ
            translated_key = translations['key'].get(k, k)
            # Переводим значение, если оно строка
            if isinstance(v, str):
                translated_value = translations['value'].get(v, v)
                translated_dict[translated_key] = translated_value
            else:
                translated_dict[translated_key] = translate_data(v)
        return translated_dict
    elif isinstance(data, str):
        # Переводим строковые значения, которые не являются ключами
        return translations['value'].get(data, data)
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
    

def mmo_request(mmo_request="", character=None, command=None, token="", body=None):
    if body:
        if body == True:
            response = requests.post(f"https://api.artifactsmmo.com{mmo_request}", headers={"Authorization": f"Bearer {token}"})
        else:
            response = requests.post(f"https://api.artifactsmmo.com{mmo_request}", headers={"Authorization": f"Bearer {token}"}, json=body)
    else:
        response = requests.get(f"https://api.artifactsmmo.com{mmo_request}", headers={"Authorization": f"Bearer {token}"})

    data = response.json()
    if data.get('error'):
        with open(error_path, 'r', encoding='utf-8') as file:
            errors = json.load(file)
            data = errors.get(f"{response.status_code}")
            if data is None:
                data = response.json()
    data = translate_data(data)
    return data