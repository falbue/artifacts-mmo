from characters import CharacterWorker


valera = CharacterWorker("valera")

# Обычная задача в конец очереди.
valera.gather_resource(277, 10)

# Приоритет задаём снаружи, без параметра в gather_resource.
valera.enqueue_call(valera.gather_resource, 277, 3, priority=True)

valera.run()
