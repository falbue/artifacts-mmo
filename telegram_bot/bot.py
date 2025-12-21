import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import TelegramTextApp
from TelegramTextApp.TTA import send_menu  # type: ignore
from core import elements
from core.accounts import get_account


def grand_items(tta):
    data = elements.get_sell_orders()
    items = data.get("data", [])
    keyboard = {}
    for item in items:
        keyboard[f"sell|{item['id']}"] = f"{item['code']} {item['price']}"
    return keyboard


def sell_order(tta):
    data = elements.get_sell_order(tta.order_id)
    return data["data"]


def account_info(tta):
    data = get_account(tta.account)
    return data["data"]


def test(tta):
    send_menu("account|Falbue", "user")


if __name__ == "__main__":
    TelegramTextApp.start()  # type: ignore
