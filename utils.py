import json
import os
import logger
from datetime import datetime, timedelta
import time
import threading

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

def load_file(filename):
    filepath = os.path.join('data', filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def print_mmo(data):
    if isinstance(data, (dict, list)):
        print( json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print( str(data))



def find_resource(resource_code):
    maps = load_file("maps.json")
    items = load_file("items.json")

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


def character_cooldown(server_time_str):
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