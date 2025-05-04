def get_guess(length):
    while True:
        guess = input(f"Enter your {length}-letter guess: ").lower().strip()

        if len(guess) != length:
            print(f"Your guess must be exactly {length} letters.")
            continue

        if not guess.isalpha():
            print("Your guess must contain only letters.")
            continue

#TODO: UC7, check if the word exists
        # if guess not in valid_words:      #add valid_words to attributes
        #     print("That's not a valid word.")
        #     continue


        return guess  #turns it into a list of letters

SILVER = "s"
GREEN = "g"
YELLOW = "y"

def validate_guess(secret_word):
    secret_word_letters = list(secret_word)
    length = len(secret_word_letters)
    color_list = [SILVER] * length  #ALL SILVER
    guess = get_guess(length)
    letters = list(guess)

    used_secret = [False] * length
    used_guess = [False] * length

    # GREEN
    for i in range(length):
        if letters[i] == secret_word_letters[i]:
            color_list[i] = GREEN
            used_secret[i] = True
            used_guess[i] = True

    #YELLOW
    for i in range(length):
        if not used_guess[i]:
            for j in range(length):
                if not used_secret[j] and letters[i] == secret_word_letters[j]:
                    color_list[i] = YELLOW
                    used_secret[j] = True
                    break

    return color_list, guess, letters


