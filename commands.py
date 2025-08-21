from mmo_request import mmo_request
from utils import *

def gathering(name, cooldown, quantity):
    logger.debug(f"{name} приступил к добыванию ресурса")
    time.sleep(int(cooldown))
    for i in range(quantity):
        cooldown = mmo_request(f"/my/{name}/action/gathering", True, True)
        time.sleep(cooldown)

def fight(name, cooldown, quantity):
    logger.debug(f"{name} начал бой")
    time.sleep(int(cooldown))
    for i in range(quantity):
        cooldown = mmo_request(f"/my/{name}/action/fight", True, True)
        time.sleep(cooldown)

def craft(name, cooldown, quantity):
    logger.debug(f"{name} начал крафт")
    time.sleep(int(cooldown))
    for i in range(quantity):
        cooldown = mmo_request("/my/{name}/action/crafting", True, True)
        time.sleep(cooldown)