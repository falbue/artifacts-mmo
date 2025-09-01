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
    if check_craftable(resource):
        crafting(character, resource, quantity)
        return
    skill, coordinates = find_resource(resource)
    name = character["name"]
    tool = check_tool(character, skill)
    if tool:
        if tool["equip"] == "bank":
            deposit_bank(character, item=tool["tool"], quantity=1, take_items=True)
        equip_item(character, item=tool["tool"])
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['name']} приступил к добыванию ресурса {resource}")

    gathered_count = 0
    while gathered_count < quantity:
        if skill == "mob":
            data = fight(character)
            items = data['data']["fight"]["drops"]
        else:
            data = gathering(character)
            items = data["data"]["details"]["items"]

        found_target_resource = False
        for item_data in items:
            if item_data["code"] == resource:
                found_target_resource = True
                gathered_count += 1
                logger.debug(f'Успешно добыт {resource}')
            else:
                logger.debug(f'Добыт {item_data["code"]} вместо {resource}')
    logger.info(f"{character['name']} добыл {gathered_count} {resource}")
    return

def crafting(character, crafting_item=None, quantity=1):
    items = scan_data("items")
    name = character["name"]

    for item in items:
        if item.get("code") == crafting_item:
            craft_items = item["craft"]["items"]
            for craft_item in craft_items:
                quantity_craft = craft_item["quantity"] * quantity
                find_item = find_item_inventory(craft_item["code"], character["Инвентарь"])
                if find_item <= quantity_craft:
                    bank_inventory = request_mmo("/my/bank/items")["data"]
                    find_item_bank = find_item_inventory(craft_item["code"], bank_inventory)
                    if find_item_bank + find_item < quantity_craft:
                        give_bank = "all"
                        logger.debug(f"{name} не хватило {quantity_craft - (find_item + find_item_bank)} {craft_item['code']} для крафта {crafting_item}")
                        extraction(character, craft_item["code"], quantity_craft - (find_item + find_item_bank))
                    else:
                        give_bank = quantity_craft

                    if find_item_bank > 0: 
                        deposit_bank(character, item=craft_item["code"], quantity=quantity_craft-find_item, take_items=True)



            craftable = item["craft"]["skill"]
            coordinates = find_workshop(craftable)
            request_mmo(f"/my/{name}/action/move", coordinates)
            craft(character, crafting_item, quantity)
            logger.info(f"{name} создал {crafting_item}")
            return

def equip_item(character, item="", quantity=1):
    slot = scan_data("items", item)
    if slot:
        slot = slot["type"]
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

    name = character["name"]
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
    name = character["name"]
    request_mmo(f"/my/{name}/action/move", coordinates)
    inventory = character["Инвентарь"]
    if item == "all":
        if take_items == "deposit":
            for inventory_item in inventory:
                code = inventory_item["code"] 
                quantity = inventory_item["quantity"]
                if quantity > 0:
                    package.append({"code": code, "quantity": quantity})
        else:
            logger.warning(f"{name} не сможет забрать всё из банка")
            return 
    else:
        if take_items == "deposit":
            item_quantity = find_item_inventory(item, inventory)
            if item_quantity is None:
                return
            if  quantity == "all":
                quantity = item_quantity
        package = [{"code": item, "quantity":quantity}]

    if not package:
        logger.warning(f"Инвентарь {name} пуст")
        return

    if take_items == "deposit":
        logger.debug(f"{name} положил в банк {item}")
    else:
        logger.debug(f"{name} взял из банка {item}")

    request_mmo(f"/my/{name}/action/bank/{take_items}/item", package)

def fighting(character, mob="chicken", fights=1):
    name = character["name"]
    coordinates = find_map_object(mob)
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['name']} начинает бой с {mob}")
    fight(character, fights)
