# These functions and variables are used to test the assignments, which start below

import random

random.seed(420)
bad_scrabble = {char.upper(): i + 1 for i, char in enumerate("abcdefghijklmnopqrstuvwxyz")}
WORD_LIST = ["armistice", "badminton", "zillion", "conglomerate", "botanical"]


def get_high_score(word_list: list):
    highest = ""
    for word in word_list:
        score = score_word(word.upper())
        if score > score_word(highest.upper()):
            highest = word
    return highest


def dict_checker(test: dict):
    val_set = set()
    for char, val in test.items():
        if val > 26:
            raise ValueError(f"Value of {char} too high: {val}")
        if val in val_set:
            raise ValueError(f"Value of {char} repeated: {val}")
        val_set.add(val)


# =========================== BEGINNING OF ASSIGNMENTS ============================#

"""
The bad_scrabble dictionary maps each letter in the alphabet to
its integer position in the alphabet. Write a function that converts each letter
in a word into that number and then adds them all together to get a final score, then
return the score. Note that strings can be treated as iterators of their characters.
"""


def score_word(word: str) -> int:
    pass  # Delete this line and write your code here


print(get_high_score(WORD_LIST))  # Should print 'conglomerate' when run

"""
Now modify the bad_scrabble dictionary so that 'zillion' has the highest score,
no number in the dictionary should be above 26, and there should be no duplicates.
i.e. you can only swap values between letters in the dictionary. Hint: swap the
values of "I" and "L" with something else. Also note that all keys in the dictionary
are upper case.
"""
# Modify bad_scrabble below


dict_checker(bad_scrabble)
print(get_high_score(WORD_LIST))

# Ignore this
vals = list(range(1, 27))
random.shuffle(vals)
vals = list(zip(vals, bad_scrabble.keys()))
bad_scrabble = {char.upper(): i + 1 for i, char in vals}
"""
The values of bad_scrabble have been shuffled (they are shuffled in the same
way every time), write a function that loops through a dictionary, alpha, and returns
a list which orders each character in the alphabet according to its new value.
You will have to nest loops to do this, and may need to look up some list methods.
(or at least I'll be impressed if you can do it without nesting them)
"""


def new_alphabet(alpha: dict) -> list[str]:
    pass  # Delete this line and write your code here


print("".join(new_alphabet(bad_scrabble)))  # ZAKUDIHEWLQXVFGPRONBTYJCMS is expected
