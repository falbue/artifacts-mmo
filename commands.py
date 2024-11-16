from send_request import *
from translate_data import *


# data = send_request('characters/Falbue')  # получение инофрмации о персонаже
data = send_request('maps/0/1')  # получение инофрмации о карте
# data = send_request("my/Falbue/action/move", {"x":0,"y":1})  # перемещение персонажа
# data = send_request("my/Falbue/action/fight", True) # бой
# data = send_request("my/Falbue/action/gathering", True) # добыча
# data = send_request("my/Falbue/action/crafting", True) # крафт
# data = send_request("my/Falbue/action/gathering", True) # Добыча

# обработка данных
print_data(data)