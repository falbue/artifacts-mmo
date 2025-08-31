from request_mmo import request_mmo
from utils import *
from commands import *


def extraction(character, resource, quantity=1):
    skill, coordinates = find_resource(resource)
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        request_mmo(f"/my/{name}/action/move", coordinates)
        logger.debug(f"{character['Имя']} приступил к добыванию ресурса {resource}")
    
        gathered_count = 0
        while gathered_count < quantity:
            if skill == 'mining':
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

def crafting(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    items = scan_data("items")
    for character in characters:
        name = character["Имя"]
        for item in items:
            if item.get("Код") == resource:
                craftable = item["craft"]["skill"]
                coordinates = find_workshop(craftable)
        request_mmo(f"/my/{name}/action/move", coordinates)
        thread = threading.Thread(target=craft, args=(character, resource, quantity))
        thread.start()

def equip_item(character="all", item="", quantity=1):
    slot = scan_data("items", item)
    if slot:
        slot = slot["Тип"]
        body = {
        "code": item,
        "slot": slot,
        "quantity": quantity
        }
    else:return

    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        request_mmo(f"/my/{name}/action/equip", body)

def deposit_bank(character, item="all", quantity="all", take_items="deposit"):
    characters = load_characters(character)
    items = scan_data("items")

    if take_items == "withdraw":
        bank_inventory = request_mmo("/my/bank/items")["data"]
        bank_item_quantity = find_item_inventory(item, bank_inventory)
        if bank_item_quantity is None:
            return

    for character in characters:
        package = []
        name = character["Имя"]
        inventory = character["Инвентарь"]
        if item == "all":
            if take_items == "deposit":
                for inventory_item in inventory:
                    code = inventory_item["Код"] 
                    quantity = inventory_item["Количество"]
                    if quantity > 0:
                        deposit.append({"code": code, "quantity": quantity})
            elif take_items == "withdraw ":
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
            request_mmo(f"/my/{name}/action/bank/{take_items}/item", [{"code": item, "quantity":quantity}]) 

# extraction("Falbue", "egg", 2)
