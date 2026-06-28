import aiohttp

from orchestrator.utils import config, setup_logger

log = setup_logger("API", config.LOG_PATH, config.LOG_LEVEL)


class APIClient:
    """Генерический асинхронный HTTP-клиент."""

    _instance = None  # Синглтон

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.base_url = config.URL.rstrip("/")
        self.token = config.TOKEN
        self.session: aiohttp.ClientSession | None = None
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }
        self._initialized = True

    async def init(self):
        """Инициализация сессии (вызывать один раз при старте)"""
        if not self.session:
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def close(self):
        """Закрытие сессии (вызывать один раз при завершении)"""
        if self.session:
            await self.session.close()
            self.session = None

    async def get(self, endpoint: str, params: dict | None = None):
        if not self.session:
            raise RuntimeError(
                "Клиент не инициализирован. Вызовите await client.init()"
            )
        url = f"{self.base_url}{endpoint}"
        async with self.session.get(url, params=params) as response:
            return {"status": response.status, "data": await response.json()}

    async def post(self, endpoint: str, data: dict | None = None):
        if not self.session:
            raise RuntimeError(
                "Клиент не инициализирован. Вызовите await client.init()"
            )
        url = f"{self.base_url}{endpoint}"
        async with self.session.post(url, json=data) as response:
            return {"status": response.status, "data": await response.json()}


client = APIClient()
