import json
import os
from datetime import datetime, timedelta
import time
import threading
from datetime import datetime, timezone
from pathlib import Path

from .. import config
from . import logger

logger = logger.setup(config.DEBUG, "UTILS", config.LOG_PATH)

current_dir = Path(__file__).parent.parent
localize_path = current_dir / "localize" / config.LOCALIZE / "localize_key.json"
error_path = current_dir / "localize" / config.LOCALIZE / "errors.json"

ARTIFACTS_DATA = config.ARTIFACTS_DATA
_time_offset = None

def translate_data(data): # перевод из указанного файла
    with open(localize_path, 'r', encoding='utf-8') as file:
        translations = json.load(file)
    if isinstance(data, list):
        return [translate_data(item) for item in data]
    elif isinstance(data, dict):
        return {translations.get(k, k): translate_data(v) for k, v in data.items()}
    else:
        return data

def save_file(filename, data): # сохранение файла
    try:
        if not filename.lower().endswith('.json'):
            logger.error(f"Ошибка: Файл {filename} не является JSON файлом")
            return False

        if not os.path.exists(ARTIFACTS_DATA):
            os.makedirs(ARTIFACTS_DATA)
            logger.info("Создана папка 'data'")

        filepath = os.path.join(ARTIFACTS_DATA, filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        logger.info(f"Файл {filename} успешно сохранен в папку data")
        return True
        
    except Exception as e:
        logger.error(f"Ошибка при сохранении файла: {e}")
        return False

def load_file(filename, all_data=False): # загрузка файла
    filepath = os.path.join(ARTIFACTS_DATA, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            if all_data == True:
                return json.load(f)
            elif all_data == False:
                return json.load(f)["data"]
    return None

def print_mmo(data, localize="en"): # удобный вывод json
    if isinstance(data, (dict, list)):
        text = ( json.dumps(data, indent=4, ensure_ascii=False))
    else:
        text = ( str(data))

    if localize == "en":
        print(text)
    elif localize == "ru":
        print(translate_data(text))



def find_resource(resource_code): # поиск нужного ресурса из файла
    items = load_file("items.json")

    target_item = None
    for item in items:
        if item["code"] == resource_code:
            target_item = item
            break

    if not target_item:
        return None

    if target_item["type"] != "resource":
        return None

    skill_type = target_item["subtype"]
    target_resource_codes = []

    if skill_type == "mob":
        monsters = load_file("monsters.json")
        for resource in monsters:
            for drop in resource["drops"]:
                if drop["code"] == resource_code:
                    target_resource_codes.append(resource["code"])
                    break 
    else:
        resources = load_file("resources.json")
        for resource in resources:
            if resource["skill"] == skill_type:
                for drop in resource["drops"]:
                    if drop["code"] == resource_code:
                        target_resource_codes.append(resource["code"])
                        break

    return skill_type, find_map_object(target_resource_codes)

def find_map_object(resource_code): # поиск нужного объекта на карте
    maps = load_file("maps.json")
    coordinates = []
    for map_obj in maps:
        content = map_obj.get("content", {})
        if content:
            if content.get("code") in resource_code:
                coordinates.append({"x": map_obj["x"], "y": map_obj["y"]})
    
    if len(coordinates) == 1:
        coordinates = coordinates[0]
    return coordinates


def nearest_object(object_coordinates, character_coordinates): # поиск ближайщего объекта
    if not object_coordinates:
        return None
    
    min_squared_distance = float('inf')
    nearest_obj = None
    
    for obj in object_coordinates:
        # Вычисляем квадрат расстояния (быстрее, чем евклидово расстояние)
        dx = obj['x'] - character_coordinates['x']
        dy = obj['y'] - character_coordinates['y']
        squared_distance = dx*dx + dy*dy
        
        if squared_distance < min_squared_distance:
            min_squared_distance = squared_distance
            nearest_obj = obj
    
    return nearest_obj


def set_server_time_offset(server_time_str): # Устанавливает смещение времени на основе серверного времени.
    global _time_offset
    try:
        server_time = datetime.fromisoformat(server_time_str.replace('Z', '+00:00'))
        local_time_at_request = datetime.now(timezone.utc)
        _time_offset = server_time - local_time_at_request
    except (ValueError, TypeError) as e:
        print(f"Ошибка при установке смещения времени: {e}")
        _time_offset = None


def get_corrected_current_time(): # Возвращает текущее время, скорректированное по серверному.
    if _time_offset is None:
        raise RuntimeError("Смещение времени не установлено. Вызовите set_server_time_offset() сначала.")
    
    return datetime.now(timezone.utc) + _time_offset


def check_cooldown(server_time_str): # Проверяет кулдаун, используя серверное время и коррекцию.
    try:
        server_time = datetime.fromisoformat(server_time_str.replace('Z', '+00:00'))
        corrected_current_time = get_corrected_current_time()

        time_difference = (server_time - corrected_current_time).total_seconds()

        if time_difference > 0:
            return int(time_difference)
        else:
            return 0

    except (ValueError, TypeError) as e:
        print(f"Ошибка при обработке времени: {e}")
        return 0


def find_character(data, character_name): # Поиск персонажа
    for character in data['data']:
        if character['name'] == character_name:
            return character
    return None

def find_item_inventory(item, inventory): # Поиск предемета в указанном инвентаре
    item_inventory_found = False
    for inventory_item in inventory:
        if inventory_item["code"] == item:
            item_inventory_found = True
            break
    if not item_inventory_found:
        return 0
    return inventory_item["quantity"]

def check_craftable(crafting_item): # Проверка на крафт предмета
    items = load_file("items.json")
    for item in items:
        if item.get("code") == crafting_item:
            craftable = item.get("craft")
            if craftable:
                return True
    return False

def inventory_full(character): # Проверка, на заполненность инвентаря
    if character.get("character"):
        character = character["character"]
    max_items = character.get("inventory_max_items")
    inventory = character.get("inventory", [])
    total_items = 0
    for item in inventory:
        if item.get("code") and item.get("code") != "":
            total_items += item.get("quantity", 0)
    return total_items >= max_items