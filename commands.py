from request_mmo import request_mmo
from utils import *

def scan_data(data_type="all", all_data=True, scanning=False):
    if data_type == "all":
        for scan in ["maps", "items", "resources", "monsters"]:
            scan_data(scan, scanning=scanning)
        return
    if all_data is True:
        cache_file = f"{data_type}.json"
        cache_data = load_file(cache_file, True)
        
        if cache_data is not None and scanning != True:
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
        
    elif isinstance(all_data, str) and all_data != "":
        result = request_mmo(f"{data_type}/{all_data}")
        logger.debug(f"Получение данных о {all_data}")
        if result:
            return result["data"]
        return None

def find_workshop(craftable):
    results = []
    maps = scan_data("maps")
    for item in maps:
        if item.get("content"):
            if item["content"].get("code") == craftable:
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

def check_tool(character, item_type):
    items_data = scan_data("items")
    items_dict = {item["code"]: item for item in items_data if "code" in item}
    
    def find_best_item(inventory_items):
        best_item = None
        best_critical_value = 0
        
        for inventory_item in inventory_items:
            item_code = inventory_item.get("code")
            if not item_code:
                continue

            item_data = items_dict.get(item_code)
            if not item_data:
                continue
            
            if item_type == "mob":
                if item_data.get("type") == "weapon":
                    critical_value = 0
                    for effect in item_data.get("effects", []):
                        if effect.get("code") == "critical_strike":
                            critical_value = effect.get("value", 0)
                            break
                    if best_item is None or critical_value > best_critical_value:
                        best_item = item_data
                        best_critical_value = critical_value
            else:
                for effect in item_data.get("effects", []):
                    if effect.get("code") == item_type:
                        level = item_data.get("level", 0)
                        if best_item is None or level > best_item["level"]:
                            best_item = item_data
                        break
        return best_item
    
    best_inventory_item = find_best_item(character["inventory"])
    
    bank_inventory = request_mmo("/my/bank/items")["data"]
    best_bank_item = find_best_item(bank_inventory)
    best_item = [best_inventory_item, best_bank_item]
    best_inventory = find_best_item(best_item)
    
    if best_inventory["code"] == best_inventory_item["code"]:
        equip = {"equip": "inventory", "tool": best_inventory["code"]}
    elif best_inventory["code"] == best_bank_item["code"]:
        equip = {"equip": "bank", "tool": best_inventory["code"]}
    else:
        equip = None
        logger.debug(f"{character['name']} не нашёл подходящего инструмента")
    
    if equip:
        equip_item = character["weapon_slot"]
        if equip["tool"] == equip_item:
            equip = None
            logger.debug(f"На {character['name']} уже экиперован {equip_item}")

    return equip

def restore_health(character, min_health=30):
    if isinstance(character, list):
        character = character[0]
    
    health = character['hp']
    max_health = character['max_hp']
    threshold = max_health * min_health / 100

    if health < threshold:
        request_mmo(f"/my/{character['name']}/action/rest", True)
        logger.info(f"{character['name']} восстановил здоровье")

def gathering(character):
    data = request_mmo(f"/my/{character['name']}/action/gathering", True)
    return data


def fight(character, fights=1):
    restore_health(character)
    for _ in range(fights):
        try:
            data = request_mmo(f"/my/{character['name']}/action/fight", True)
        except:
            logger.info(f"{character['name']} умер!")
            return
    return data

def craft(character, resource, quantity):
    name = character['name']
    logger.debug(f"{name} начал крафт {resource}")
    request_mmo(f"/my/{name}/action/crafting", {"code":resource, "quantity":quantity})