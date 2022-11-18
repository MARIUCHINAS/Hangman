import random
from time import sleep

def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         0         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            sleep(5)
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))
        sleep(5)

hangman_words = ['class', 'pilot', 'planet', 'word', 'phrase', 'concept', 'idea', 'thing', 'object', 'entity', 'unit', 'element', 'detail', 'opinion', 'tone', 'mood', 'feeling', 'emotion', 'sensation', 'response', 'reaction', 'viewpoint', 'attitude', 'consequence', 'chaos', 'randomness', 'chance', 'variability', 'uncertainty', 'ambiguity', 'disorder', 'confusion', 'havoc', 'pandemonium', 'structure', 'form', 'shape', 'configuration', 'composition', 'design', 'pattern', 'arrangement', 'system', 'organization', 'process', 'function', 'operation', 'action', 'task', 'activity', 'course', 'step', 'procedure', 'method', 'purpose', 'goal', 'objective', 'target', 'intention', 'motive', 'ambition', 'aim', 'design', 'plan', 'energy', 'force', 'power', 'spirit', 'drive', 'determination', 'real', 'enthusiasm', 'passion', 'foundation', 'basis', 'groundwork', 'root', 'origin', 'source', 'bottom', 'essence', 'heart', 'center', 'excellence', 'perfection', 'quality', 'value', 'worth', 'greatness', 'superiority', 'magnitude']
hangman(random.choice(hangman_words))