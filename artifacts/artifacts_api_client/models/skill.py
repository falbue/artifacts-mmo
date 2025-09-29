from enum import Enum

class Skill(str, Enum):
    ALCHEMY = "alchemy"
    COOKING = "cooking"
    FISHING = "fishing"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    MINING = "mining"
    WEAPONCRAFTING = "weaponcrafting"
    WOODCUTTING = "woodcutting"

    def __str__(self) -> str:
        return str(self.value)
