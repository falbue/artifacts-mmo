from enum import Enum

class AccountStatus(str, Enum):
    FOUNDER = "founder"
    GOLD_FOUNDER = "gold_founder"
    STANDARD = "standard"
    VIP_FOUNDER = "vip_founder"

    def __str__(self) -> str:
        return str(self.value)
