from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .main import Character


@dataclass
class Task:
    """Одна задача в очереди персонажа."""

    title: str
    run: Callable[[], TaskPlan | None]


@dataclass
class TaskPlan:
    """План постановки следующих задач после выполнения текущей."""

    top: list[Task] | None = None
    back: list[Task] | None = None


def drop_bank(character: Character) -> Task:
    """Задача для сброса всего инвентаря в банк."""

    return_position = character.params.get("map_id")

    def _run() -> TaskPlan | None:
        character.move(334)
        character.bank("all", quantity=0, action="deposit")
        character.move(return_position)
        return None

    return Task(
        title="Сброс инвентаря в банк",
        run=_run,
    )


def gather(
    character: Character,
    map_id: int,
    quantity: int,
) -> Task:
    """Создаёт возобновляемую задачу добычи с корректной очередью при полном инвентаре."""

    remaining = max(quantity, 0)
    task: Task

    def _run() -> TaskPlan | None:
        nonlocal remaining

        if remaining <= 0:
            return None

        if character.params.get("map_id") != map_id:
            character.move(map_id)

        error = character.gathering()
        if error == 497:
            return TaskPlan(top=[drop_bank(character), task])

        remaining -= 1
        if remaining > 0:
            return TaskPlan(top=[task])

        return None

    task = Task(
        title=f"Добыть {quantity} ресурса на карте {map_id}",
        run=_run,
    )
    return task
