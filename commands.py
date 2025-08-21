from mmo_request import mmo_request
from utils import *

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

def mining_resource(character="all", resource=None, quantity=1):
    characters = mmo_request("/my/characters")
    names = []
    if character == "all":
        for i in range(len(characters["data"])):
            names.append(characters["data"][i]["Имя"])
    elif character <= len(characters["data"]):
        names.append(characters["data"][character-1]["Имя"])
    else:
        logger.error("Персонаж не выбран. Измените параметры")

    for name in names:
        maps = scan_maps()
        coordinats = find_objects(maps, resource)
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinats, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()

def gathering(name, cooldown, quantity):
    logger.debug(f"{name} приступил к добыванию ресурса")
    time.sleep(int(cooldown))
    for i in range(quantity):
        cooldown = mmo_request(f"/my/{name}/action/gathering", True, True)
        time.sleep(cooldown)

# scan_maps()
mining_resource(character="all", resource="copper_rocks", quantity=20)
# data = mmo_request(f"/my/Falbue/action/move", {"x":"0","y":"0"})