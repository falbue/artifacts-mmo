import json

from orchestrator.utils import config
from orchestrator.utils.logger import setup_logger

log = setup_logger("UTILS", config.LOG_PATH, config.LOG_LEVEL)


def check_gather(response: dict, item_code: str) -> int:
    """
    Проверить, был ли успешный gather.

    Returns:
        True если gather успешен, False если нет.
    """

    if response.get("details", {}).get("items"):
        for item in response["details"]["items"]:
            if item.get("code") == item_code:
                return item.get("quantity", 0)

    return 0


def print_json(data: dict):
    print(json.dumps(data, indent=2))
