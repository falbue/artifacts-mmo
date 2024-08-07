import requests
import json

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
response = requests.post(f"{URL}/my/{PLAYER}/action/recycling ", headers=HEADERS)

# Обработка ответа
if response.status_code == 200:
    print("Получен предмет!")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
