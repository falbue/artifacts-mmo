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
