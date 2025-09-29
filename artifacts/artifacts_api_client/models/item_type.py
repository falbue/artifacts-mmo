from enum import Enum

class ItemType(str, Enum):
    AMULET = "amulet"
    ARTIFACT = "artifact"
    BAG = "bag"
    BODY_ARMOR = "body_armor"
    BOOTS = "boots"
    CONSUMABLE = "consumable"
    CURRENCY = "currency"
    HELMET = "helmet"
    LEG_ARMOR = "leg_armor"
    RESOURCE = "resource"
    RING = "ring"
    RUNE = "rune"
    SHIELD = "shield"
    UTILITY = "utility"
    WEAPON = "weapon"

    def __str__(self) -> str:
        return str(self.value)
