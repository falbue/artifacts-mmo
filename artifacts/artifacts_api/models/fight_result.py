from enum import Enum

class FightResult(str, Enum):
    LOSS = "loss"
    WIN = "win"

    def __str__(self) -> str:
        return str(self.value)
