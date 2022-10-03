from random import shuffle
from config_system import config

def guess(base_sets: list):
    sets = base_sets
    round = 0
    while sets:
        round += 1
        missed = []
        
        shuffle(sets)
        max_score = len(sets)
        current_score = 0
        print(f"Round {round}, words in this round: {max_score}")

        for current_set_index, set in enumerate(sets):
            foreign_words, local_words = set
            print(" ".join(local_words))

            guess = input(":").strip()
            if not guess:
                print("Skipped")
                missed.append(set)
                continue
            guess_words = guess.split(" ")
            
            is_correct = False
            for foreign_word in foreign_words:
                foreign_phrase_words = foreign_word.split(" ")
                if len(guess_words) > len(foreign_phrase_words):
                    # too many words provided
                    continue
                
                missed_minor_words = []
                is_correct = True
                
                for i, _ in enumerate(foreign_phrase_words):
                    if guess_words[i] != foreign_phrase_words[i]:
                        if foreign_phrase_words[i] in config.ignore:
                            missed_minor_words.append(foreign_phrase_words.pop(i))

                        else:
                            is_correct = False
                            break
                    
                    if i == len(guess_words) -1 and i < len(foreign_phrase_words) - 1:
                        is_correct = False
                        break

                if is_correct:
                    break

            # Scoring
            if is_correct:
                if missed_minor_words:
                    if len(missed_minor_words) > 1:
                        print(f'Correct, missed minor words: "{", ".join(missed_minor_words)}"')
                    else:
                        print(f'Correct, missed minor word: "{missed_minor_words[0]}"')
                else:
                    print("Correct")
                
                current_score += 1
                print(f"{current_score} / {max_score}")
            else:
                print("Failed")
                print(f"> {foreign_word}")
                missed.append(set)

        
        print("------------------")
        sets = missed.copy()