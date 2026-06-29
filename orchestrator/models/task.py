from dataclasses import dataclass, field
from enum import Enum
import uuid


class TaskType(Enum):
    """Типы задач."""

    GATHER = "gather"
    CRAFT = "craft"
    MOVE = "move"
    COMBAT = "combat"
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class TaskStatus(Enum):
    """Статусы выполнения."""

    PENDING = "pending"
    READY = "ready"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"


@dataclass
class Task:
    """Единица работы в системе."""

    type: TaskType
    resource: str
    quantity_total: int

    # Опциональные поля
    id: str = field(default_factory=lambda: str(uuid.uuid4())[:8])
    quantity_done: int = 0
    priority: int = 0
    status: TaskStatus = TaskStatus.PENDING
    blocked_by: list[str] = field(default_factory=list)
    target_location: int | None = None  # для MOVE задач (map_id)
    assignee_class: str | None = None  # "Miner", "Gardener"
    assignee_id: str | None = None  # имя персонажа которому назначена задача

    def __str__(self):
        return f"[{self.id}] {self.type.value} {self.resource} ({self.quantity_done}/{self.quantity_total}) priority={self.priority}"

    def is_ready(self) -> bool:
        """Задача готова если нет блокирующих её задач."""
        return not self.blocked_by and self.status == TaskStatus.PENDING

    def is_done(self) -> bool:
        """Задача завершена если выполнено нужное количество."""
        return self.quantity_done >= self.quantity_total
