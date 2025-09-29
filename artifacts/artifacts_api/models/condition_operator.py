from enum import Enum

class ConditionOperator(str, Enum):
    EQ = "eq"
    GT = "gt"
    LT = "lt"
    NE = "ne"

    def __str__(self) -> str:
        return str(self.value)
