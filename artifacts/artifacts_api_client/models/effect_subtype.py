from enum import Enum

class EffectSubtype(str, Enum):
    BUFF = "buff"
    DEBUFF = "debuff"
    GATHERING = "gathering"
    GOLD = "gold"
    HEAL = "heal"
    OTHER = "other"
    SPECIAL = "special"
    STAT = "stat"
    TELEPORT = "teleport"

    def __str__(self) -> str:
        return str(self.value)
