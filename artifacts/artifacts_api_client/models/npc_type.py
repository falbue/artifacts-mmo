from enum import Enum

class NPCType(str, Enum):
    MERCHANT = "merchant"
    TRADER = "trader"

    def __str__(self) -> str:
        return str(self.value)
