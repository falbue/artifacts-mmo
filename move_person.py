# БИБЛИОТЕКИ----------------------------
import requests
import json
from http_status import http_status

# ПЕРМЕННЫЕ----------------------------
# конфиг
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
HEADERS = config['headers']
URL = config['url']

# переменные скрипта
PLAYER = "Falbue" # имя персонажа


# Тело запроса
data = {
    "x": 1,
    "y": 1
}

# Выполнение запроса
response = requests.post(f"{URL}/my/{PLAYER}/action/move", headers=HEADERS, json=data)

# Обработка ответа
if response.status_code == 200:
    print("Персонаж успешно переместился!")
else:
    http_status(response.status_code)
