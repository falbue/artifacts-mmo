import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from helpers import setup_logger
from helpers.config import config

PATH = Path(__file__).parent / "localization" / "errors.json"

log = setup_logger("UTILS", config.LOG_PATH, config.LOG_LEVEL)


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
    data = requests.get("https://api.artifactsmmo.com/").json().get("data", {})

    if not data:
        log.warning("Не удалось получить данные с сервера для синхронизации времени")
        return 0.0

    server_time_raw = data.get("server_time")
    if not server_time_raw:
        log.warning("Не удалось получить время сервера")
        return 0.0

    try:
        server_dt = datetime.fromisoformat(server_time_raw.replace("Z", "+00:00"))
    except ValueError:
        log.warning(f"Некорректный формат времени сервера: {server_time_raw}")
        return 0.0

    local_dt = datetime.fromtimestamp(local_time(), tz=timezone.utc)
    time_diff = round((server_dt - local_dt).total_seconds(), 2)

    log.debug("Синхронизация времени завершена")
    return time_diff


def difference_time(time1: str, time2: str | None = None) -> float:
    """
    Вычисляет разницу во времени между сервером и локальным временем

    :param time1: Время сервера в формате ISO 8601
    :param time2: Локальное время в формате ISO 8601. Если не указано, используется текущее локальное время
    :return: Разница во времени в секундах
    """
    if time2 is None:
        local = datetime.fromtimestamp(local_time(), tz=timezone.utc)
    else:
        local = datetime.fromisoformat(time2.replace("Z", "+00:00"))
    server = datetime.fromisoformat(time1.replace("Z", "+00:00"))
    time_diff = round((server - local).total_seconds(), 2)
    if time_diff < 0:
        return 0
    return time_diff
