from send_request import *
import time
from plyer import notification
from tg_notif import *
from fight import *

name = 'Falbue'


# data = send_request('maps')  # получение инофрмации о всей карте
# data = send_request('maps/2/0')  # получение инофрмации о карте
# data = send_request('items')  # получение инофрмации о предметах
# data = send_request('items/wooden_shield')  # получение инофрмации об указаном предмете
# data = send_request(f'my/{name}/action/rest', True)  # лечение
# data = send_request("my/Falbue/action/move", {"x":5,"y":1})  # перемещение персонажа
# data = send_request("my/Falbue/action/fight", True) # бой
# data = send_request("my/Falbue/action/gathering", True) # добыча
# data = send_request("my/Falbue/action/crafting", {'code':'ash_plank', "quantity": 1}) # крафт
# data = send_request(f'my/{name}/action/equip', {"code": "copper_ring", "slot": "ring1", "quantity": 1})  # надеть предмет
# data = send_request(f'my/{name}/action/equip', {"slot": "weapon", "quantity": 1})  # снять предмет
data = send_request(f'my/{name}/action/grandexchange/sell', {"code": "yellow_slimeball", "quantity": 60, "price": 100})  # Создать сделку

# обработка данных
# print(data)
# data = send_request('characters/Falbue')  # получение инофрмации о персонаже
print_data(data)
# print_data(data["Инвентарь"])

# i = 0
# notification.notify(title='Начата добыча', message='Ресурс добывается!', timeout=10)
# while i != 5*8:
#     data = send_request("my/Falbue/action/gathering", True) # добыча
#     time.sleep(25)
#     i+=1
#     print(f"Добыто {i} ресурса")
     
# notification.notify(title='Задача выполнена!', message='Ресурс добыт', timeout=10)

# fight(name)