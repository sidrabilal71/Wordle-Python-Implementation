import random
from datetime import datetime
from UserInput import validate_guess
from dataclasses import field
from datetime import datetime
from UserInput import validate_guess, display_feedback, update_letter_status, display_keyboard

ATTEMPTS = 6  # Maximum number of attempts allowed per game

def load_words(difficulty="easy", length=5):
    """
    Load words from a file based on difficulty and word length.
    - File is expected to be named like 'words5letters.txt' or 'words6letters.txt'.
    - Splits the list in half: first half is 'easy', second half is 'difficult'.
    """
    filename = f"words{length}letters.txt"

    try:
        with open(filename, "r") as file:
            words = list(
                map(lambda w: w.strip().lower(), file)) # Clean and lowercase all lines
            midpoint = len(words) // 2  # Split in half

            if difficulty == "difficult":
                return words[midpoint:]  # Second half
            else:
                return words[:midpoint]  # First half
    except FileNotFoundError:
        print(f"Word file {filename} not found.")
        return []

def load_daily_word(length):
    """
    Load the daily word in a deterministic way based on today's date.
    Ensures all players get the same word on the same day.
    """
    filename = f"words{length}letters.txt"

    try:
        with open(filename, "r") as file:
            words = list(
                map(lambda line: line.strip().lower(), file)
            )

            # Use today's date as a seed
            today = datetime.now().strftime("%Y-%m-%d")  #example "2025-05-25" Format: 'YYYY-MM-DD'
            random.seed(today)  #Set seed to today for consistent word

            index = random.randint(0, len(words) - 1)
            return words[index]

    except FileNotFoundError:
        print(f"❌ Daily word file {filename} not found.")
        return None


def start_new_game(settings):
    """
    Start a single game session based on the provided settings:
    - Selects secret word based on normal or daily mode
    - Allows the player up to 6 attempts to guess
    - Tracks guesses, displays feedback, and keyboard updates
    - Returns a session dictionary with game outcome
    """
    print("\n🎮 Starting a new game...")

    difficulty = settings.get("difficulty", "easy")
    length = settings.get("length", 5)
    mode = settings.get("mode", "normal")


    # Get the secret word depending on the mode
    if mode == "daily":
        secret_word = load_daily_word(length)
        if not secret_word:
            return None
    else:
        word_list = load_words(difficulty, length)
        if not word_list:
            return None
        secret_word = random.choice(word_list)


    # Initialize game session state
    session = {
        "secret_word": secret_word,
        "attempts_left": ATTEMPTS,
        "word_length": length,
        "guesses": [],
        "won": False
    }
    # Clear the keyboard display for the new game
    display_keyboard(True)  #removes the colors of the previous game on the keyboard



    # Gameplay loop: allow user to make up to 6 guesses
    for i in range(ATTEMPTS):

        # color_results = color for letters, guess is the word in a string, letters are the list of that string
        color_results, guess, letters = validate_guess(session["secret_word"])  #returns a list as long as the word, where in each position there's is "s","g" and "y" for silver(grey), green and yellow
        display_feedback(color_results, guess)  # Show colored feedback (green, yellow, grey)
        update_letter_status(color_results, guess) # Update visual keyboard with color info
        display_keyboard() # Show current keyboard state

        # Check win condition
        if guess == session["secret_word"]:
            session["won"] = True
            print(f"You won! The secret word was: {session['secret_word']}.")
            print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")
            break

        # Record the guess and reduce attempts
        session["attempts_left"] = session["attempts_left"] - 1
        session["guesses"].append(guess)

        # Feedback depending on remaining attempts
        if not session["won"] and session["attempts_left"] > 0:
            if session["attempts_left"] > 1:
                print(f"Your word is not correct! You have {session['attempts_left']} attempts left. Think carefully.")
            else:
                print(f"Your word is not correct! You only have one attempt left. Think carefully.")

        # If out of attempts, reveal word
        if session["attempts_left"] == 0:
            print(f"You lost! The secret word was: {session['secret_word']}.")
            print(f"🔠 Game initialized with a {length}-letter word (Difficulty: {difficulty})")

    return session

