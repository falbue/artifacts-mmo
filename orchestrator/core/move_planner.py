from orchestrator.models.task import Task, TaskType
from orchestrator.utils.logger import setup_logger

log = setup_logger("MOVE_PLANNER")


class MovePlanner:
    def __init__(self, api_client):
        self.client = api_client

    async def enrich_tasks(
        self, tasks: list[Task], character_current_map: int
    ) -> list[Task]:
        """Поиск и нахождение оптимальной точки на карте, для выполнения задачи

        Args:
            tasks (list[Task]): Список задач
            character_current_map (int): Текущее местоположение персонажа

        Returns:
            list[Task]: Возвращает новый список задач, с дополнительными перемещениями
        """
        enriched = []
        current_map = character_current_map

        for task in tasks:
            maps = await self._get_target_map(task)
            target_map = min(maps, key=lambda x: abs(x - current_map)) if maps else None

            if target_map is None:
                log.error(f"Карта для задачи {task} не найдена")
                raise

            if target_map is not None and target_map != current_map:
                move_task = Task(
                    type=TaskType.MOVE,
                    resource=f"move_to_{target_map}",
                    target_location=target_map,
                    quantity_total=1,
                    assignee_class=task.assignee_class,
                )
                enriched.append(move_task)
                task.blocked_by.append(move_task.id)
                current_map = target_map

            enriched.append(task)

        return enriched

    async def _get_target_map(self, task: Task) -> list[int]:
        """Узнать на какой карте нужно выполнять задачу"""
        mapping = {
            "lumberjack": "woodcutting",
            "miner": "mining",
        }

        if task.assignee_class is None:
            log.warning(f"Отсутствует класс для задачи {task}")
            return []

        if task.type == TaskType.DEPOSIT or task.type == TaskType.WITHDRAW:
            return [334]

        if task.type == TaskType.CRAFT:
            content_code = mapping.get(task.assignee_class)
            print(task.assignee_class, content_code)
            maps = await self.client.get(
                "/maps",
                params={
                    "content_type": "workshop",
                    "content_code": content_code,
                },
            )
            map_ids = [
                map_info.get("map_id")
                for map_info in maps["data"][0]
                if map_info.get("map_id")
            ]
            return map_ids

        if task.type == TaskType.GATHER:
            resource = await self.client.get(
                "/resources", params={"drop": task.resource}
            )
            maps = await self.client.get(
                "/maps", params={"content_code": resource["data"][0].get("code")}
            )

            map_ids = [
                map_info.get("map_id")
                for map_info in maps["data"]
                if map_info.get("map_id")
            ]
            return map_ids

        return []
