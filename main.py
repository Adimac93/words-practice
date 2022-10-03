from time import time
from user_input import guess
from parser import Parser
from sources import get_local_resource

parser = Parser(" - ",",")
sets = parser.parse(get_local_resource("words.txt"))

start_time = time()
guess(sets)
print(f"Your time is: {round(time() - start_time,2)}s")