from request_mmo import request_mmo
from utils import *

def scan_data(data_type="all", all_data=True):
    if data_type == "all":
        for scan in ["maps", "items", "resources", "monsters"]:
            scan_data(scan)
        return
    if all_data is True:
        cache_file = f"{data_type}.json"
        cache_data = load_file(cache_file, True)
        
        if cache_data is not None:
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            if datetime.now() - cache_time < timedelta(hours=1):
                logger.debug(f"Данные {data_type} из кеша")
                return cache_data['data']
        
        logger.debug(f"Cканирование {data_type}...")
        data_list = []
        initial_data = request_mmo(f"/{data_type}?size=100")
        pages = initial_data["pages"]
        
        for i in range(pages):
            command = f"/{data_type}?size=100&page={i+1}"
            page_data = request_mmo(command)
            data_list.extend(page_data["data"])
        
        cache_data = {
            'timestamp': datetime.now().isoformat(),
            'data': data_list
        }
        
        save_file(cache_file, cache_data)
        return data_list
        
    elif isinstance(all_data, str):
        result = request_mmo(f"{data_type}/{all_data}")
        if result:
            return result["data"]
        return None
    
    return None

def find_workshop(craftable):
    results = []
    maps = scan_data("maps")
    for item in maps:
        if item.get("Контент"):
            if item["Контент"].get("Код") == craftable:
                x = item.get("x")
                y = item.get("y")
                if x is not None and y is not None:
                   results.append({"x": x, "y": y})
    return results[0]

def load_characters(character):
    characters = request_mmo("/my/characters")
    names = []
    if character == "all":
        for i in range(len(characters["data"])):
            names.append(characters["data"][i])
    elif isinstance(character, int) and character <= len(characters["data"]):
        names.append(characters["data"][character-1])
    elif isinstance(character, str):
        x = find_character(characters, character)
        if names is None:
            logger.error("Персонаж не выбран. Измените параметры")
        names.append(x)
    else:
        logger.error("Персонаж не выбран. Измените параметры")
    return names

def restore_health(character, min_health=30):
    if isinstance(character, list):
        character = character[0]
    
    health = character['Здоровье']
    max_health = character['Максимальное здоровье']
    threshold = max_health * min_health / 100

    if health < threshold:
        request_mmo(f"/my/{character['Имя']}/action/rest", True)
        logger.info(f"{character['Имя']} восстановил здоровье")

def gathering(character):
    data = request_mmo(f"/my/{character['Имя']}/action/gathering", True)
    return data


def fight(character, fights=1):
    restore_health(character)
    for _ in range(fights):
        data = request_mmo(f"/my/{character['Имя']}/action/fight", True)
        if data == 598:
            logger.info(f"{character['Имя']} умер!")
        restore_health(data["data"]["character"])
    return data

def craft(character, resource, quantity):
    name = character['Имя']
    logger.debug(f"{name} начал крафт {resource}")
    request_mmo(f"/my/{name}/action/crafting", {"code":resource, "quantity":quantity})