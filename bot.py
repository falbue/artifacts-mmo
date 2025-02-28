import re
from artifactsmmo import mmo_request

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImN5YW5zYWlyMDVAZ21haWwuY29tIiwicGFzc3dvcmRfY2hhbmdlZCI6IiJ9.lbDwAlICwQJYUX2kGjRqBPra0Uv7NbYUcZhXRP7nt0I"

def markdown(text, full=False):  # экранирование
    if full == True: special_characters = r'*|~[]()>#+-=|{}._!'
    else: special_characters = r'>#+-={}.!'
    escaped_text = ''
    for char in text:
        if char in special_characters:
            escaped_text += f'\\{char}'
        else:
            escaped_text += char
    return escaped_text

def formating_text(tta_data, text):        
    format_dict = {}
    if tta_data["name"] == "character":
        callback = mmo_request(character=tta_data['data'], command="character_info", body=None)
        format_dict = callback["data"]

    if tta_data["name"] == "move":
        body_elements = [element.strip() for element in tta_data["data"].split(",")]
        callback = mmo_request(command=f"maps/{body_elements[0]}/{body_elements[1]}")
        url = (f'https://www.artifactsmmo.com/images/maps/{callback["data"]["Внешность"]}.png')
        # url = markdown(url, True)
        format_dict = {"map_url": url}

    try:
        input_text = tta_data["data"].split(":")[1]
        formatted_text = text.format_map(
            {key: format_dict.get(key, None) for key in re.findall(r'\{(.*?)\}', text)}
        )
    except Exception as e:
        formatted_text = text.format_map(
            {key: format_dict.get(key, None) for key in re.findall(r'\{(.*?)\}', text)}
        )

    return formatted_text

def maps_objects(tta_data):
    callback = mmo_request(token=token, command="maps_resource", body=None)["data"]
    buttons = {}
    for maps_object in callback:
        buttons[f"move:{maps_object['x']}, {maps_object['y']}"] = maps_object["Внешность"]
    return buttons

def characters(tta_data):
    callback = mmo_request(token=token, command="my_characters", body=None)
    callback = callback["data"][0]

    buttons = {}
    for _ in callback:
        name = callback["Имя"]
        buttons[f"character:{name}"] = name
    return buttons

def move_character(tta_data):
    body = tta_data['data']
    callback = mmo_request(character="Falbue", token=token, command="move", body=body)

def gathering(tta_data):
    callback = mmo_request(character="Falbue", token=token, command="gathering", body=True)
    if isinstance(callback, dict):
        text = callback['data']["details"]['Опыт']
        text = f"Получено опыта {text}"
    else:
        text = callback
    return text


if __name__ == "__main__":
    from TelegramTextApp import TTA
    TTA.start("7769748297:AAHmSJlaHjAzs2ZAMGqg9IzARIDWcKS7lbE", "menus", debug=True, tta_experience=True, formating_text="formating_text")