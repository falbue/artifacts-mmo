from enum import Enum

class CharacterLeaderboardType(str, Enum):
    ALCHEMY = "alchemy"
    COMBAT = "combat"
    COOKING = "cooking"
    FISHING = "fishing"
    GEARCRAFTING = "gearcrafting"
    JEWELRYCRAFTING = "jewelrycrafting"
    MINING = "mining"
    WEAPONCRAFTING = "weaponcrafting"
    WOODCUTTING = "woodcutting"

    def __str__(self) -> str:
        return str(self.value)
