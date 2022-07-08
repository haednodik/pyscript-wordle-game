def game_instruction():
    print("Wordle is a single player game")
    print("A player has to guess a five letter hidden word")
    print("You have six attempts")
    print('Your Progress Guide "✔❌❌✔➕"')
    print('"✔" Indicates that the letter at that position was guessed correctly')
    print('"➕" indicates that the letter at that position is in the hidden word, but in a different position')
    print('''"❌" indicates that the letter at that position is wrong, and isn't in the hidden word''')

def check_word():
    hidden_word = "snail"
    attempt = 6
    while attempt > 0:
        guess = str(input("Guess the word: "))
        if guess == hidden_word:
            print("You guessed the words correctly! WIN 🕺🕺🕺 ")
            break
        else:
            attempt = attempt - 1
            print(f"You have {attempt} attempt(s) left...")
            for char, g_char in zip(hidden_word, guess):
                if g_char in hidden_word and g_char in char:
                    print(g_char + " ✔ ")
                elif g_char in hidden_word:
                    print(g_char + " ➕ ")
                else:
                    print(" ❌ ")
            if attempt == 0:
                print(" Game over !!!! ")
