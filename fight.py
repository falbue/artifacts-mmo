from send_request import *
import time
from plyer import notification
from tg_notif import *
from fight import *

def fight(name, time_work=None):
	i = 0
	notification.notify(title='Задача запущена!', message='Бой начался', timeout=10)
	while i != time_work:
	    data = send_request(f'my/{name}/action/rest', True)  # лечение
	    x = data['Кулдаун']["Всего секунд"]
	    time.sleep(x)
	    data = send_request("my/Falbue/action/fight", True) # бой
	    x = data['Кулдаун']["Всего секунд"]
	    time.sleep(x)
	    i+=1
	    print(f"Бой {i} закончен")
    
	notification.notify(title='Задача выполнена!', message='Бой закончен!', timeout=10)
	tg_notif("Бой закончен!")