from characters import CharacterWorker
from characters.tasks import gather


name = CharacterWorker("oleg")

# Обычная задача в конец очереди.
name.task(gather, 277, 10000)

name.run()
