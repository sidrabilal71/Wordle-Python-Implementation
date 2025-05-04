import random
from UserInput import validate_guess
from dataclasses import field

ATTEMPTS = 6

def load_words(difficulty="easy", length=5):
    filename = f"{difficulty}_{length}.txt"  # e.g., "easy_5.txt"

    if length==5:
        filename=f"words5letters.txt"
    elif length==6:
        filename=f"words6letters.txt"


    try:
        with open(filename, "r") as file:
            words = [word.strip().lower() for word in file if len(word.strip()) == length]
            if difficulty == "difficult":
                return words[30:]  # lines 31 onwards (0-indexed)
            else:
                return words[:30]  # lines 1–30
    except FileNotFoundError:
        print(f"Word file {filename} not found.")
        return []

def start_new_game(settings):
    print("\n🎮 Starting a new game...")

    difficulty = settings.get("difficulty", "easy")
    length = settings.get("length", 5)

    word_list = load_words(difficulty, length)
    if not word_list:
        return None

    secret_word = random.choice(word_list)
    session = {
        "secret_word": secret_word,
        "attempts_left": ATTEMPTS,
        "word_length": length,
        "guesses": [],
        "won": False
    }

    # loop for guessing one word
    for i in range(ATTEMPTS):
        print(session)
        #TODO: do stuff with the return color_results

        # color_results = color for letters, guess is the word in a string, letters are the list of that string
        color_results, guess, letters = validate_guess(session["secret_word"])  #returns a list as long as the word, where in each position there's is "s","g" and "y" for silver(grey), green and yellow
        if guess == session["secret_word"]:
            session["won"] = True
            print(f"You won! The secret word was: {guess}.")
            break
        session["attempts_left"] = session["attempts_left"] - 1
        session["guesses"].append(guess)

    print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")
    return session
