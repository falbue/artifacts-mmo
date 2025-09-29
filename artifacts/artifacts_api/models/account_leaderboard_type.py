from enum import Enum

class AccountLeaderboardType(str, Enum):
    ACHIEVEMENTS_POINTS = "achievements_points"
    GOLD = "gold"

    def __str__(self) -> str:
        return str(self.value)
