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
    

def mmo_request(character=None, token="", command="", body=None):
    command_body = None
    if command != "":
        with open(commands_path, 'r', encoding='utf-8') as file:
            commands = json.load(file)
            command_text = commands.get(command)
            if command_text is None:
                command_text = command
            command_text_1 = command_text.split(":")[0]
            if len(command_text.split(":")) > 1:
                command_body = commands[command].replace(f"{command_text_1}:", "")
            format_dict = {"character": character}
            command = command_text_1.format_map({key: format_dict.get(key, None) for key in re.findall(r'\{(.*?)\}', command_text_1)})

    # print(command)

    if command_body:
        body = process_command(command_body, body)
        print(body)

    if body:
        if body == True:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {token}"})
        else:
            response = requests.post(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {token}"}, json=body)
    else:
        response = requests.get(f"https://api.artifactsmmo.com/{command}", headers={"Authorization": f"Bearer {token}"})

    data = response.json()
    if data.get('error'):
        with open(error_path, 'r', encoding='utf-8') as file:
            errors = json.load(file)
            data = errors.get(f"{response.status_code}")
            if data is None:
                data = response.json()
    data = translate_data(data)
    return data



# data = mmo_request(command='maps/2/0')  # получение инофрмации о карте
# // data = send_request('items')  # получение инофрмации о предметах
# // data = send_request('items/wooden_shield')  # получение инофрмации об указаном предмете
# // data = send_request(f'my/{name}/action/rest', True)  # лечение
# // data = send_request("my/Falbue/action/fight", True) # бой
# // data = send_request("my/Falbue/action/gathering", True) # добыча
# // data = send_request("my/Falbue/action/crafting", {'code':'ash_plank', "quantity": 1}) # крафт
# // data = send_request(f'my/{name}/action/equip', {"code": "copper_ring", "slot": "ring1", "quantity": 1})  # надеть предмет
# // data = send_request(f'my/{name}/action/equip', {"slot": "weapon", "quantity": 1})  # снять предмет
# // data = send_request(f'my/{name}/action/grandexchange/sell', {"code": "yellow_slimeball", "quantity": 60, "price": 100})  # Создать сделку