import random
from datetime import datetime
from UserInput import validate_guess
from dataclasses import field
from datetime import datetime
from UserInput import validate_guess, display_feedback, update_letter_status, display_keyboard

ATTEMPTS = 6

def load_words(difficulty="easy", length=5):
    filename = f"{difficulty}_{length}.txt"

    if length==5:
        filename=f"words5letters.txt"
    elif length==6:
        filename=f"words6letters.txt"


    try:
        with open(filename, "r") as file:
            words = list(
                map(lambda w: w.strip().lower(), file))

            if difficulty == "difficult":
                return words[30:]  # lines 31 onwards (0-indexed)
            else:
                return words[:30]  # lines 1–30
    except FileNotFoundError:
        print(f"Word file {filename} not found.")
        return []

def load_daily_word(length):
    filename = f"words{length}letters.txt"

    try:
        with open(filename, "r") as file:
            words = list(
                map(lambda line: line.strip().lower(), file)
            )

            # Use today's date as a seed
            today = datetime.now().strftime("%Y-%m-%d")  #example "2025-05-25"
            random.seed(today)

            index = random.randint(0, len(words) - 1)
            return words[index]

    except FileNotFoundError:
        print(f"❌ Daily word file {filename} not found.")
        return None


def start_new_game(settings):
    print("\n🎮 Starting a new game...")

    difficulty = settings.get("difficulty", "easy")
    length = settings.get("length", 5)
    mode = settings.get("mode", "normal")

    if mode == "daily":
        secret_word = load_daily_word(length)
        if not secret_word:
            return None
    else:
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
    display_keyboard(True)  #removes the colors of the previous game on the keyboard


    # loop for guessing one word
    for i in range(ATTEMPTS):

        # color_results = color for letters, guess is the word in a string, letters are the list of that string
        color_results, guess, letters = validate_guess(session["secret_word"])  #returns a list as long as the word, where in each position there's is "s","g" and "y" for silver(grey), green and yellow
        display_feedback(color_results, guess)
        update_letter_status(color_results, guess)
        display_keyboard()

        if guess == session["secret_word"]:
            session["won"] = True
            print(f"You won! The secret word was: {session['secret_word']}.")
            print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")
            break
        session["attempts_left"] = session["attempts_left"] - 1
        session["guesses"].append(guess)

        if not session["won"] and session["attempts_left"] > 0:
            if session["attempts_left"] > 1:
                print(f"Your word is not correct! You have {session['attempts_left']} attempts left. Think carefully.")
            else:
                print(f"Your word is not correct! You only have one attempt left. Think carefully.")

        if session["attempts_left"] == 0:
            print(f"You lost! The secret word was: {session['secret_word']}.")
            print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")

    return session

