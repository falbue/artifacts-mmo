from request_mmo import request_mmo
from utils import *
from commands import *


def mining_resource(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        maps = scan_data("maps")
        coordinates = find_resource(resource)
        if len(coordinates) > 1 and isinstance(coordinates, list):
            coordinates = nearest_object(coordinates, {"x":character["x"],"y":character["y"]})
        cooldown = character_cooldown(character["Окончание кулдауна"])
        request_mmo(f"/my/{name}/action/move", coordinates, cooldown)
        character = load_characters(name)[0]
        thread = threading.Thread(target=gathering, args=(character, quantity))
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

mining_resource(character=1, resource="copper_ore", quantity=1)