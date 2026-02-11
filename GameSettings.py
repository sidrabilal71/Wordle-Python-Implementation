class GameSettings:
    def __init__(self):
        """
        Initialize default settings for the game:
        - Mode: 'normal' or 'daily'
        - Difficulty: 'easy' or 'difficult' (only applies in normal mode)
        - Word length: 5 or 6 letters
        """
        self.mode = "normal"  # Default mode is 'normal' (player can play anytime)
        self.difficulty = "easy"  # Default difficulty is 'easy'
        self.word_length = 5  # Default word length is 5-letter words

    def set_mode(self):
        """
        Ask the user to choose the game mode: 'normal' or 'daily'.
        Input is repeated until a valid option is entered.
        """
        while True:
            user_input = input("Select game mode (normal/daily): ").strip().lower()         # We check the input string in lower case to avoid confusing between user-code
            if user_input in ["normal", "daily"]:
                self.mode = user_input                                                      # Save the specified mode for future use
                break
            print("Invalid input. Please enter 'normal' or 'daily'.")                       # User is trying to introduce a wrong name type

    def set_difficulty(self):
        """
        Ask the user to select difficulty: 'easy' or 'difficult'.
        Only relevant in 'normal' mode.
        """
        while True:
            user_input = input("Select difficulty (easy/difficult): ").strip().lower()      # We check the input string in lower case to avoid confusing between user-code
            if user_input in ["easy", "difficult"]:
                self.difficulty = user_input                                                # Save the specified difficulty for future use
                break
            print("Invalid input. Please enter 'easy' or 'difficult'.")                     # User is trying to introduce a wrong name type

    def set_word_length(self):
        """
        Ask the user to choose the word length: 5 or 6 letters.
        Only accepts valid integer inputs as strings ('5' or '6').
        """
        while True:
            user_input = input("Select word length (5 or 6): ").strip()
            if user_input in ["5", "6"]:
                self.word_length = int(user_input)                                          # Save the specified length of the words for future use
                break
            print("Invalid input. Please enter '5' or '6'.")                                # User is trying to introduce a wrong name type

    def configure_settings(self):
        """
        Central function to prompt user for game settings.
        - First asks for game mode
        - If mode is 'normal', also asks for difficulty
        - Always asks for word length
        """
        print("Configure your game settings:")
        self.set_mode()
        if self.mode == "normal":   # Skip difficulty selection in 'daily'
            self.set_difficulty()
        self.set_word_length()

    def __str__(self):
        return f"Mode: {self.mode}, Difficulty: {self.difficulty}, Word Length: {self.word_length}" # Printing the user the settings selected

