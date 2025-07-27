class GameStats:
    """Track statisticks for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Import high score from file.
        try:
            with open('high_score.txt', 'r') as f:
                content = f.read().strip()
            self.high_score = int(content) if content else 0
        except FileNotFoundError:
            # File doesn't exist: create it with 0 and set high_score
            with open('high_score.txt', 'w') as f:
                f.write('0')
            self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
