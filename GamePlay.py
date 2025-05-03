import random
from dataclasses import field

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
        "attempts_left": 6,
        "word_length": length,
        "guesses": [],
        "won": False
    }

    print(session)

    print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")
    return session
