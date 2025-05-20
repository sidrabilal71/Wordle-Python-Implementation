class GameSettings:
    def __init__(self):
        self.mode = "normal"                                                                # Default: normal
        self.difficulty = "easy"                                                            # Default: easy
        self.word_length = 5                                                                # Default: 5-letter words

    def set_mode(self):
        while True:
            user_input = input("Select game mode (normal/daily): ").strip().lower()         # We check the input string in lower case to avoid confusing between user-code
            if user_input in ["normal", "daily"]:
                self.mode = user_input                                                      # Save the specified mode for future use
                break
            print("Invalid input. Please enter 'normal' or 'daily'.")                       # User is trying to introduce a wrong name type

    def set_difficulty(self):
        while True:
            user_input = input("Select difficulty (easy/difficult): ").strip().lower()      # We check the input string in lower case to avoid confusing between user-code
            if user_input in ["easy", "difficult"]:
                self.difficulty = user_input                                                # Save the specified difficulty for future use
                break
            print("Invalid input. Please enter 'easy' or 'difficult'.")                     # User is trying to introduce a wrong name type

    def set_word_length(self):
        while True:
            user_input = input("Select word length (5 or 6): ").strip()
            if user_input in ["5", "6"]:
                self.word_length = int(user_input)                                          # Save the specified length of the words for future use
                break
            print("Invalid input. Please enter '5' or '6'.")                                # User is trying to introduce a wrong name type

    def configure_settings(self):
        print("Configure your game settings:")
        self.set_mode()
        if self.mode == "normal":
            self.set_difficulty()
        self.set_word_length()

    def __str__(self):
        return f"Mode: {self.mode}, Difficulty: {self.difficulty}, Word Length: {self.word_length}" # Printing the user the settings selected

