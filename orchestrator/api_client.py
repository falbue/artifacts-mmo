import aiohttp

from orchestrator.utils import config, setup_logger

log = setup_logger("API", config.LOG_PATH, config.LOG_LEVEL)


class APIClient:
    """Генерический асинхронный HTTP-клиент. Поддерживает любой OpenAPI."""

    def __init__(self):
        self.base_url = config.URL.rstrip("/")
        self.token = config.TOKEN
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    async def __aenter__(self):
        """Инициализация сессии"""
        return self

    async def __aexit__(self, *args):
        """Закрытие сессии"""
        if self.session:
            await self.session.close()

    async def get(self, endpoint: str, params: dict = {}) -> dict:
        """GET запрос.

        Args:
            endpoint: путь (например "/my/character_name")
            params: query параметры (опционально)

        Returns:
            JSON ответ сервера
        """
        assert self.session is not None

        url = f"{self.base_url}{endpoint}"
        async with self.session.get(url, headers=self.headers, params=params) as resp:
            return await self._handle_response(resp, endpoint, "GET")

    async def post(self, endpoint: str, body: dict = {}) -> dict:
        """POST запрос.

        Args:
            endpoint: путь (например "/my/character_name/action/move")
            body: JSON body (опционально)

        Returns:
            JSON ответ сервера
        """
        assert self.session is not None

        url = f"{self.base_url}{endpoint}"
        async with self.session.post(url, json=body, headers=self.headers) as resp:
            return await self._handle_response(resp, endpoint, "POST", body)

    async def _handle_response(
        self,
        resp: aiohttp.ClientResponse,
        endpoint: str,
        method: str,
        body: dict = {},
    ) -> dict:
        """Обработать HTTP ответ и логировать."""

        # Всегда прочитаем JSON
        try:
            data = await resp.json()
        except Exception as e:
            log.error(f"[API] Failed to parse JSON response: {e}")
            data = {}
            raise APIError(resp.status, f"Invalid JSON response: {e}")

        # Обработать статус коды
        if resp.status >= 500:
            log.error(f"[API] {method} {endpoint} -> {resp.status} SERVER ERROR")
            raise APIError(resp.status, f"Server error {resp.status}")

        if resp.status >= 400:
            message = data.get("message", data.get("error", f"HTTP {resp.status}"))
            log.warning(f"[API] {method} {endpoint} -> {resp.status}: {message}")
            if body:
                log.debug(f"  Request body: {body}")
            raise APIError(resp.status, message)

        log.debug(f"[API] {method} {endpoint} -> {resp.status} OK")
        return data


class APIError(Exception):
    """Исключение при ошибке API."""

    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API {status_code}: {message}")
