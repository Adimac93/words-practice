from random import shuffle
from time import time


def get_words_list():
    with open("words.txt", encoding="utf-8") as file:
        return file.read().splitlines()

def guess(words_to_practice: list) -> None:
    round_counter = 1
    
    while True:
        print(f"Round: {round_counter}")

        shuffle(words_to_practice)
        missed = []

        words_total_number = len(words_to_practice)
        words_count = words_total_number

        for word in words_to_practice:
            en, pl = word
            print(pl)
            answer = input(":")
            is_correct = answer == en
            if is_correct:
                words_count-=1
                print(f"{words_count}/{words_total_number} words left in this round")
            else:
                missed.append(word)
                print(en)

        if not missed:
            break

        round_counter += 1
        words_to_practice = missed.copy()



base_list = [tuple(map(str.strip,line.split("-",maxsplit=1))) for line in get_words_list()]
start_time = time()

print(f"Practicing {len(base_list)} words")
guess(base_list)
print(f"Your time is: {round(time() - start_time,2)}s")