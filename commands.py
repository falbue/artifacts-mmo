from send_request import *
from translate_data import *
import time
from plyer import notification
from tg_notif import *

name = 'Falbue'


# data = send_request('maps/2/0')  # получение инофрмации о карте
# data = send_request('items')  # получение инофрмации о предметах
# data = send_request(f'my/{name}/action/rest')  # лечение
# data = send_request("my/Falbue/action/move", {"x":2,"y":0})  # перемещение персонажа
# data = send_request("my/Falbue/action/fight", True) # бой
# data = send_request("my/Falbue/action/gathering", True) # добыча
# data = send_request("my/Falbue/action/crafting", {'code':'copper', "quantity": 2}) # крафт
# data = send_request('characters/Falbue')  # получение инофрмации о персонаже

# обработка данных
# print(data)
# print_data(data)
# print_data(data['Инвентарь'])

i = 0
notification.notify(title='Начата добыча меди', message='Медь добывается', timeout=10)
while i != 24 - 11:
    data = send_request("my/Falbue/action/gathering", True) # добыча
    time.sleep(25)
    i+=1
    print(f"Добыто {i} меди")
    
notification.notify(title='Задача выполнена!', message='Ресурс добыт', timeout=10)
tg_notif("Ресурс добыт")