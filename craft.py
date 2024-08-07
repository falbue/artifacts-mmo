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

# Выполнение запроса
response = requests.post(f"{URL}/my/{PLAYER}/action/crafting", headers=HEADERS)

# Обработка ответа
if response.status_code == 200:
    print("Создан предмет!")
else:
    print(f"Ошибка: {response.status_code}")

    print(response.text)
