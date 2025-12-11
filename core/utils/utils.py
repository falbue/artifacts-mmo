import json
from .logger import setup

logger = setup(__name__)


def print_json(data):  # удобный вывод json
    try:
        if isinstance(data, (dict, list)):
            text = json.dumps(data, indent=4, ensure_ascii=False)
        else:
            print(type(data))
            text = str(data)
        print(text)
    except Exception as e:
        logger.error(f"Ошибка при выводе json: {e}")
