# БИБЛИОТЕКИ----------------------------
import requests
import json

# ПЕРЕМЕННЫЕ----------------------------
# конфиг
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

TOKEN = config['token']
HEADERS = config['headers']
URL = config['url']

x = 1
y = 1

# переменные скрипта
PLAYER = "Falbue" # имя персонажа

# Выполнение запроса
response = requests.get(f"{URL}/maps/{x}/{y}", headers=HEADERS)

# Получение данных
data = response.json()

# Преобразование данных в читаемый формат на русском языке
readable_data = {
    "данные": {
        "название": data['data']['name'],
        "скин": data['data']['skin'],
        "координаты": {
            "x": data['data']['x'],
            "y": data['data']['y']
        },
        "содержимое": {
            "тип": data['data']['content']['type'],
            "код": data['data']['content']['code']
        }
    }
}

# Функция для красивого вывода без отступов
def pretty_print(data):
    def print_dict(d):
        for key, value in d.items():
            if isinstance(value, dict):
                print(f"{key}:")
                print_dict(value)
            else:
                print(f"{key}: {value}")
    
    print_dict(data)

# Вывод данных в красивом виде
pretty_print(readable_data)
