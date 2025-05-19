from GamePlay import start_new_game
from GameSettings import GameSettings
from GameStats import GameStats

class Main:
    def __init__(self):
        self.settings = GameSettings()
        self.stats = GameStats()  # Add the stats object

    def run(self):
        while True:
            print("Welcome to the Wordle Enhanced Game!")                               # Welcome the user to the game
            self.settings.configure_settings()                                          # Starting point of the game is by specifying the settings
            print("Game will start with the following settings:")                       # Showing which settings have been established
            print(self.settings)
            game_session = start_new_game({
                "difficulty": self.settings.difficulty,
                "length": self.settings.word_length
            })

            if game_session["won"]:
                self.stats.record_win()
            else:
                self.stats.record_loss()

            self.stats.display_stats()                                                 # Show stats after each game

            play_again = input("\n🔁 Do you want to play again? (yes/no): ").strip().lower()
            if play_again not in ["yes", "y"]:
                print("👋 Thanks for playing! Goodbye.")
                break

# Example of running the main class
if __name__ == "__main__":
    game = Main()
    game.run()
