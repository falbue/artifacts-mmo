from request_mmo import request_mmo
from utils import *
from commands import *


def character_action(func, character, *args, **kwargs):
    characters = load_characters(character)
    threads = []
    for character in characters:
        thread = threading.Thread(
            target=func, 
            args=(character, *args), 
            kwargs=kwargs
        )
        thread.start()
        threads.append(thread)
    
    return threads


def extraction(character, resource, quantity=1):
    skill, coordinates = find_resource(resource)
    name = character["Имя"]
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['Имя']} приступил к добыванию ресурса {resource}")

    gathered_count = 0
    while gathered_count < quantity:
        if skill in ['mining', "fishing"]:
            data = gathering(character)
            items = data["data"]["details"]["items"]
        elif skill == "mob":
            data = fight(character)
            items = data['data']["fight"]["drops"]

        found_target_resource = False
        for item_data in items:
            if item_data["Код"] == resource:
                found_target_resource = True
                gathered_count += 1
                logger.debug(f'Успешно добыт {resource}')
            else:
                logger.debug(f'Добыт {item_data["Код"]} вместо {resource}')
    logger.info(f"{character['Имя']} добыл {gathered_count} {resource}")
    return

def crafting(character, resource=None, quantity=1):
    items = scan_data("items")
    name = character["Имя"]
    for item in items:
        if item.get("Код") == resource:
            craftable = item["craft"]["skill"]
            coordinates = find_workshop(craftable)
    request_mmo(f"/my/{name}/action/move", coordinates)
    craft(character, resource, quantity)

def equip_item(character, item="", quantity=1):
    slot = scan_data("items", item)
    if slot:
        slot = slot["Тип"]
        if slot == "ring":
            if character["Кольцо 1"] == "":
                slot = 'ring1'
            elif character["Кольцо 2"] == "":
                slot = 'ring2'
            else:
                logger.warning("Слот для колец занят")
                return
        body = {
        "code": item,
        "slot": slot,
        "quantity": quantity
        }
    else:return

    name = character["Имя"]
    request_mmo(f"/my/{name}/action/equip", body)

def deposit_bank(character, item="all", quantity="all", take_items="deposit"):
    items = scan_data("items")

    if take_items != "deposit":
        take_items = "withdraw"

    if take_items == "withdraw":
        bank_inventory = request_mmo("/my/bank/items")["data"]
        bank_item_quantity = find_item_inventory(item, bank_inventory)
        if bank_item_quantity is None:
            return
        if quantity == "all":
            quantity = bank_item_quantity 
    package = []

    coordinates = find_workshop("bank")
    name = character["Имя"]
    request_mmo(f"/my/{name}/action/move", coordinates)
    inventory = character["Инвентарь"]
    if item == "all":
        if take_items == "deposit":
            for inventory_item in inventory:
                code = inventory_item["Код"] 
                quantity = inventory_item["Количество"]
                if quantity > 0:
                    package.append({"code": code, "quantity": quantity})
        else:
            logger.warning(f"{name} не сможет забрать всё из банка")
            return
        request_mmo(f"/my/{name}/action/bank/{take_items}/item", package)
    else:
        if take_items == "deposit":
            item_quantity = find_item_inventory(item, inventory)
            if item_quantity is None:
                return
            if  quantity == "all":
                quantity = item_quantity
        package = [{"code": item, "quantity":quantity}]
        request_mmo(f"/my/{name}/action/bank/{take_items}/item", package)

    if take_items == "deposit":
        logger.debug(f"{name} положил в банк {item}")
    else:
        logger.debug(f"{name} взял из банка {item}")

def fighting(character, mob="chicken", fights=1):
    name = character["Имя"]
    coordinates = find_map_object(mob)
    if len(coordinates) > 1 and isinstance(coordinates, list):
        coordinates = nearest_object(coordinates, {"x":character["x"],"y":character["y"]})
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['Имя']} начинает бой с {mob}")
    fight(character, fights)
