from characters import CharacterWorker
from characters.tasks import gather, craft, withdraw_bank


name = CharacterWorker("oleg")

# Обычная задача в конец очереди.
name.task(craft, "copper_bar", 56)

name.run()
