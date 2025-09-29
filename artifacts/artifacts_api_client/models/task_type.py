from enum import Enum

class TaskType(str, Enum):
    ITEMS = "items"
    MONSTERS = "monsters"

    def __str__(self) -> str:
        return str(self.value)
