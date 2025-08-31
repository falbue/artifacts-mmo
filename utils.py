import json
import os
import logger
from datetime import datetime, timedelta
import time
import threading
from datetime import datetime, timezone

logger = logger.setup(True)

def save_file(filename, data):
    try:
        if not filename.lower().endswith('.json'):
            logger.error(f"Ошибка: Файл {filename} не является JSON файлом")
            return False

        if not os.path.exists('data'):
            os.makedirs('data')
            logger.info("Создана папка 'data'")

        filepath = os.path.join('data', filename)

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        
        logger.info(f"Файл {filename} успешно сохранен в папку data")
        return True
        
    except Exception as e:
        logger.error(f"Ошибка при сохранении файла: {e}")
        return False

def load_file(filename, all_data=False):
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            if all_data == True:
                return json.load(f)
            elif all_data == False:
                return json.load(f)["data"]
    return None

def print_mmo(data):
    if isinstance(data, (dict, list)):
        print( json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print( str(data))



def find_resource(resource_code):
    items = load_file("items.json")

    target_item = None
    for item in items:
        if item["Код"] == resource_code:
            target_item = item
            break

    if not target_item:
        return None

    if target_item["Тип"] != "resource":
        return None

    skill_type = target_item["Подтип"]
    target_resource_codes = []

    if skill_type == "mob":
        monsters = load_file("monsters.json")
        for resource in monsters:
            for drop in resource["drops"]:
                if drop["Код"] == resource_code:
                    target_resource_codes.append(resource["Код"])
                    break 
    else:
        resources = load_file("resources.json")
        for resource in resources:
            if resource["skill"] == skill_type:
                for drop in resource["drops"]:
                    if drop["Код"] == resource_code:
                        target_resource_codes.append(resource["Код"])
                        break

    return skill_type, find_map_object(target_resource_codes)

def find_map_object(resource_code):
    maps = load_file("maps.json")
    coordinates = []
    for map_obj in maps:
        content = map_obj.get("Контент", {})
        if content:
            if content.get("Код") in resource_code:
                coordinates.append({"x": map_obj["x"], "y": map_obj["y"]})
    
    if len(coordinates) == 1:
        coordinates = coordinates[0]
    return coordinates


def nearest_object(object_coordinates, character_coordinates):
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


def check_cooldown(server_time_str):
    try:
        server_time = datetime.fromisoformat(server_time_str.replace('Z', '+00:00'))
        current_time = datetime.now(timezone.utc)

        time_difference = (server_time - current_time).total_seconds()
        
        if time_difference > 0:
            return int(time_difference)
        else:
            return 0
            
    except (ValueError, TypeError) as e:
        logger.error(f"Ошибка при обработке времени: {e}")
        return 0


def find_character(data, character_name):
    for character in data['data']:
        if character['Имя'] == character_name:
            return character
    return None

def find_item_inventory(item, inventory):
    item_inventory_found = False
    for inventory_item in inventory:
        if inventory_item["Код"] == item:
            item_inventory_found = True
            break
    if not item_inventory_found:
        logger.warning(f"{item} не найден в инвентаре")
        return None
    return inventory_item["Количество"]