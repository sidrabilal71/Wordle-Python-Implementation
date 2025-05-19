class GameStats:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.current_streak = 0
        self.max_streak = 0

    def record_win(self):
        self.wins += 1
        self.current_streak += 1
        self.max_streak = max(self.max_streak, self.current_streak)

    def record_loss(self):
        self.losses += 1
        self.current_streak = 0

    def display_stats(self):
        print("\n Game Statistics:")
        print(f"Wins: {self.wins}")
        print(f"Losses: {self.losses}")
        print(f"Current Streak: {self.current_streak}")
        print(f"Max Streak: {self.max_streak}\n")
