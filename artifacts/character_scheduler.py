import threading
import queue
from typing import Dict, Callable, Optional, List
import traceback
import inspect

from .instructions import *
from .commands import load_characters  # Импортируем load_characters

# Словарь очередей действий для каждого персонажа
_character_queues: Dict[str, queue.PriorityQueue] = {}
_character_threads: Dict[str, threading.Thread] = {}
_active_tasks: Dict[str, 'PrioritizedAction'] = {}
_active_tasks_lock = threading.Lock()


class PrioritizedAction:
    def __init__(self, priority: int, func: Callable, args, kwargs, task_id: str):
        self.priority = priority
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.task_id = task_id
        self.cancelled = False
        self._index = PrioritizedAction._counter
        PrioritizedAction._counter += 1

    def __lt__(self, other):
        if self.priority != other.priority:
            return self.priority < other.priority
        return self._index < other._index

    _counter = 0


def _worker(character: str):
    """Рабочий поток для выполнения действий персонажа по приоритету."""
    q = _character_queues[character]
    while True:
        item = q.get()
        if item is None:  # Сигнал остановки
            break

        with _active_tasks_lock:
            if item.task_id in _active_tasks and _active_tasks[item.task_id].cancelled:
                q.task_done()
                continue

        try:
            item.func(*item.args, **item.kwargs)
        except Exception as e:
            # Получаем информацию о месте возникновения ошибки
            tb = traceback.extract_tb(e.__traceback__)
            frame = tb[-1]  # Последний фрейм — место, где произошла ошибка
            filename = frame.filename
            line_number = frame.lineno
            print(f"Ошибка в действии {item.task_id}: {e} | Файл: {filename}, строка: {line_number}")
        finally:
            q.task_done()


def enqueue_character_action(
    func: Callable,
    character: str,
    *args,
    priority: int = 0,
    task_id: Optional[str] = None,
    wait_action: bool = False,
    return_id: bool = False,
    **kwargs
):
    """
    Добавляет действие в очередь персонажа(ей) с приоритетом.
    Поддерживает "all", индекс или имя персонажа.
    """
    characters = load_characters(character)

    task_ids = []

    for char in characters:
        name = char["name"]  # Предполагаем, что load_characters возвращает словарь с "name"

        with _active_tasks_lock:
            if name not in _character_queues:
                _character_queues[name] = queue.PriorityQueue()
                t = threading.Thread(target=_worker, args=(name,), daemon=True)
                _character_threads[name] = t
                t.start()

        # Генерация ID
        if task_id is None:
            task_id_gen = f"{func.__name__}_{name}_{PrioritizedAction._counter}"
        else:
            task_id_gen = f"{task_id}_{name}"

        action = PrioritizedAction(priority, func, (char,) + args, kwargs, task_id_gen)

        with _active_tasks_lock:
            _active_tasks[task_id_gen] = action

        _character_queues[name].put(action)
        task_ids.append(task_id_gen)

        if wait_action:
            _character_queues[name].join()

    # Возвращаем ID, если нужно
    if return_id:
        return task_ids[0] if len(task_ids) == 1 else task_ids
    return None


def cancel_action(task_id: str):
    """Отменяет задачу по ID."""
    with _active_tasks_lock:
        if task_id in _active_tasks:
            _active_tasks[task_id].cancelled = True
            del _active_tasks[task_id]


def move_task_to_top(task_id: str):
    """Поднимает задачу в начало очереди персонажа (с наивысшим приоритетом)."""
    with _active_tasks_lock:
        if task_id in _active_tasks:
            action = _active_tasks[task_id]
            action.priority = -100000


def move_task_to_bottom(task_id: str):
    """Опускает задачу в конец очереди персонажа (с низшим приоритетом)."""
    with _active_tasks_lock:
        if task_id in _active_tasks:
            action = _active_tasks[task_id]
            action.priority = 100000


def list_tasks(character: Optional[str] = None) -> List[str]:
    """Возвращает список task_id задач, подходящих под фильтр."""
    with _active_tasks_lock:
        result = []
        for task_id, action in _active_tasks.items():
            if action.cancelled:
                continue
            if character and action.args[0]["name"] != character:
                continue
            result.append(task_id)
        return result


def wait_for_character(character: str):
    """Ждёт завершения всех действий для указанного персонажа."""
    if character in _character_queues:
        _character_queues[character].join()


def wait_for_all():
    """Ждёт завершения всех действий для всех персонажей."""
    for q in _character_queues.values():
        q.join()