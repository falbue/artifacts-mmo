from enum import Enum

class ActionType(str, Enum):
    BUY_BANK_EXPANSION = "buy_bank_expansion"
    BUY_GE = "buy_ge"
    BUY_NPC = "buy_npc"
    CANCEL_GE = "cancel_ge"
    CHANGE_SKIN = "change_skin"
    CHRISTMAS_EXCHANGE = "christmas_exchange"
    CRAFTING = "crafting"
    DELETE_ITEM = "delete_item"
    DEPOSIT_GOLD = "deposit_gold"
    DEPOSIT_ITEM = "deposit_item"
    EQUIP = "equip"
    FIGHT = "fight"
    GATHERING = "gathering"
    GIVE_GOLD = "give_gold"
    GIVE_ITEM = "give_item"
    MOVEMENT = "movement"
    RECYCLING = "recycling"
    RENAME = "rename"
    REST = "rest"
    SELL_GE = "sell_ge"
    SELL_NPC = "sell_npc"
    TASK = "task"
    UNEQUIP = "unequip"
    USE = "use"
    WITHDRAW_GOLD = "withdraw_gold"
    WITHDRAW_ITEM = "withdraw_item"

    def __str__(self) -> str:
        return str(self.value)
