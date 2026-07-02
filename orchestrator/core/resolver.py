import networkx as nx
from orchestrator.core.move_planner import MovePlanner
from orchestrator.models.task import Task, TaskType
from orchestrator.utils.logger import setup_logger

log = setup_logger("RESOLVER")

WORKSHOPS = {
    "mining": "miner",
    "woodcutting": "lumberjack",
}


class DependencyResolver:
    """
    Разбирает цель (достижение) на дерево задач с зависимостями.

    Создаёт только логические задачи (GATHER, CRAFT, COMBAT, DEPOSIT, WITHDRAW).
    MOVE задачи добавляет MovePlanner отдельно.
    """

    def __init__(self, api_client):
        self.client = api_client
        self.graph = nx.DiGraph()
        self.all_tasks: dict[str, Task] = {}
        self.move_planner = MovePlanner(api_client)

    async def resolve(self, goal: dict) -> list[Task]:
        """
        Разобрать цель на список задач.

        Args:
            goal: {
                "type": "craft",  # или "gather", "combat"
                "item": "health_potion",
                "quantity": 5
            }

        Returns:
            Список Task отсортированный по приоритету
        """
        self.all_tasks.clear()
        self.graph.clear()

        log.info(f"Разбор цели: {goal}")

        goal_type = goal.get("type", "craft")

        if goal_type == "craft":
            root_task = Task(
                type=TaskType.CRAFT,
                resource=goal["item"],
                quantity_total=goal["quantity"],
            )
        elif goal_type == "gather":
            root_task = Task(
                type=TaskType.GATHER,
                resource=goal["item"],
                quantity_total=goal["quantity"],
            )
        else:
            raise ValueError(f"Неизвестный тип цели: {goal_type}")

        await self._decompose(root_task, parent=None)

        self._calculate_priorities()

        tasks_list = sorted(self.all_tasks.values(), key=lambda t: (-t.priority, t.id))

        log.info(f"Разобрано {len(tasks_list)} задач")
        return tasks_list

    async def _decompose(self, task: Task, parent: Task | None):
        """
        Рекурсивно разбивает задачу на подзадачи
        """
        if not task.assignee_class:
            task.assignee_class = await self._get_assignee_class(task)
        self.all_tasks[task.id] = task

        if parent:
            # Добавить зависимость: эта задача разблокирует parent
            self.graph.add_edge(task.id, parent.id)
            if task.id not in parent.blocked_by:
                parent.blocked_by.append(task.id)

        # Получить требования для этой задачи
        requirements = await self._get_requirements(task)

        # Рекурсивно разобрать каждое требование
        for req_task in requirements:
            if req_task.id not in self.all_tasks:
                await self._decompose(req_task, parent=task)

    async def _get_requirements(self, task: Task) -> list[Task]:
        """
        Определить что нужно для выполнения задачи.
        """
        requirements = []

        if task.type == TaskType.CRAFT:
            # Получить рецепт с API
            recipe = await self.client.get(f"/items/{task.resource}")
            recipe = recipe.get("data", {}).get("craft")
            if recipe is None:
                log.warning(f"Нет рецепта для {task.resource}")
                return []

            for ingredient in recipe.get("items", []):
                qty_needed = ingredient["quantity"] * task.quantity_total

                # Проверить есть ли уже в банке
                # TODO: проверить в банке

                task_type = await self.client.get(f"/items/{ingredient['code']}")
                if task_type.get("craft"):
                    req_task = Task(
                        type=TaskType.CRAFT,
                        resource=ingredient["code"],
                        quantity_total=qty_needed,
                    )
                    req_task.assignee_class = await self._get_assignee_class(req_task)
                else:
                    req_task = Task(
                        type=TaskType.GATHER,
                        resource=ingredient["code"],
                        quantity_total=qty_needed,
                    )
                    req_task.assignee_class = await self._get_assignee_class(req_task)
                requirements.append(req_task)

        elif task.type == TaskType.GATHER:
            # Для GATHER может потребоваться инструмент
            # TODO: проверить нужен ли инструмент
            # Если нужен и его нет — создать задачу на крафт инструмента
            # Бывает добыча ресурса через бой

            req_task = Task(
                type=TaskType.CRAFT,
                resource=task.resource,
                quantity_total=task.quantity_total,
            )
            req_task.assignee_class = await self._get_assignee_class(req_task)

        elif task.type == TaskType.COMBAT:
            # COMBAT обычно не имеет зависимостей
            # Но может потребоваться лучшее оружие
            # TODO: проверить оружие
            pass

        return requirements

    async def _get_assignee_class(self, task: Task) -> str:
        """Определить какой класс будет выполнять задачу."""
        mapping = {
            "woodcutting": "lumberjack",
            "mining": "miner",
        }
        if task.type == TaskType.CRAFT:
            craft_data = await self.client.get(f"/items/{task.resource}")
            craft = craft_data.get("data", {}).get("craft")
            if craft is None:
                role = craft_data.get("data", {}).get("subtype")
            else:
                role = craft_data.get("data", {}).get("craft").get("skill")

        elif task.type == TaskType.GATHER:
            resource_data = await self.client.get(
                "/resources", params={"drop": task.resource}
            )
            role = resource_data["data"][0].get("skill")
        else:
            role = "Unknown"

        if role == "Unknown":
            log.warning(f"Неизвестный класс для задачи {task}")
        return mapping.get(role, "Unknown")

    def _calculate_priorities(self):
        """
        Приоритет = сколько задач зависит (транзитивно) от этой.
        Используем networkx для поиска descendants.
        """
        # Сначала убедиться что все задачи в графе
        for task_id in self.all_tasks:
            if not self.graph.has_node(task_id):
                self.graph.add_node(task_id)

        # Теперь считать приоритеты
        for task_id in self.all_tasks:
            descendants = len(nx.descendants(self.graph, task_id))
            self.all_tasks[task_id].priority = descendants

            # Если нет descendants — это листовая задача
            if descendants == 0:
                self.all_tasks[task_id].priority = 1000
