import os
from datetime import datetime

class GameStats:
    def __init__(self, stats_file="game_stats.txt", daily_file="daily_played.txt"):
        """
        Initializes the GameStats object.
        - Loads previous stats and daily play info from files if available.
        """
        self.filename = stats_file              # File to store win/loss/streak stats
        self.daily_file = daily_file            # File to store last daily play dates
        self.wins = 0
        self.losses = 0
        self.current_streak = 0
        self.max_streak = 0
        self.last_daily5_date = None            # Last time 5-letter daily game was played
        self.last_daily6_date = None            # Last time 6-letter daily game was played
        self.load_stats()                       # Load stats from file
        self.load_daily_play()                  # Load last played daily word dates

    def load_daily_play(self):
        """
        Loads the last played dates for daily 5-letter and 6-letter games from the daily file.
        """
        if os.path.exists(self.daily_file):
            with open(self.daily_file, "r") as f:
                for line in f:
                    if line.startswith("daily5:"):
                        self.last_daily5_date = line.strip().split(":")[1]
                    elif line.startswith("daily6:"):
                        self.last_daily6_date = line.strip().split(":")[1]

    def save_daily_play(self, length):
        """
        Saves today's date as the last played date for the current daily game.
        - Supports 5-letter and 6-letter word modes.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        if length == 5:
            self.last_daily5_date = today
        elif length == 6:
            self.last_daily6_date = today

        with open(self.daily_file, "w") as f:
            if self.last_daily5_date:
                f.write(f"daily5:{self.last_daily5_date}\n")
            if self.last_daily6_date:
                f.write(f"daily6:{self.last_daily6_date}\n")

    def has_played_today(self, length):
        """
        Checks if the player has already played the daily game today.
        Returns True if played today, otherwise False.
        """
        today = datetime.now().strftime("%Y-%m-%d")
        if length == 5:
            return self.last_daily5_date == today
        elif length == 6:
            return self.last_daily6_date == today
        return False

    def record_win(self):
        """
        Checks if the player has already played the daily game today.
        Returns True if played today, otherwise False.
        """
        self.wins += 1
        self.current_streak += 1
        self.max_streak = max(self.max_streak, self.current_streak)
        self.save_stats()

    def record_loss(self):
        """
        Updates stats when the user loses a game.
        - Increments losses and resets current streak.
        """
        self.losses += 1
        self.current_streak = 0
        self.save_stats()

    def display_stats(self):
        """
        Prints the current stats to the console.
        """
        print("\n📊 Game Statistics:")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Current Streak: {self.current_streak}")
        print(f"Max Streak: {self.max_streak}\n")

    def save_stats(self):
        """
        Saves the current stats to the stats file in CSV format.
        """
        with open(self.filename, "w") as file:
            file.write(f"{self.wins},{self.losses},{self.current_streak},{self.max_streak}")

    def load_stats(self):
        """
        Loads the saved stats from the stats file if it exists.
        """
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                line = file.read().strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 4:
                        self.wins = int(parts[0])
                        self.losses = int(parts[1])
                        self.current_streak = int(parts[2])
                        self.max_streak = int(parts[3])

    def reset_stats(self):
        """
        Resets all statistics to 0 and saves to file.
        """
        self.wins = 0
        self.losses = 0
        self.current_streak = 0
        self.max_streak = 0
        self.save_stats()

