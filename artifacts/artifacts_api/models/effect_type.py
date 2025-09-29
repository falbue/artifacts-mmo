from enum import Enum

class EffectType(str, Enum):
    COMBAT = "combat"
    CONSUMABLE = "consumable"
    EQUIPMENT = "equipment"

    def __str__(self) -> str:
        return str(self.value)
