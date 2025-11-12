# Создание враппера
```bash
openapi-python-client generate --url https://api.artifactsmmo.com/openapi.json
```
# Примерная структура
artifacts-mmo/
│
├── artifacts_api_client/              # сгенерированный OpenAPI клиент
│
├── core/                          # основная логика игры
│   ├── __init__.py
│   ├── mining.py                  # логика добычи
│   ├── trading.py                 # обмен
│   ├── crafting.py                # крафт
│   ├── movement.py                # перемещение
│   ├── inventory.py               # инвентарь
│   └── character.py               # управление персонажем
│
├── memory/                        # система памяти
│   ├── __init__.py
│   ├── state_manager.py           # состояние персонажа
│   ├── db.py                      # хранение в SQLite или JSON
│   └── persistence.py             # сохранение/загрузка
│
├── ai/                            # логика ИИ (если будет)
│   └── decision_maker.py          # принятие решений
│
├── telegram_bot/                  # телеграм-бот
│   ├── __init__.py
│   ├── bot.py                     # основной бот
│   └── handlers.py                # обработчики команд
│
├── config/                        # настройки
│   └── settings.py
│
├── utils/                         # вспомогательные функции
│   └── helpers.py
│
├── main.py                        # точка входа для бота
└── requirements.txt

---
# Документация враппера
Библиотека клиента для доступа к Artifacts API

## Использование
Сначала создайте клиента:

```python
from artifacts_api_client import Client

client = Client(base_url="https://api.example.com")
```

Если для доступа к конечным точкам требуется аутентификация, используйте `AuthenticatedClient`:

```python
from artifacts_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Теперь вызовите свою конечную точку и используйте свои модели:

```python
from artifacts_api_client.models import MyDataModel
from artifacts_api_client.api.my_tag import get_my_data_model
from artifacts_api_client.types import Response

with client as client:
    my_data: MyDataModel = get_my_data_model.sync(client=client)
    # или если вам нужна дополнительная информация (например, status_code)
    response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Или выполните то же самое с асинхронной версией:

```python
from artifacts_api_client.models import MyDataModel
from artifacts_api_client.api.my_tag import get_my_data_model
from artifacts_api_client.types import Response

async with client as client:
    my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
    response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

По умолчанию при вызове HTTPS API будет выполнена попытка проверить, что SSL работает правильно. Использование проверки сертификатов настоятельно рекомендуется в большинстве случаев, но иногда вам может потребоваться аутентификация на сервере (особенно на внутреннем сервере) с использованием пользовательского пакета сертификатов.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

Вы также можете полностью отключить проверку сертификатов, но имейте в виду, что **это риск для безопасности**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Что нужно знать:
1. Каждая комбинация путь/метод становится модулем Python с четырьмя функциями:
    1. `sync`: Блокирующий запрос, возвращающий разобранные данные (если успешно) или `None`
    1. `sync_detailed`: Блокирующий запрос, всегда возвращающий `Request`, опционально с установленным `parsed`, если запрос был успешным.
    1. `asyncio`: Как `sync`, но асинхронный вместо блокирующего
    1. `asyncio_detailed`: Как `sync_detailed`, но асинхронный вместо блокирующего

1. Все параметры пути/запроса и тела становятся аргументами метода.
1. Если у вашей конечной точки были какие-либо теги, первый тег будет использоваться в качестве имени модуля для функции (my_tag выше)
1. Любая конечная точка, которая не имела тега, будет находиться в `artifacts_api_client.api.default`

## Расширенные настройки

В сгенерированном классе `Client` есть больше настроек, которые позволяют вам контролировать поведение во время выполнения, посмотрите строку документации для этого класса, чтобы получить больше информации. Вы также можете настроить базовый `httpx.Client` или `httpx.AsyncClient` (в зависимости от вашего случая использования):

```python
from artifacts_api_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Или получите базовый httpx клиент для прямого изменения с помощью client.get_httpx_client() или client.get_async_httpx_client()
```

Вы даже можете установить httpx клиент напрямую, но имейте в виду, что это переопределит все существующие настройки (например, base_url):

```python
import httpx
from artifacts_api_client import Client

client = Client(
    base_url="https://api.example.com",
)
# Обратите внимание, что base_url нужно установить заново, как и любые общие файлы cookie, заголовки и т.д.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## Сборка / публикация этого пакета
Этот проект использует [Poetry](https://python-poetry.org/) для управления зависимостями и пакетами. Вот основы:
1. Обновите метаданные в pyproject.toml (например, авторы, версия)
1. Если вы используете частный репозиторий, настройте его с помощью Poetry
    1. `poetry config repositories.<your-repository-name> <url-to-your-repository>`
    1. `poetry config http-basic.<your-repository-name> <username> <password>`
1. Опубликуйте клиент с помощью `poetry publish --build -r <your-repository-name>` или, если для публичного PyPI, просто `poetry publish --build`

Если вы хотите установить этот клиент в другой проект без публикации (например, для разработки), то:
1. Если этот проект **использует Poetry**, вы можете просто выполнить `poetry add <path-to-this-client>` из этого проекта
1. Если проект не использует Poetry:
    1. Создайте wheel с помощью `poetry build -f wheel`
    1. Установите этот wheel из другого проекта `pip install <path-to-wheel>`
```