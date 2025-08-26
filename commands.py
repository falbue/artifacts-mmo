from request_mmo import request_mmo
from utils import *

def scan_data(data_type="maps", all_data=True):
    if all_data is True:
        cache_file = f"{data_type}.json"
        cache_data = load_file(cache_file, True)
        
        if cache_data is not None:
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            if datetime.now() - cache_time < timedelta(hours=1):
                logger.debug("Данные из кеша")
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
        if isinstance(result, dict) and "data" in result:
            return result["data"]
        return None
    
    return None

scan_data("maps")

def find_workshop(craftable):
    results = []
    maps = scan_maps()
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

def gathering(character, quantity):
    cooldown = character_cooldown(character["Окончание кулдауна"])
    logger.debug(f"{character['Имя']} приступил к добыванию ресурса")
    time.sleep(cooldown)
    for i in range(quantity):
        cooldown = request_mmo(f"/my/{character['Имя']}/action/gathering", True, True)
        time.sleep(cooldown)

def fight(name, cooldown, quantity):
    logger.debug(f"{name} начал бой")
    time.sleep(int(cooldown))
    for i in range(quantity):
        cooldown = request_mmo(f"/my/{name}/action/fight", True, True)
        time.sleep(cooldown)

def craft(name, resource, cooldown, quantity):
    logger.debug(f"{name} начал крафт")
    time.sleep(int(cooldown))
    cooldown = request_mmo(f"/my/{name}/action/crafting", {"code":resource, "quantity":quantity}, True)
    time.sleep(cooldown)