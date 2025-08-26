from request_mmo import request_mmo
from utils import *
from commands import *


def mining_resource(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        maps = scan_maps()
        coordinates = find_objects(maps, resource)
        if len(coordinates) > 1 and isinstance(coordinates, list):
            coordinates = nearest_object(coordinates, {"x":character["x"],"y":character["y"]})
        cooldown = 0
        cooldown = request_mmo(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def fighting(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        maps = scan_maps()
        coordinates = find_objects(maps, resource)
        cooldown = 0
        cooldown = request_mmo(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def crafting(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        items = scan_items()
        for item in items:
            if item.get("Код") == resource:
                craftable = item["craft"]["skill"]
                coordinates = find_workshop(craftable)
        cooldown = request_mmo(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=craft, args=(name, resource, cooldown, quantity))
        thread.start()

def equip_item(character="all", item="", quantity=1):
    slot = scan_items(item)
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

# equip_item(item = "copper_helmet", quantity = 1)
# mining_resource(character="all", resource="copper_rocks", quantity=40)
crafting(character="all", resource="copper_bar", quantity=5)