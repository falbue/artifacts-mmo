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

def check_tool(character, item_type):
    items_data = scan_data("items")
    items_dict = {item["Код"]: item for item in items_data if "Код" in item}
    
    def find_best_item(inventory_items):
        best_item = None
        
        for inventory_item in inventory_items:
            item_code = inventory_item.get("Код")
            if not item_code:
                continue

            item_data = items_dict.get(item_code)
            if not item_data:
                continue
            
            if item_type == "mob":
                if (item_data.get("Тип") == "weapon" and 
                    item_data.get("Подтип") in ["", "sword", "axe", "mace", "dagger"]):
                    level = item_data.get("Уровень", 0)
                    if best_item is None or level > best_item["level"]:
                        best_item = {"item": item_data, "level": level}
            else:
                for effect in item_data.get("effects", []):
                    if effect.get("Код") == item_type:
                        level = item_data.get("Уровень", 0)
                        if best_item is None or level > best_item["level"]:
                            best_item = {"item": item_data, "level": level}
                        break
        
        return best_item
    
    best_inventory_item = find_best_item(character["Инвентарь"])
    
    bank_inventory = request_mmo("/my/bank/items")["data"]
    best_bank_item = find_best_item(bank_inventory)
    
    if best_inventory_item:
        return {"equip": "inventory", "tool": best_inventory_item["item"]["Код"]}
    elif best_bank_item:
        return {"equip": "bank", "tool": best_bank_item["item"]["Код"]}
    
    return None

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
    return data

def craft(character, resource, quantity):
    name = character['Имя']
    logger.debug(f"{name} начал крафт {resource}")
    request_mmo(f"/my/{name}/action/crafting", {"code":resource, "quantity":quantity})