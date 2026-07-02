import asyncio
from orchestrator.utils.logger import setup_logger

log = setup_logger("TASK_MANAGER")


class TaskManager:
    """
    Оркестратор системы.

    Связывает все компоненты:
    - Scheduler (распределение)
    - Runner (выполнение)
    - DependencyResolver (разбор целей)
    - MovePlanner (добавление MOVE)
    - AchievementPlanner (выбор целей)
    """

    def __init__(
        self, characters, scheduler, resolver, move_planner, achievement_planner
    ):
        self.characters = characters
        self.scheduler = scheduler
        self.resolver = resolver
        self.move_planner = move_planner
        self.achievement_planner = achievement_planner

    async def execute_goal(self, goal: dict, character=None):
        """
        Выполнить одну цель.

        Args:
            goal: {
                "type": "craft" | "gather" | "combat",
                "item": "health_potion",
                "quantity": 5
            }
            character: если None — используется первый доступный персонаж
        """
        if character is None:
            character = self.characters[0]  # или выбрать по логике

        log.info(f"Выполнение цели: {goal}")

        try:
            # 1. Resolver создаёт логические задачи
            tasks = await self.resolver.resolve(goal)

            # 2. MovePlanner добавляет MOVE задачи
            tasks = await self.move_planner.enrich_tasks(
                tasks, character_current_map=character.map_id
            )

            log.info(f"Создано {len(tasks)} задач")

            # 3. Добавить в scheduler
            self.scheduler.add_tasks(tasks)

            # 4. Ждать выполнения
            await self._wait_all_tasks_done(tasks)

            log.info(f"Goal completed: {goal}")

        except Exception as e:
            log.error(f"Ошибка в выполнении цели: {e}")
            raise

    async def _wait_all_tasks_done(self, tasks: list) -> bool:
        """
        Ждать пока все задачи завершатся.

        Returns:
            True если все завершились успешно
            False если какая-то упала
        """
        task_ids = {t.id for t in tasks}

        while True:
            # Проверить статус всех задач
            all_done = all(
                self.scheduler.all_tasks[tid].status.value in ["done", "failed"]
                for tid in task_ids
                if tid in self.scheduler.all_tasks
            )

            if all_done:
                # Проверить есть ли failed
                failed = [
                    self.scheduler.all_tasks[tid]
                    for tid in task_ids
                    if tid in self.scheduler.all_tasks
                    and self.scheduler.all_tasks[tid].status.value == "failed"
                ]

                if failed:
                    log.error(f"Some tasks failed: {failed}")
                    return False

                log.info("All tasks completed successfully")
                return True

            await asyncio.sleep(1)

    async def start_season(self):
        """
        Основной сезонный цикл (для автоматического выполнения достижений).

        Опционально — если используется achievement_planner.
        """
        await self.achievement_planner.load_achievements()

        while True:
            achievement = self.achievement_planner.get_next_achievement()

            if not achievement:
                log.info("All achievements completed!")
                break

            log.info(f"Working on achievement: {achievement['name']}")

            goal = {
                "type": achievement.get("type", "craft"),
                "item": achievement["code"],
                "quantity": achievement.get("target_qty", 1),
            }

            success = await self.execute_goal(goal)

            if success:
                self.achievement_planner.mark_as_completed(achievement["id"])

    def get_system_status(self) -> dict:
        """Статистика по системе."""
        return {
            "characters": [
                {
                    "name": c.name,
                    "current_task": self.scheduler.get_character_task(c.name),
                    "cooldown": c.get_cooldown_remaining()
                    if hasattr(c, "get_cooldown_remaining")
                    else 0,
                }
                for c in self.characters
            ],
            "tasks": self.scheduler.get_task_stats(),
        }
