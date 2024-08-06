import requests

# Замените INSERT_TOKEN_HERE на ваш реальный токен
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IkZhbGJ1ZSIsInBhc3N3b3JkX2NoYW5nZWQiOiIifQ.rgxtPlIeKnAd3E7RKTdSTv60oLbVN5BqeOks8hmqxpk"
character_name = "Falbue"

# Заголовки запроса
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {token}"
}

# Тело запроса
data = {
    "x": 0,
    "y": 1
}

# Выполнение запроса
response = requests.post(f"https://api.artifactsmmo.com/my/{character_name}/action/move", headers=headers, json=data)

# Обработка ответа
if response.status_code == 200:
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
