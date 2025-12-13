from datetime import datetime
import json
from .utils.request import request_mmo as request
import os


def update_elements(element: str, filename: str = "") -> dict:
    """
    Обновляет данные из API и сохраняет их в JSON-файл
    """
    if filename is None:
        filename = element

    data = []
    initial_data = request(f"/{element}?size=100")
    pages = initial_data["pages"]

    for i in range(pages):
        command = f"/{element}?size=100&page={i + 1}"
        page_data = request(command)
        data.extend(page_data["data"])

    data = {"data": data}

    data_dir = os.path.join(os.path.dirname(__file__), "data")
    os.makedirs(data_dir, exist_ok=True)

    file_path = os.path.join(data_dir, f"{filename}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return data


def get_elements(element: str, ttl_seconds: int = 0) -> dict:
    """
    Возвращает актуальные данные: либо из файла, либо обновлённые, если срок истёк.
    """
    file_path = os.path.join(os.path.dirname(__file__), "data", f"{element}.json")

    if os.path.exists(file_path):
        mod_time = os.path.getmtime(file_path)
        mod_datetime = datetime.fromtimestamp(mod_time)
        now = datetime.now()

        if (now - mod_datetime).total_seconds() < ttl_seconds or ttl_seconds == 0:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)

    if element == "npcs_items":
        filename = element
        element = "npcs/items"
    else:
        filename = ""

    return update_elements(element, filename)


def find_map_elements(code: str):
    elements = get_elements("maps")["data"]
    data = []
    for map_chunk in elements:
        if map_chunk["interactions"].get("content"):
            if map_chunk["interactions"]["content"].get("code") == code:
                data.append(
                    {
                        "map_id": map_chunk.get("map_id"),
                        "x": map_chunk.get("x"),
                        "y": map_chunk.get("y"),
                    }
                )
    return data


def get_resource(name: str = ""):
    data = get_elements("resources")["data"]
    for resource in data:
        if resource.get("name") == name or resource.get("code") == name:
            return resource
    return None


def get_item(name: str):
    data = get_elements("items")["data"]
    for item in data:
        if item.get("name") == name or item.get("code") == name:
            return item
    return None


def get_npcs_item(name: str):
    data = get_elements("npcs_items")["data"]
    for npc in data:
        if npc.get("name") == name or npc.get("code") == name:
            return npc
    return None


def get_sell_orders(size: int = 100, page: int = 1):
    data = request(f"/grandexchange/orders?size={size}&page={page}")
    return data


def get_sell_order(order_id: int):
    data = request(f"/grandexchange/orders/{order_id}")
    return data
