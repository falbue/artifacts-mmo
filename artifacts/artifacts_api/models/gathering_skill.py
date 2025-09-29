from enum import Enum

class GatheringSkill(str, Enum):
    ALCHEMY = "alchemy"
    FISHING = "fishing"
    MINING = "mining"
    WOODCUTTING = "woodcutting"

    def __str__(self) -> str:
        return str(self.value)
