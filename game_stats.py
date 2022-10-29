class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Omotoa;oze statistics."""
        self.settings = ai_game.settings
        self.reset_status()

        # Start game in an inactive state.
        self.game_active = False

    def reset_status(self):
        """Initialize statistis that can change during the game."""
        self.ships_left = self.settings.ship_limit
