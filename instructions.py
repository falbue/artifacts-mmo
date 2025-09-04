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
        equip_item(character, item=tool)
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['name']} приступил к добыванию ресурса {resource}")

    gathered_count = 0
    while gathered_count < quantity:
        if skill == "mob":
            data = fight(character)
            if data["data"]['fight'].get("result") != "loss":
                items = data['data']["fight"]["drops"]
            else:
                extraction(character, resource, quantity=quantity - gathered_count)
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

        result = inventory_full(data)
        if result is True:
            logger.warning(f"Инвентарь {name} полный")
            deposit_bank(character, item="all", quantity="all", take_items="deposit")
            extraction(character, resource, quantity=quantity - gathered_count)

    logger.info(f"{character['name']} добыл {gathered_count} {resource}")
    return

def crafting(character, crafting_item=None, quantity=1, ):
    items = scan_data("items")
    name = character["name"]

    for item in items:
        if item.get("code") == crafting_item:
            craft_items = item["craft"]["items"]
            for craft_item in craft_items:
                quantity_craft = craft_item["quantity"] * quantity
                find_item = find_item_inventory(craft_item["code"], character["inventory"])
                if find_item <= quantity_craft:
                    bank_inventory = request_mmo("/my/bank/items")["data"]
                    find_item_bank = find_item_inventory(craft_item["code"], bank_inventory)
                    if find_item_bank + find_item < quantity_craft:
                        give_bank = "all"
                        logger.debug(f"{name} не хватило {quantity_craft - (find_item + find_item_bank)} {craft_item['code']} для крафта {crafting_item}")
                        extraction(character, craft_item["code"], quantity_craft - (find_item + find_item_bank))
                    elif find_item_bank + find_item >= quantity_craft:
                        give_bank = quantity_craft - find_item
                        if give_bank > 0: 
                            deposit_bank(character, item=craft_item["code"], quantity=give_bank, take_items=True)



            craftable = item["craft"]["skill"]
            coordinates = find_workshop(craftable)
            request_mmo(f"/my/{name}/action/move", coordinates)
            craft(character, crafting_item, quantity)
            logger.info(f"{name} создал {crafting_item}")
            return

def equip_item(character, item="", quantity=1):
    inventory = find_item_inventory(item, character["inventory"])
    if inventory == 0:
        inventory = find_item_inventory(item, request_mmo("/my/bank/items")["data"])
        if inventory == 0:
            logger.warning(f"Невозможно надеть {item}. Не найден в банке и инвентаре")
            return
        else:
            deposit_bank(character, item=item, quantity=quantity, take_items=True)

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

    package = [] # предметы, для обмена
    gold = {} # золото

    if take_items != "deposit": # взятие из банка
        take_items = "withdraw"
        if item == "all": # проверка на возможность взятия всех предметов
            logger.warning(f"{name} не сможет забрать всё из банка")
            return

    if take_items == "withdraw": # Проверка, на наличие нужного предмета
        if item == "gold" and quantity != "all":
            bank_gold = request_mmo("my/bank")["data"]["gold"]
            if bank_gold < quantity:
                logger.error(f"В банке не хватило {quantity - bank_gold} для {name}")
                return
        else:
            bank_inventory = request_mmo("/my/bank/items")["data"]
            bank_item_quantity = find_item_inventory(item, bank_inventory)
            if bank_item_quantity is None:
                logger.error(f"{name} не нашёл в банке {item}")
                return
    
            if quantity == "all" and item != "gold":
                quantity = bank_item_quantity 

    name = character["name"]
    inventory = character["inventory"]

    if item == "all": # получаем все предметы для депозита
        gold["quantity"] = character['gold']
        for inventory_item in inventory:
            code = inventory_item["code"] 
            quantity_item = inventory_item["quantity"]
            if quantity_item > 0:
                package.append({"code": code, "quantity": quantity_item})

    else: # получаем нужный предмет для обмена
        if item == "gold": # работа с золотом
            if take_items == "deposit": 
                gold_quantity = character["gold"]
                if quantity == "all":
                    quantity = gold_quantity
                    if gold_quantity < quantity:
                        logger.error(f"У {name} не хватает {quantity - gold_quantity} золота")
                        return
            
            if take_items == "withdraw" and quantity == "all":
                bank_gold = request_mmo("my/bank")["data"]["gold"]
                quantity = bank_gold
            
            if quantity == 0:
                logger.warning(f"У {name} нет золота")
                return
            gold["quantity"] = quantity

        if item != "gold": # работа с предметом
            if take_items == "deposit":
                item_quantity = find_item_inventory(item, inventory)
                if quantity == "all":
                    quantity = item_quantity
                if item_quantity is None:
                    logger.error("{item} не найден в инветаре {name}")
                    return
                elif item_quantity < quantity:
                    logger.error(f"В инвентаре {name} не хватает {quantity - item_quantity} {item}")
                    return    
            if quantity == 0:
                logger.warning(f"У {name} нет {item}")
                return
            package = [{"code": item, "quantity":quantity}]

    coordinates = find_workshop("bank")
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{name} пришёл в банк")

    if item == "gold":
        request_mmo(f"/my/{name}/action/bank/{take_items}/gold", gold)
    elif item == "all":
        if gold["quantity"] > 0:
            request_mmo(f"/my/{name}/action/bank/{take_items}/gold", gold)
        if package != []:
            request_mmo(f"/my/{name}/action/bank/{take_items}/item", package)
    else:
        request_mmo(f"/my/{name}/action/bank/{take_items}/item", package)

    if take_items == "deposit":
        logger.debug(f"{name} положил в банк {quantity} {item}")
    else:
        logger.debug(f"{name} взял из банка {quantity} {item}")


def fighting(character, mob="chicken", fights=1):
    name = character["name"]
    coordinates = find_map_object(mob)
    request_mmo(f"/my/{name}/action/move", coordinates)
    logger.debug(f"{character['name']} начинает бой с {mob}")
    data = fight(character, fights)
    if data[0] == False:
        fighting(character, mob=mob, fights=fights - data[1])

def complete_task(character):
    task = character['task']
    task_total = character["task_total"]
    task_progress = character["task_progress"]
    task_type = character['task_type']
    name = character["name"]
    logger.debug(f"{name} приступил к выполнению задания {task}")
    if task_type == "items":
        result1 = find_item_inventory(task, character["inventory"])
        result2 = find_item_inventory(task, request_mmo("/my/bank/items")["data"])
        if result2 > 0 and result1 < task_total:
            deposit_bank(character, item=task, quantity="all", take_items=True)
        if result1 + result2 <= task_total:
            result3 = task_total - result2 - result1
            if result3 > 0:
                extraction(character, task, result3)

        coordinates = find_workshop("items")
        request_mmo(f"/my/{name}/action/move", coordinates)
        logger.debug(f"{name} пришёл к мастеру {task_type}")

        request_mmo(f"/my/{name}/action/task/trade", {"code": task, "quantity": task_total})
        logger.debug(f"{name} отдал мастеру {task_type} {task_total} {task}")

        request_mmo(f"/my/{name}/action/task/complete", True)
        logger.info(f"{name} выполнил задание {task}")
        return
    else:
        fights = task_total - task_progress
        fighting(character, task, fights)
        return

def new_task(character, task_type="items"):
    result = character["task"]
    name = character["name"]
    if result == "":
        name = character["name"]
        coordinates = find_workshop(task_type)
        request_mmo(f"/my/{name}/action/move", coordinates)
        logger.debug(f"{name} пришёл к мастеру {task_type}")
        data = request_mmo(f"/my/{name}/action/task/new", True)["data"]
        logger.info(f"{name} получил задание {data['task']['code']}")
    else:
        logger.debug(f"{name} уже имеет задание {result}")
    return

def solution_task(character, task_type="items"):
    result = character["task"]
    if result != "":
        complete_task(character)
    else:
        new_task(character, task_type)
        complete_task(character)
    return