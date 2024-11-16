from send_request import *
from translate_data import *


data = send_request('characters/Falbue')  # получение инофрмации о персонаже
# data = send_request("my/Falbue/action/move", {"x":0,"y":1})  # перемещение персонажа
# data = send_request("my/Falbue/action/fight", True) # бой
# data = send_request("my/Falbue/action/gathering", True) # добыча

# обработка данных
print(data)
print_data(data["Инвентарь"])