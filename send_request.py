import requests
import json
import os
from translate_data import *

config_data = {
        "url": "https://api.artifactsmmo.com",
        "headers": {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer token..."
        }
    }

def http_status(status_code):
    status_messages = {
        422: "Неверный формат данных",
        404: "Не найдено",
        500: "Фатальная ошибка",
        405: "Нужно изменить тип запроса на post. Введите в запрос body=True",

        452: "Не правильный токен",
        453: "Токен истек",
        454: "Токен отсутствует",
        455: "Ошибка генерации токена",
        456: "Имя пользователя уже занято",
        457: "Этот email уже используется",
        458: "Пароль не изменен (тот же пароль)",
        459: "Неверный текущий пароль",

        483: "Недостаточно здоровья у персонажа",
        484: "Максимум утилит уже установлен",
        485: "Этот предмет уже экипирован",
        486: "Персонаж заблокирован",
        474: "Персонаж не может выполнять эту задачу",
        475: "Слишком много предметов для задачи",
        487: "Персонаж не имеет задачи",
        488: "Задача не завершена",
        489: "Персонаж уже в задаче",
        490: "Персонаж уже в выбраном месте",
        491: "Ошибка слота экипировки персонажа",
        492: "Недостаточно золота у персонажа",
        493: "Персонаж не имеет необходимого уровня навыка",
        494: "Имя персонажа уже занято",
        495: "Максимальное количество персонажей достигнуто",
        496: "Персонаж не имеет необходимого уровня",
        497: "Инвентарь персонажа заполнен",
        498: "Персонаж не найден",
        499: "Персонаж в кулдауне",

        471: "Недостаточное количество предметов",
        472: "Предмет не подходит для экипировки",
        473: "Невозможно переработать предмет",
        476: "Предмет нельзя использовать",
        478: "Предмет отсутствует",

        479: "Максимальное количество предметов на обмен",
        480: "Предмет не в наличии",
        482: "Цена на обмен не соответствует",
        436: "Транзакция обмена уже в процессе",
        431: "Нет доступных ордеров",
        433: "Достигнут лимит ордеров",
        434: "Слишком много предметов для обмена",
        435: "Вы не можете обмениваться с этим аккаунтом",
        437: "Неверный предмет для обмена",
        438: "Вы не можете отменить чужой ордер",

        460: "Недостаточно золота в банке",
        461: "Транзакция с банком уже в процессе",
        462: "Банк заполнен",

        597: "Карта не найдена",
        598: "Контент на карте не найден",
    }
    
    # Получаем сообщение из словаря или используем стандартное сообщение
    message = status_messages.get(status_code, f"Неизвестный код состояния {status_code}")
    print(message)

def send_request(request=None, body=None): 
    if request is None:
        print("Введите запрос!")
        return   

    # Проверяем существует ли файл config.json
    if not os.path.exists('config.json'):
        print("Файл config.json не найден, создается новый.")
        with open('config.json', 'w') as config_file:
            json.dump(config_data, config_file, indent=4)

    # Загружаем конфигурацию из файла
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    if config['headers'] == config_data['headers']:
        print("Введите токен в файл config.json\nПолучить токен: https://artifactsmmo.com/account")
        return
    HEADERS = config['headers']
    URL = config['url']

    if body:
        response = requests.post(f"{URL}/{request}", headers=HEADERS, json=body)
    else:
        response = requests.get(f"{URL}/{request}", headers=HEADERS)

    if response.status_code == 200:
        data = response.json()
        data = data['data']
        data = translate_data(data)
        return data
    else:
        http_status(response.status_code)
        print(f"Отправленный запрос: {URL}/{request}")