from enum import Enum

class ItemSlot(str, Enum):
    AMULET = "amulet"
    ARTIFACT1 = "artifact1"
    ARTIFACT2 = "artifact2"
    ARTIFACT3 = "artifact3"
    BAG = "bag"
    BODY_ARMOR = "body_armor"
    BOOTS = "boots"
    HELMET = "helmet"
    LEG_ARMOR = "leg_armor"
    RING1 = "ring1"
    RING2 = "ring2"
    RUNE = "rune"
    SHIELD = "shield"
    UTILITY1 = "utility1"
    UTILITY2 = "utility2"
    WEAPON = "weapon"

    def __str__(self) -> str:
        return str(self.value)
