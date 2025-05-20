from GamePlay import start_new_game
from GameSettings import GameSettings
from GameStats import GameStats

class Main:
    def __init__(self):
        self.settings = GameSettings()
        self.stats = GameStats()

    def run(self):
        while True:
            print("Welcome to the Wordle Enhanced Game!")                  # Welcome the user to the game and present the menu
            print("\n📌 Main Menu")
            print("1. ▶ Start a new game")
            print("2. 📊 View stats")
            print("3. 🔄 Reset stats")
            print("4. ❌ Exit")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                self.start_game_flow()
            elif choice == "2":
                self.stats.display_stats()
            elif choice == "3":
                confirm = input("Are you sure you want to reset stats? (Input yes,y to confirm/ anything else to decline): ").strip().lower()
                if confirm in ["yes", "y"]:
                    self.stats.reset_stats()
                    print("✅ Stats have been reset.")
                else:
                    print("Stats reset refused.")
            elif choice == "4":
                print("👋 Thanks for playing! Goodbye.")
                break
            else:
                print("❌ Invalid choice. Please enter 1–4.")

    def start_game_flow(self):                                            # The flow of the game to continue playing and register wins/losses
        self.settings.configure_settings()                                # Starting point of the game is by specifying the settings
        if self.settings.mode == "daily":
            if self.stats.has_played_today(self.settings.word_length):
                print(f"🕒 You have already played Daily {self.settings.word_length}-Letter Mode today!")
                print("📆 Come back tomorrow for a new challenge.")
                input("Press Enter to return to the main menu...")
                return
        print("Game will start with the following settings:")             # Showing which settings have been established
        print(self.settings)

        game_session = start_new_game({
            "mode": self.settings.mode,
            "difficulty": self.settings.difficulty,
            "length": self.settings.word_length
        })

        if game_session["won"]:
            self.stats.record_win()
            if self.settings.mode == "daily":
                self.stats.save_daily_play(self.settings.word_length)  # Mark daily word as played in its respective length
        else:
            self.stats.record_loss()
            if self.settings.mode == "daily":
                self.stats.save_daily_play(self.settings.word_length)  # Still counts as played

        self.stats.display_stats()                                        # Show stats after each game
        input("Press Enter to return to the main menu...")

# Example of running the main class
if __name__ == "__main__":
    game = Main()
    game.run()
