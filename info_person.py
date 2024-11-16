
from send_request import send_request

# ПЕРЕМЕННЫЕ----------------------------
data = send_request(request = "characters/Falbue")

# Перевод ключей на русский
translations = {
    'name': 'Имя',
    'skin': 'Внешность',
    'level': 'Уровень',
    'xp': 'Опыт',
    'max_xp': 'Максимум опыта',
    'total_xp': 'Общий опыт',
    'gold': 'Золото',
    'speed': 'Скорость',
    'mining_level': 'Уровень добычи',
    'mining_xp': 'Опыт добычи',
    'mining_max_xp': 'Максимум опыта добычи',
    'woodcutting_level': 'Уровень рубки',
    'woodcutting_xp': 'Опыт рубки',
    'woodcutting_max_xp': 'Максимум опыта рубки',
    'fishing_level': 'Уровень рыбалки',
    'fishing_xp': 'Опыт рыбалки',
    'fishing_max_xp': 'Максимум опыта рыбалки',
    'weaponcrafting_level': 'Уровень ковки оружия',
    'weaponcrafting_xp': 'Опыт ковки оружия',
    'weaponcrafting_max_xp': 'Максимум опыта ковки оружия',
    'gearcrafting_level': 'Уровень ковки снаряжения',
    'gearcrafting_xp': 'Опыт ковки снаряжения',
    'gearcrafting_max_xp': 'Максимум опыта ковки снаряжения',
    'jewelrycrafting_level': 'Уровень ювелирного дела',
    'jewelrycrafting_xp': 'Опыт ювелирного дела',
    'jewelrycrafting_max_xp': 'Максимум опыта ювелирного дела',
    'cooking_level': 'Уровень кулинарии',
    'cooking_xp': 'Опыт кулинарии',
    'cooking_max_xp': 'Максимум опыта кулинарии',
    'hp': 'Здоровье',
    'haste': 'Поспешность',
    'critical_strike': 'Критический удар',
    'stamina': 'Выносливость',
    'attack_fire': 'Атака огнем',
    'attack_earth': 'Атака землей',
    'attack_water': 'Атака водой',
    'attack_air': 'Атака воздухом',
    'dmg_fire': 'Урон огнем',
    'dmg_earth': 'Урон землей',
    'dmg_water': 'Урон водой',
    'dmg_air': 'Урон воздухом',
    'res_fire': 'Сопротивление огню',
    'res_earth': 'Сопротивление земле',
    'res_water': 'Сопротивление воде',
    'res_air': 'Сопротивление воздуху',
    'x': 'Координата X',
    'y': 'Координата Y',
    'cooldown': 'Перезарядка',
    'cooldown_expiration': 'Окончание перезарядки',
    'weapon_slot': 'Оружие',
    'shield_slot': 'Щит',
    'helmet_slot': 'Шлем',
    'body_armor_slot': 'Броня',
    'leg_armor_slot': 'Набедренники',
    'boots_slot': 'Ботинки',
    'ring1_slot': 'Кольцо 1',
    'ring2_slot': 'Кольцо 2',
    'amulet_slot': 'Амулет',
    'artifact1_slot': 'Артефакт 1',
    'artifact2_slot': 'Артефакт 2',
    'artifact3_slot': 'Артефакт 3',
    'consumable1_slot': 'Расходник 1',
    'consumable1_slot_quantity': 'Количество расходника 1',
    'consumable2_slot': 'Расходник 2',
    'consumable2_slot_quantity': 'Количество расходника 2',
    'task': 'Задача',
    'task_type': 'Тип задачи',
    'task_progress': 'Прогресс задачи',
    'task_total': 'Всего задач',
    'inventory_max_items': 'Максимум предметов в инвентаре',
    'inventory': 'Инвентарь'
}

# Функция для перевода данных на русский
def translate_data(data, translations):
    if isinstance(data, list):
        return [translate_data(item, translations) for item in data]
    elif isinstance(data, dict):
        return {translations.get(k, k): translate_data(v, translations) for k, v in data.items()}
    else:
        return data

translated_data = translate_data(data, translations)

# Функция для красивого вывода данных
def print_data(data):
    for key, value in data.items():
        if isinstance(value, list):
            print(f"\n{key}:")
            for item in value:
                print(f"  {item}")
        else:
            print(f"{key}: {value}")

# Вывод основных данных персонажа
print("Основные данные персонажа:")
print(translated_data)
print_data({k: v for k, v in translated_data['data'].items() if k != 'Инвентарь'})

# Вывод инвентаря
print_data({'Инвентарь': translated_data['data']['Инвентарь']})
