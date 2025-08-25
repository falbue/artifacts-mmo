from mmo_request import mmo_request
from utils import *
from commands import *


def mining_resource(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        maps = scan_maps()
        coordinates = find_objects(maps, resource)
        if len(coordinates) > 1:
            coordinates = nearest_object(coordinates, {"x":character["x"],"y":character["y"]})
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def fighting(character="all", resource=None, quantity=1):
    characters = load_characters(character)
    for character in characters:
        name = character["Имя"]
        maps = scan_maps()
        coordinates = find_objects(maps, resource)
        cooldown = 0
        cooldown = mmo_request(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=gathering, args=(name, cooldown, quantity))
        thread.start()


def crafting(character="all", resource=None, quantity=1):
    names = load_characters(character)
    for character in characters:
        name = character["Имя"]
        items = scan_items()
        for item in items:
            if item.get("Код") == resource:
                craftable = item["craft"]["skill"]
                coordinates = find_workshop(craftable)
        cooldown = mmo_request(f"/my/{name}/action/move", coordinates, cooldown=True)
        thread = threading.Thread(target=craft, args=(name, resource, cooldown, quantity))
        thread.start()

mining_resource(character="all", resource="ash_tree", quantity=1)
# crafting(character="all", resource="copper_helmet", quantity=1)