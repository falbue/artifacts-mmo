from mmo_request import mmo_request
from utils import *
from commands import *

def scan_maps():
    maps_file = "maps.json"
    cache_data = load_file(maps_file)
    if cache_data is not None:
        if isinstance(cache_data, dict) and 'timestamp' in cache_data and 'data' in cache_data:
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            
        if datetime.now() - cache_time < timedelta(hours=1):
            logger.debug("Данные из кеша")
            return cache_data['data']
    
    logger.debug("Cканирование карт...")
    maps = []
    data = mmo_request("/maps?size=100")
    pages = data["pages"]
    
    for i in range(pages):
        command = f"/maps?size=100&page={i+1}"
        data = mmo_request(command)
        maps.extend(data["data"])
    
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'data': maps
    }
    
    save_file(maps_file, cache_data)
    return maps

def scan_items():
    file = "items.json"
    cache_data = load_file(file)
    if cache_data is not None:
        if isinstance(cache_data, dict) and 'timestamp' in cache_data and 'data' in cache_data:
            cache_time = datetime.fromisoformat(cache_data['timestamp'])
            
        if datetime.now() - cache_time < timedelta(hours=1):
            logger.debug("Данные из кеша")
            return cache_data['data']
    
    logger.debug("Cканирование ресурсов...")
    items = []
    data = mmo_request("/items?size=100")
    pages = data["pages"]
    
    for i in range(pages):
        command = f"/items?size=100&page={i+1}"
        data = mmo_request(command)
        items.extend(data["data"])
    
    cache_data = {
        'timestamp': datetime.now().isoformat(),
        'data': items
    }
    
    save_file(file, cache_data)
    return items

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
    characters = mmo_request("/my/characters")
    names = []
    if character == "all":
        for i in range(len(characters["data"])):
            names.append(characters["data"][i]["Имя"])
    elif character <= len(characters["data"]):
        names.append(characters["data"][character-1]["Имя"])
    else:
        logger.error("Персонаж не выбран. Измените параметры")
    return names

def mining_resource(character="all", resource=None, quantity=1):
    names = load_characters(character)
    for name in names:
        maps = scan_maps()
        coordinats = find_objects(maps, resource)
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinats, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def fighting(character="all", resource=None, quantity=1):
    names = load_characters(character)
    for name in names:
        maps = scan_maps()
        coordinats = find_objects(maps, resource)
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinats, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def crafting(character="all", resource=None, quantity=1):
    names = load_characters(character)
    for name in names:
        maps = scan_maps()
        coordinats = find_objects(maps, resource)
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinats, cooldown=True)
        thread = threading.Thread(target=craft, args=(name, cooldown, quantity))
        thread.start()

# scan_maps()
# mining_resource(character="all", resource="copper_rocks", quantity=100)
# crafting(character="all", resource="mining", quantity=10)
# data = mmo_request(f"/items")
# print_mmo(data)
scan_items()