from characters import TeamCoordinator


def plan_craft_copper_bar(worker, bars: int) -> None:
    recipe = [
        {"action": "move", "map_id": 277},
        {"action": "gather", "times": 10},
        {"action": "move", "map_id": 529},
        {"action": "craft", "code": "copper_bar", "quantity": 1},
    ]
    worker.enqueue_recipe(recipe, repeat=bars)


coordinator = TeamCoordinator(
    bank_map_id=529,
    resource_nodes={
        "copper_ore": 277,
    },
)

valera = coordinator.add_worker("valera")

# Если есть второй персонаж, можно раскомментировать для cooperative-режима:
# helper = coordinator.add_worker("petya")

# Универсальная обёртка для крафта: можно менять recipe под любой предмет.
plan_craft_copper_bar(valera, bars=1)

# Вставка команды в топ:
# Если во время добычи нужно срочно отправить 3 ресурса в банк, вставляем это поверх очереди.
coordinator.inject_bank_topup(
    worker_name="valera",
    code="copper_ore",
    quantity=3,
    return_map_id=277,
)

# Поведение в простое:
# Если кому-то не хватает ресурсов, свободный персонаж поможет (добудет и положит в банк).
# coordinator.request_material(requester="valera", code="copper_ore", quantity=3)

coordinator.run(max_steps=200)
