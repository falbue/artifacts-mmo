from enum import Enum

class CraftSkill(str, Enum):
    ALCHEMY = "alchemy"
    COOKING = "cooking"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    MINING = "mining"
    WEAPONCRAFTING = "weaponcrafting"
    WOODCUTTING = "woodcutting"

    def __str__(self) -> str:
        return str(self.value)
