import requests

def get_map(x, y):
    url = f"https://api.artifactsmmo.com/maps/{x}/{y}"
    headers = {
        'Accept': 'application/json'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяет наличие ошибок HTTP

        # Обрабатываем ответ в формате JSON
        map_data = response.json()
        return map_data

    except requests.exceptions.HTTPError as http_err:
        print(f"Произошла HTTP ошибка: {http_err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")

# Пример использования функции
x = 0  # Замените на нужное значение X
y = 0  # Замените на нужное значение Y

map_details = get_map(x, y)

if map_details:
    print("Детали карты успешно получены!")
    print(f"Название: {map_details['data']['name']}")
    print(f"Скин: {map_details['data']['skin']}")
    print(f"Позиция X: {map_details['data']['x']}")
    print(f"Позиция Y: {map_details['data']['y']}")
    
    # Проверяем наличие контента
    content = map_details['data'].get('content', None)
    if content:
        print(f"Тип контента: {content.get('type', 'Не указан')}")
        print(f"Код контента: {content.get('code', 'Не указан')}")
    else:
        print("Контент карты отсутствует.")
else:
    print("Не удалось получить детали карты.")
