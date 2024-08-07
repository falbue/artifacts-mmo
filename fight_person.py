import requests
import json

# ПЕРМЕННЫЕ----------------------------
# конфиг
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
HEADERS = config['headers']


# переменные скрипта
PLAYER = "Falbue" # имя персонажа

# Выполнение запроса
response = requests.post(f"https://api.artifactsmmo.com/my/{PLAYER}/action/fight", headers=HEADERS)

# Обработка ответа
if response.status_code == 200:
    print("Враг побежден!")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
