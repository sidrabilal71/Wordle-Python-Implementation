import requests
from collections import defaultdict

letter_status = defaultdict(lambda: None)                                                                               # Initial letter statuses: None means not guessed yet

KEYBOARD_ROWS = [
    "     QWERTYUIOP",
    "     ASDFGHJKLÑ",
    "      ZXCVBNM"
]
COLOR_CODES = {
    "g": "\033[1;32m",                                                                                                  # Green (correct position)
    "y": "\033[1;33m",                                                                                                  # Yellow (wrong position)
    "s": "\033[1;37m",                                                                                                  # Grey (not in word)
    None: "\033[0m"                                                                                                     # Default
}
RESET = "\033[0m"

def check_word(word):                                                                                                   # Used to check if the input word exists
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    return response.status_code == 200

def get_guess(length):
    while True:
        guess = input(f"Enter your {length}-letter guess: ").lower().strip()

        if len(guess) != length:
            print(f"Your guess must be exactly {length} letters.")
            continue

        if not guess.isalpha():
            print("Your guess must contain only letters.")
            continue

        if not check_word(guess):                                                                                       # Add valid_words to attributes
            print("That's not a valid word.")
            continue

        return guess                                                                                                    # Turns it into a list of letters

SILVER = "s"
GREEN = "g"
YELLOW = "y"

def validate_guess(secret_word):
    secret_word_letters = list(secret_word)
    length = len(secret_word_letters)
    color_list = [SILVER] * length                                                                                      #ALL SILVER
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

def display_feedback(color_list, guess):
    color_codes = {
        "g": "\033[1;32m",                                                                                              # Bright Green
        "y": "\033[1;33m",                                                                                              # Bright Yellow
        "s": "\033[1;37m",                                                                                              # Bright Grey (white)
    }
    reset = "\033[0m"

    colored_output = ""
    for char, color in zip(guess, color_list):
        colored_output += f"{color_codes[color]}{char.upper()}{reset} "

    print(f"\n🧩 Feedback: {colored_output.strip()}")

def update_letter_status(color_list, guess):
    for letter, color in zip(guess.upper(), color_list):
        current = letter_status[letter]
        # Priority: green > yellow > silver
        if current == "g":
            continue
        if current == "y" and color == "s":
            continue
        letter_status[letter] = color

def display_keyboard():
    print("\n⌨️ Used Letters:")
    for row in KEYBOARD_ROWS:
        line = ""
        for letter in row:
            status = letter_status[letter]
            color = COLOR_CODES[status]
            line += f"{color}{letter}{RESET} "
        print(line.strip())
    print()





