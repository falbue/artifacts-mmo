from enum import Enum

class MapContentType(str, Enum):
    BANK = "bank"
    GRAND_EXCHANGE = "grand_exchange"
    MONSTER = "monster"
    NPC = "npc"
    RESOURCE = "resource"
    TASKS_MASTER = "tasks_master"
    WORKSHOP = "workshop"

    def __str__(self) -> str:
        return str(self.value)
