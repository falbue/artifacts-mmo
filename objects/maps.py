import aiohttp
from helpers.utils import HOST, localize_error
from helpers import logger
from helpers import config

log = logger.setup_logger("MAPS", config.LOG_PATH, config.LOG_LEVEL)


async def find_map(
    content_code: str,
    page: int = 1,
    size: int = 50,
) -> list | None:
    url = f"{HOST}/maps?content_code={content_code}&page={page}&size={size}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                error = localize_error(str(response.status))
                log.warning(f"{response.status} {error}")
                return None
            data = await response.json()
    if not data.get("data"):
        log.warning(f"Карты с content_code {content_code} не найдены")
        return None
    return data.get("data", [])


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


async def find_drop_code(code: str) -> str | None:
    resource_url = f"{HOST}/resources?drop={code}"
    monsters_url = f"{HOST}/monsters?drop={code}"
    data = []
    async with aiohttp.ClientSession() as session:
        async with session.get(resource_url) as resource_res:
            if resource_res.status == 200:
                resource_data = await resource_res.json()
                if resource_data.get("data"):
                    data.extend(resource_data["data"])
        async with session.get(monsters_url) as monster_res:
            if monster_res.status == 200:
                monster_data = await monster_res.json()
                if monster_data.get("data"):
                    data.extend(monster_data["data"])
    max_rate = 0
    return_data = None
    for item in data:
        for drop in item.get("drops", []):
            if drop.get("code") == code:
                if drop.get("rate", 0) > max_rate:
                    max_rate = drop.get("rate", 0)
                    return_data = item.get("code")

    return return_data


async def find_map_resource(player_data, resource_code) -> int | None:
    """
    Ближайщий поиск, где добывать ресурс
    """
    drop = await find_drop_code(resource_code)
    if drop is None:
        return
    work_map_list = await find_map(drop)
    if work_map_list is None:
        return
    work_map = find_nearest_map(player_data, work_map_list)
    return work_map


async def find_craftable(code: str) -> dict | None:
    url = f"{HOST}/items/{code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status != 200:
                error = localize_error(str(response.status))
                log.warning(f"{response.status} {error}")
                return None
            data = await response.json()
    if not data.get("data"):
        log.warning(f"Предмет с кодом {code} не найден")
        return None
    item_data = data["data"]
    return item_data["craft"]
