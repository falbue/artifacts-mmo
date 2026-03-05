import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from helpers import setup_logger
from helpers.config import config

PATH = Path(__file__).parent / "localization" / "errors.json"
HOST = "https://api.artifactsmmo.com"

log = setup_logger("UTILS", config.LOG_PATH, config.LOG_LEVEL)

TIME_DIFF = 0.0


def _parse_iso_utc(raw_value: str) -> datetime:
    dt = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def localize_error(code: str) -> str | None:
    with open(PATH, "r", encoding="utf-8") as f:
        errors = json.load(f)
        error = errors.get(str(code), None)
    if error is None:
        log.warning(f"Неизвестный код ошибки: {code}")
    return error


def local_time() -> float:
    return datetime.now(timezone.utc).timestamp()


def synchronize_time() -> float:
    global TIME_DIFF
    data = requests.get(f"{HOST}/").json().get("data", {})

    if not data:
        log.warning("Не удалось получить данные с сервера для синхронизации времени")
        return 0.0

    server_time_raw = data.get("server_time")
    if not server_time_raw:
        log.warning("Не удалось получить время сервера")
        return 0.0

    try:
        server_dt = _parse_iso_utc(server_time_raw)
    except ValueError:
        log.warning(f"Некорректный формат времени сервера: {server_time_raw}")
        return 0.0

    local_dt = datetime.fromtimestamp(local_time(), tz=timezone.utc)
    time_diff = round((server_dt - local_dt).total_seconds(), 2)
    TIME_DIFF = time_diff
    log.info(f"Синхронизация времени завершена. Разница: {TIME_DIFF} секунд")
    return max(0.0, round(time_diff, 2))


synchronize_time()


def difference_time(time1: str, time2: str | None = None) -> float:
    """
    Вычисляет разницу во времени между сервером и локальным временем

    :param time1: Время сервера в формате ISO 8601
    :param time2: Локальное время в формате ISO 8601. Если не указано, используется текущее локальное время
    :return: Разница во времени в секундах
    """
    try:
        if time2 is None:
            local = datetime.fromtimestamp(local_time(), tz=timezone.utc)
        else:
            local = _parse_iso_utc(time2)
        server = _parse_iso_utc(time1)
    except ValueError as e:
        log.warning(f"Ошибка формата времени: {e}")
        return 0.0
    result = max(0.0, round((server - local).total_seconds(), 2))
    return result - TIME_DIFF


def find_map(
    content_code: str,
    page: int = 1,
    size: int = 50,
) -> list | None:
    url = f"{HOST}/maps?content_code={content_code}&page={page}&size={size}"
    response = requests.get(url)
    if response.status_code != 200:
        error = localize_error(str(response.status_code))
        log.warning(f"{response.status_code} {error}")
        return None
    data = response.json().get("data", [])
    if not data:
        log.warning(f"Карты с контентом {content_code} не найдены")
        return None
    return data


def find_nearest_map(player_data: dict, maps: list) -> int | None:
    """
    Поиск ближайшей карты из списка к текущему положению игрока

    :param player_data: Данные персонажа с координатами 'x' и 'y'
    :param maps: Список карт с полями 'map_id', 'x', и 'y'
    :return: map_id ближайшей карты или None, если список карт пуст
    """
    if not maps:
        return None

    player_x = player_data.get("x", 0)
    player_y = player_data.get("y", 0)

    nearest_map = min(
        maps, key=lambda m: (m["x"] - player_x) ** 2 + (m["y"] - player_y) ** 2
    )

    return nearest_map["map_id"]


def find_item(code: str):
    url = f"{HOST}/items/{code}"
    response = requests.get(url)
    if response.status_code != 200:
        error = localize_error(str(response.status_code))
        log.warning(f"{response.status_code} {error}")
        return {}
    data = response.json().get("data", {})
    if not data:
        log.warning(f"Предмет с кодом {code} не найден")
        return None
    return data


def calc_items(data: list) -> int:
    total = 0
    for item in data:
        total += item.get("quantity", 0)
    return total


def dict_quantity_items(data: list) -> dict:
    items = {}
    for item in data:
        items[item["code"]] = item["quantity"]
    return items


def check_bank_item(code: str) -> int | None:
    url = f"{HOST}/my/bank/items?item_code={code}"
    headers = {"Authorization": f"Bearer {config.AUTH}"}
    response = requests.get(url, headers=headers).json()
    data = response.get("data", [])
    if data:
        item = data[0]
        return item.get("quantity", 0)
    return None


def bank_item(size: int = 50) -> list:
    url = f"{HOST}/my/bank/items?size={size}"
    headers = {"Authorization": f"Bearer {config.AUTH}"}
    response = requests.get(url, headers=headers).json()
    data = response.get("data", [])
    return data


def find_drop_code(code: str):
    resource_url = f"{HOST}/resources?drop={code}"
    monsters_url = f"{HOST}/monsters?drop={code}"
    data = []
    resource_res = requests.get(resource_url).json()
    monster_res = requests.get(monsters_url).json()
    if resource_res.get("data"):
        data.extend(resource_res["data"])
    if monster_res.get("data"):
        data.extend(monster_res["data"])

    max_rate = 0
    return_data = None
    for item in data:
        for drop in item.get("drops", []):
            if drop.get("code") == code:
                if drop.get("rate", 0) > max_rate:
                    max_rate = drop.get("rate", 0)
                    return_data = item.get("code")

    return return_data
