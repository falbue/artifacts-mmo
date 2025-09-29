from enum import Enum

class AchievementType(str, Enum):
    COMBAT_DROP = "combat_drop"
    COMBAT_KILL = "combat_kill"
    COMBAT_LEVEL = "combat_level"
    CRAFTING = "crafting"
    GATHERING = "gathering"
    OTHER = "other"
    RECYCLING = "recycling"
    TASK = "task"
    USE = "use"

    def __str__(self) -> str:
        return str(self.value)
