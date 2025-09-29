from enum import Enum

class CharacterSkin(str, Enum):
    CORRUPTED1 = "corrupted1"
    MEN1 = "men1"
    MEN2 = "men2"
    MEN3 = "men3"
    WOMEN1 = "women1"
    WOMEN2 = "women2"
    WOMEN3 = "women3"
    ZOMBIE1 = "zombie1"

    def __str__(self) -> str:
        return str(self.value)
