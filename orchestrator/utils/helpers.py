import json
from datetime import datetime, timezone
from pathlib import Path

from orchestrator.utils import config
from orchestrator.utils.logger import setup_logger

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


def print_json(data: dict):
    print(json.dumps(data, indent=2))
