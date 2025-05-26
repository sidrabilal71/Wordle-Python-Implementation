import requests
from collections import defaultdict

# A dictionary to keep track of each letter's status (green/yellow/grey)
# Default is None → not guessed yet
letter_status = defaultdict(lambda: None)                                                                               # Initial letter statuses: None means not guessed yet

# Layout of the on-screen keyboard (used for display)
KEYBOARD_ROWS = [
    "     QWERTYUIOP",
    "     ASDFGHJKL",
    "      ZXCVBNM"
]

# ANSI color codes used to show feedback (terminal coloring)
COLOR_CODES = {
    "g": "\033[1;32m",  # Green = correct letter in correct place
    "y": "\033[1;33m",  # Yellow = correct letter in wrong place
    "s": "\033[1;37m",  # Silver/Grey = letter not in the word
    None: "\033[0m"     # Reset/default color                                                                                                   # Default
}
RESET = "\033[0m"

def check_word(word):
    """
    Check if a word is valid English using an external dictionary API.
    Returns True if the word exists, False otherwise.
    """
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    return response.status_code == 200

def get_guess(length):
    """
    Prompt the user to enter a valid guess:
    - Must be correct length
    - Only letters
    - Must exist in the dictionary
    Returns the guess (lowercased string).
    """
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

        return guess    # Validated guess                                                                                                # Turns it into a list of letters

# Constants used for feedback
SILVER = "s"
GREEN = "g"
YELLOW = "y"


def validate_guess(secret_word):
    """
    Compares the player's guess with the secret word.
    Returns:
    - A list of color codes (g/y/s)
    - The original guess
    - A list of guessed letters
    """
    secret_word_letters = list(secret_word)
    length = len(secret_word_letters)
    color_list = [SILVER] * length      # Initially assume all incorrect (silver)                                                                                #ALL SILVER
    guess = get_guess(length)
    letters = list(map(lambda x: x, guess))     # Convert guess to list of letters

    used_secret = [False] * length # Track matched letters in secret
    used_guess = [False] * length # Track matched letters in guess

    # Step 1: Check for correct position (GREEN)
    def match_green(i):
        if letters[i] == secret_word_letters[i]:
            color_list[i] = GREEN
            used_secret[i] = True
            used_guess[i] = True

    list(map(match_green, range(length)))


    # Step 2: Check for wrong position (YELLOW)
    def match_yellow(i):
        if not used_guess[i]:
            for j in range(length):
                if not used_secret[j] and letters[i] == secret_word_letters[j]:
                    color_list[i] = YELLOW
                    used_secret[j] = True
                    break

    list(map(match_yellow, range(length)))

    return color_list, guess, letters

def display_feedback(color_list, guess):
    """
    Print colored feedback for the user's guess.
    Each letter is displayed with a background color (green/yellow/grey).
    """
    color_codes = {
        "g": "\033[1;32m",  # Green                                                                                # Bright Green
        "y": "\033[1;33m",  # Yellow                                                                                              # Bright Yellow
        "s": "\033[1;37m",  # Silver                                                                                         # Bright Grey (white)
    }
    reset = "\033[0m"

    colored_output = ""
    for char, color in zip(guess, color_list):
        colored_output += f"{color_codes[color]}{char.upper()}{reset} "

    print(f"\n🧩 Feedback: {colored_output.strip()}")

def update_letter_status(color_list, guess):
    """
    Update the keyboard's letter status based on the most recent guess.
    Priority order: green > yellow > silver
    """
    for letter, color in zip(guess.upper(), color_list):
        current = letter_status[letter]
        # Priority: green > yellow > silver
        if current == "g":
            continue # Already green, no need to downgrade
        if current == "y" and color == "s":
            continue # Yellow is better than silver
        letter_status[letter] = color # Update to new color

def display_keyboard(reset = False):
    """
    Print the current keyboard with colors based on previous guesses.
    If reset=True, clears all colors for a new game.
    """
    if reset:
        letter_status.clear()   #clears the colors from the keyboard for new game
        return

    print("\n⌨️ Used Letters:")
    for row in KEYBOARD_ROWS:
        line = ""
        for letter in row:
            status = letter_status[letter]
            color = COLOR_CODES[status]
            line += f"{color}{letter}{RESET} "
        print(line.strip())
    print()





