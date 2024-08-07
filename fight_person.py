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

# Выполнение запроса
response = requests.post(f"https://api.artifactsmmo.com/my/{character_name}/action/fight", headers=headers)

# Обработка ответа
if response.status_code == 200:
    print("Враг побежден!")
else:
    print(f"Ошибка: {response.status_code}")
    print(response.text)
