from collections.abc import Mapping
from typing import Any, TypeVar, Optional, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.character_skin import CharacterSkin
from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
from typing import Union
import datetime

if TYPE_CHECKING:
  from ..models.inventory_slot import InventorySlot





T = TypeVar("T", bound="CharacterSchema")



@_attrs_define
class CharacterSchema:
    """ 
        Attributes:
            name (str): Name of the character.
            account (str): Account name.
            skin (CharacterSkin):
            level (int): Combat level.
            xp (int): The current xp level of the combat level.
            max_xp (int): XP required to level up the character.
            gold (int): The numbers of gold on this character.
            speed (int): *Not available, on the roadmap. Character movement speed.
            mining_level (int): Mining level.
            mining_xp (int): The current xp level of the Mining skill.
            mining_max_xp (int): Mining XP required to level up the skill.
            woodcutting_level (int): Woodcutting level.
            woodcutting_xp (int): The current xp level of the Woodcutting skill.
            woodcutting_max_xp (int): Woodcutting XP required to level up the skill.
            fishing_level (int): Fishing level.
            fishing_xp (int): The current xp level of the Fishing skill.
            fishing_max_xp (int): Fishing XP required to level up the skill.
            weaponcrafting_level (int): Weaponcrafting level.
            weaponcrafting_xp (int): The current xp level of the Weaponcrafting skill.
            weaponcrafting_max_xp (int): Weaponcrafting XP required to level up the skill.
            gearcrafting_level (int): Gearcrafting level.
            gearcrafting_xp (int): The current xp level of the Gearcrafting skill.
            gearcrafting_max_xp (int): Gearcrafting XP required to level up the skill.
            jewelrycrafting_level (int): Jewelrycrafting level.
            jewelrycrafting_xp (int): The current xp level of the Jewelrycrafting skill.
            jewelrycrafting_max_xp (int): Jewelrycrafting XP required to level up the skill.
            cooking_level (int): The current xp level of the Cooking skill.
            cooking_xp (int): Cooking XP.
            cooking_max_xp (int): Cooking XP required to level up the skill.
            alchemy_level (int): Alchemy level.
            alchemy_xp (int): Alchemy XP.
            alchemy_max_xp (int): Alchemy XP required to level up the skill.
            hp (int): Character actual HP.
            max_hp (int): Character max HP.
            haste (int): *Increase speed attack (reduce fight cooldown)
            critical_strike (int): % Critical strike. Critical strikes adds 50% extra damage to an attack (1.5x).
            wisdom (int): Wisdom increases the amount of XP gained from fights and skills (1% extra per 10 wisdom).
            prospecting (int): Prospecting increases the chances of getting drops from fights and skills (1% extra per 10
                PP).
            attack_fire (int): Fire attack.
            attack_earth (int): Earth attack.
            attack_water (int): Water attack.
            attack_air (int): Air attack.
            dmg (int): % Damage. Damage increases your attack in all elements.
            dmg_fire (int): % Fire damage. Damage increases your fire attack.
            dmg_earth (int): % Earth damage. Damage increases your earth attack.
            dmg_water (int): % Water damage. Damage increases your water attack.
            dmg_air (int): % Air damage. Damage increases your air attack.
            res_fire (int): % Fire resistance. Reduces fire attack.
            res_earth (int): % Earth resistance. Reduces earth attack.
            res_water (int): % Water resistance. Reduces water attack.
            res_air (int): % Air resistance. Reduces air attack.
            x (int): Character x coordinate.
            y (int): Character y coordinate.
            cooldown (int): Cooldown in seconds.
            weapon_slot (str): Weapon slot.
            rune_slot (str): Rune slot.
            shield_slot (str): Shield slot.
            helmet_slot (str): Helmet slot.
            body_armor_slot (str): Body armor slot.
            leg_armor_slot (str): Leg armor slot.
            boots_slot (str): Boots slot.
            ring1_slot (str): Ring 1 slot.
            ring2_slot (str): Ring 2 slot.
            amulet_slot (str): Amulet slot.
            artifact1_slot (str): Artifact 1 slot.
            artifact2_slot (str): Artifact 2 slot.
            artifact3_slot (str): Artifact 3 slot.
            utility1_slot (str): Utility 1 slot.
            utility1_slot_quantity (int): Utility 1 quantity.
            utility2_slot (str): Utility 2 slot.
            utility2_slot_quantity (int): Utility 2 quantity.
            bag_slot (str): Bag slot.
            task (str): Task in progress.
            task_type (str): Task type.
            task_progress (int): Task progression.
            task_total (int): Task total objective.
            inventory_max_items (int): Inventory max items.
            cooldown_expiration (Union[Unset, datetime.datetime]): Datetime Cooldown expiration.
            inventory (Union[Unset, list['InventorySlot']]): List of inventory slots.
     """

    name: str
    account: str
    skin: CharacterSkin
    level: int
    xp: int
    max_xp: int
    gold: int
    speed: int
    mining_level: int
    mining_xp: int
    mining_max_xp: int
    woodcutting_level: int
    woodcutting_xp: int
    woodcutting_max_xp: int
    fishing_level: int
    fishing_xp: int
    fishing_max_xp: int
    weaponcrafting_level: int
    weaponcrafting_xp: int
    weaponcrafting_max_xp: int
    gearcrafting_level: int
    gearcrafting_xp: int
    gearcrafting_max_xp: int
    jewelrycrafting_level: int
    jewelrycrafting_xp: int
    jewelrycrafting_max_xp: int
    cooking_level: int
    cooking_xp: int
    cooking_max_xp: int
    alchemy_level: int
    alchemy_xp: int
    alchemy_max_xp: int
    hp: int
    max_hp: int
    haste: int
    critical_strike: int
    wisdom: int
    prospecting: int
    attack_fire: int
    attack_earth: int
    attack_water: int
    attack_air: int
    dmg: int
    dmg_fire: int
    dmg_earth: int
    dmg_water: int
    dmg_air: int
    res_fire: int
    res_earth: int
    res_water: int
    res_air: int
    x: int
    y: int
    cooldown: int
    weapon_slot: str
    rune_slot: str
    shield_slot: str
    helmet_slot: str
    body_armor_slot: str
    leg_armor_slot: str
    boots_slot: str
    ring1_slot: str
    ring2_slot: str
    amulet_slot: str
    artifact1_slot: str
    artifact2_slot: str
    artifact3_slot: str
    utility1_slot: str
    utility1_slot_quantity: int
    utility2_slot: str
    utility2_slot_quantity: int
    bag_slot: str
    task: str
    task_type: str
    task_progress: int
    task_total: int
    inventory_max_items: int
    cooldown_expiration: Union[Unset, datetime.datetime] = UNSET
    inventory: Union[Unset, list['InventorySlot']] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.inventory_slot import InventorySlot
        name = self.name

        account = self.account

        skin = self.skin.value

        level = self.level

        xp = self.xp

        max_xp = self.max_xp

        gold = self.gold

        speed = self.speed

        mining_level = self.mining_level

        mining_xp = self.mining_xp

        mining_max_xp = self.mining_max_xp

        woodcutting_level = self.woodcutting_level

        woodcutting_xp = self.woodcutting_xp

        woodcutting_max_xp = self.woodcutting_max_xp

        fishing_level = self.fishing_level

        fishing_xp = self.fishing_xp

        fishing_max_xp = self.fishing_max_xp

        weaponcrafting_level = self.weaponcrafting_level

        weaponcrafting_xp = self.weaponcrafting_xp

        weaponcrafting_max_xp = self.weaponcrafting_max_xp

        gearcrafting_level = self.gearcrafting_level

        gearcrafting_xp = self.gearcrafting_xp

        gearcrafting_max_xp = self.gearcrafting_max_xp

        jewelrycrafting_level = self.jewelrycrafting_level

        jewelrycrafting_xp = self.jewelrycrafting_xp

        jewelrycrafting_max_xp = self.jewelrycrafting_max_xp

        cooking_level = self.cooking_level

        cooking_xp = self.cooking_xp

        cooking_max_xp = self.cooking_max_xp

        alchemy_level = self.alchemy_level

        alchemy_xp = self.alchemy_xp

        alchemy_max_xp = self.alchemy_max_xp

        hp = self.hp

        max_hp = self.max_hp

        haste = self.haste

        critical_strike = self.critical_strike

        wisdom = self.wisdom

        prospecting = self.prospecting

        attack_fire = self.attack_fire

        attack_earth = self.attack_earth

        attack_water = self.attack_water

        attack_air = self.attack_air

        dmg = self.dmg

        dmg_fire = self.dmg_fire

        dmg_earth = self.dmg_earth

        dmg_water = self.dmg_water

        dmg_air = self.dmg_air

        res_fire = self.res_fire

        res_earth = self.res_earth

        res_water = self.res_water

        res_air = self.res_air

        x = self.x

        y = self.y

        cooldown = self.cooldown

        weapon_slot = self.weapon_slot

        rune_slot = self.rune_slot

        shield_slot = self.shield_slot

        helmet_slot = self.helmet_slot

        body_armor_slot = self.body_armor_slot

        leg_armor_slot = self.leg_armor_slot

        boots_slot = self.boots_slot

        ring1_slot = self.ring1_slot

        ring2_slot = self.ring2_slot

        amulet_slot = self.amulet_slot

        artifact1_slot = self.artifact1_slot

        artifact2_slot = self.artifact2_slot

        artifact3_slot = self.artifact3_slot

        utility1_slot = self.utility1_slot

        utility1_slot_quantity = self.utility1_slot_quantity

        utility2_slot = self.utility2_slot

        utility2_slot_quantity = self.utility2_slot_quantity

        bag_slot = self.bag_slot

        task = self.task

        task_type = self.task_type

        task_progress = self.task_progress

        task_total = self.task_total

        inventory_max_items = self.inventory_max_items

        cooldown_expiration: Union[Unset, str] = UNSET
        if not isinstance(self.cooldown_expiration, Unset):
            cooldown_expiration = self.cooldown_expiration.isoformat()

        inventory: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.inventory, Unset):
            inventory = []
            for inventory_item_data in self.inventory:
                inventory_item = inventory_item_data.to_dict()
                inventory.append(inventory_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
            "account": account,
            "skin": skin,
            "level": level,
            "xp": xp,
            "max_xp": max_xp,
            "gold": gold,
            "speed": speed,
            "mining_level": mining_level,
            "mining_xp": mining_xp,
            "mining_max_xp": mining_max_xp,
            "woodcutting_level": woodcutting_level,
            "woodcutting_xp": woodcutting_xp,
            "woodcutting_max_xp": woodcutting_max_xp,
            "fishing_level": fishing_level,
            "fishing_xp": fishing_xp,
            "fishing_max_xp": fishing_max_xp,
            "weaponcrafting_level": weaponcrafting_level,
            "weaponcrafting_xp": weaponcrafting_xp,
            "weaponcrafting_max_xp": weaponcrafting_max_xp,
            "gearcrafting_level": gearcrafting_level,
            "gearcrafting_xp": gearcrafting_xp,
            "gearcrafting_max_xp": gearcrafting_max_xp,
            "jewelrycrafting_level": jewelrycrafting_level,
            "jewelrycrafting_xp": jewelrycrafting_xp,
            "jewelrycrafting_max_xp": jewelrycrafting_max_xp,
            "cooking_level": cooking_level,
            "cooking_xp": cooking_xp,
            "cooking_max_xp": cooking_max_xp,
            "alchemy_level": alchemy_level,
            "alchemy_xp": alchemy_xp,
            "alchemy_max_xp": alchemy_max_xp,
            "hp": hp,
            "max_hp": max_hp,
            "haste": haste,
            "critical_strike": critical_strike,
            "wisdom": wisdom,
            "prospecting": prospecting,
            "attack_fire": attack_fire,
            "attack_earth": attack_earth,
            "attack_water": attack_water,
            "attack_air": attack_air,
            "dmg": dmg,
            "dmg_fire": dmg_fire,
            "dmg_earth": dmg_earth,
            "dmg_water": dmg_water,
            "dmg_air": dmg_air,
            "res_fire": res_fire,
            "res_earth": res_earth,
            "res_water": res_water,
            "res_air": res_air,
            "x": x,
            "y": y,
            "cooldown": cooldown,
            "weapon_slot": weapon_slot,
            "rune_slot": rune_slot,
            "shield_slot": shield_slot,
            "helmet_slot": helmet_slot,
            "body_armor_slot": body_armor_slot,
            "leg_armor_slot": leg_armor_slot,
            "boots_slot": boots_slot,
            "ring1_slot": ring1_slot,
            "ring2_slot": ring2_slot,
            "amulet_slot": amulet_slot,
            "artifact1_slot": artifact1_slot,
            "artifact2_slot": artifact2_slot,
            "artifact3_slot": artifact3_slot,
            "utility1_slot": utility1_slot,
            "utility1_slot_quantity": utility1_slot_quantity,
            "utility2_slot": utility2_slot,
            "utility2_slot_quantity": utility2_slot_quantity,
            "bag_slot": bag_slot,
            "task": task,
            "task_type": task_type,
            "task_progress": task_progress,
            "task_total": task_total,
            "inventory_max_items": inventory_max_items,
        })
        if cooldown_expiration is not UNSET:
            field_dict["cooldown_expiration"] = cooldown_expiration
        if inventory is not UNSET:
            field_dict["inventory"] = inventory

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.inventory_slot import InventorySlot
        d = dict(src_dict)
        name = d.pop("name")

        account = d.pop("account")

        skin = CharacterSkin(d.pop("skin"))




        level = d.pop("level")

        xp = d.pop("xp")

        max_xp = d.pop("max_xp")

        gold = d.pop("gold")

        speed = d.pop("speed")

        mining_level = d.pop("mining_level")

        mining_xp = d.pop("mining_xp")

        mining_max_xp = d.pop("mining_max_xp")

        woodcutting_level = d.pop("woodcutting_level")

        woodcutting_xp = d.pop("woodcutting_xp")

        woodcutting_max_xp = d.pop("woodcutting_max_xp")

        fishing_level = d.pop("fishing_level")

        fishing_xp = d.pop("fishing_xp")

        fishing_max_xp = d.pop("fishing_max_xp")

        weaponcrafting_level = d.pop("weaponcrafting_level")

        weaponcrafting_xp = d.pop("weaponcrafting_xp")

        weaponcrafting_max_xp = d.pop("weaponcrafting_max_xp")

        gearcrafting_level = d.pop("gearcrafting_level")

        gearcrafting_xp = d.pop("gearcrafting_xp")

        gearcrafting_max_xp = d.pop("gearcrafting_max_xp")

        jewelrycrafting_level = d.pop("jewelrycrafting_level")

        jewelrycrafting_xp = d.pop("jewelrycrafting_xp")

        jewelrycrafting_max_xp = d.pop("jewelrycrafting_max_xp")

        cooking_level = d.pop("cooking_level")

        cooking_xp = d.pop("cooking_xp")

        cooking_max_xp = d.pop("cooking_max_xp")

        alchemy_level = d.pop("alchemy_level")

        alchemy_xp = d.pop("alchemy_xp")

        alchemy_max_xp = d.pop("alchemy_max_xp")

        hp = d.pop("hp")

        max_hp = d.pop("max_hp")

        haste = d.pop("haste")

        critical_strike = d.pop("critical_strike")

        wisdom = d.pop("wisdom")

        prospecting = d.pop("prospecting")

        attack_fire = d.pop("attack_fire")

        attack_earth = d.pop("attack_earth")

        attack_water = d.pop("attack_water")

        attack_air = d.pop("attack_air")

        dmg = d.pop("dmg")

        dmg_fire = d.pop("dmg_fire")

        dmg_earth = d.pop("dmg_earth")

        dmg_water = d.pop("dmg_water")

        dmg_air = d.pop("dmg_air")

        res_fire = d.pop("res_fire")

        res_earth = d.pop("res_earth")

        res_water = d.pop("res_water")

        res_air = d.pop("res_air")

        x = d.pop("x")

        y = d.pop("y")

        cooldown = d.pop("cooldown")

        weapon_slot = d.pop("weapon_slot")

        rune_slot = d.pop("rune_slot")

        shield_slot = d.pop("shield_slot")

        helmet_slot = d.pop("helmet_slot")

        body_armor_slot = d.pop("body_armor_slot")

        leg_armor_slot = d.pop("leg_armor_slot")

        boots_slot = d.pop("boots_slot")

        ring1_slot = d.pop("ring1_slot")

        ring2_slot = d.pop("ring2_slot")

        amulet_slot = d.pop("amulet_slot")

        artifact1_slot = d.pop("artifact1_slot")

        artifact2_slot = d.pop("artifact2_slot")

        artifact3_slot = d.pop("artifact3_slot")

        utility1_slot = d.pop("utility1_slot")

        utility1_slot_quantity = d.pop("utility1_slot_quantity")

        utility2_slot = d.pop("utility2_slot")

        utility2_slot_quantity = d.pop("utility2_slot_quantity")

        bag_slot = d.pop("bag_slot")

        task = d.pop("task")

        task_type = d.pop("task_type")

        task_progress = d.pop("task_progress")

        task_total = d.pop("task_total")

        inventory_max_items = d.pop("inventory_max_items")

        _cooldown_expiration = d.pop("cooldown_expiration", UNSET)
        cooldown_expiration: Union[Unset, datetime.datetime]
        if isinstance(_cooldown_expiration,  Unset):
            cooldown_expiration = UNSET
        else:
            cooldown_expiration = isoparse(_cooldown_expiration)




        inventory = []
        _inventory = d.pop("inventory", UNSET)
        for inventory_item_data in (_inventory or []):
            inventory_item = InventorySlot.from_dict(inventory_item_data)



            inventory.append(inventory_item)


        character_schema = cls(
            name=name,
            account=account,
            skin=skin,
            level=level,
            xp=xp,
            max_xp=max_xp,
            gold=gold,
            speed=speed,
            mining_level=mining_level,
            mining_xp=mining_xp,
            mining_max_xp=mining_max_xp,
            woodcutting_level=woodcutting_level,
            woodcutting_xp=woodcutting_xp,
            woodcutting_max_xp=woodcutting_max_xp,
            fishing_level=fishing_level,
            fishing_xp=fishing_xp,
            fishing_max_xp=fishing_max_xp,
            weaponcrafting_level=weaponcrafting_level,
            weaponcrafting_xp=weaponcrafting_xp,
            weaponcrafting_max_xp=weaponcrafting_max_xp,
            gearcrafting_level=gearcrafting_level,
            gearcrafting_xp=gearcrafting_xp,
            gearcrafting_max_xp=gearcrafting_max_xp,
            jewelrycrafting_level=jewelrycrafting_level,
            jewelrycrafting_xp=jewelrycrafting_xp,
            jewelrycrafting_max_xp=jewelrycrafting_max_xp,
            cooking_level=cooking_level,
            cooking_xp=cooking_xp,
            cooking_max_xp=cooking_max_xp,
            alchemy_level=alchemy_level,
            alchemy_xp=alchemy_xp,
            alchemy_max_xp=alchemy_max_xp,
            hp=hp,
            max_hp=max_hp,
            haste=haste,
            critical_strike=critical_strike,
            wisdom=wisdom,
            prospecting=prospecting,
            attack_fire=attack_fire,
            attack_earth=attack_earth,
            attack_water=attack_water,
            attack_air=attack_air,
            dmg=dmg,
            dmg_fire=dmg_fire,
            dmg_earth=dmg_earth,
            dmg_water=dmg_water,
            dmg_air=dmg_air,
            res_fire=res_fire,
            res_earth=res_earth,
            res_water=res_water,
            res_air=res_air,
            x=x,
            y=y,
            cooldown=cooldown,
            weapon_slot=weapon_slot,
            rune_slot=rune_slot,
            shield_slot=shield_slot,
            helmet_slot=helmet_slot,
            body_armor_slot=body_armor_slot,
            leg_armor_slot=leg_armor_slot,
            boots_slot=boots_slot,
            ring1_slot=ring1_slot,
            ring2_slot=ring2_slot,
            amulet_slot=amulet_slot,
            artifact1_slot=artifact1_slot,
            artifact2_slot=artifact2_slot,
            artifact3_slot=artifact3_slot,
            utility1_slot=utility1_slot,
            utility1_slot_quantity=utility1_slot_quantity,
            utility2_slot=utility2_slot,
            utility2_slot_quantity=utility2_slot_quantity,
            bag_slot=bag_slot,
            task=task,
            task_type=task_type,
            task_progress=task_progress,
            task_total=task_total,
            inventory_max_items=inventory_max_items,
            cooldown_expiration=cooldown_expiration,
            inventory=inventory,
        )


        character_schema.additional_properties = d
        return character_schema

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
