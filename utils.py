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

def find_objects(data, target_code):
    results = []
    
    for item in data:
        if (item.get("Контент") and 
            isinstance(item["Контент"], dict) and 
            item["Контент"].get("Код") == target_code):
            
            x = item.get("x")
            y = item.get("y")
            
            if x is not None and y is not None:
                results.append({"x": x, "y": y})
    
    if not results:
        return None
    elif len(results) == 1:
        return results[0]
    else:
        return results