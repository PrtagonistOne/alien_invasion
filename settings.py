class Settings:
    """A class to stire all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.bullet_speed = None
        self.alien_speed = None
        self.alien_points = None
        self.ship_speed = None
        self.fleet_direction = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 139)

        # High score should never be reset.
        self.high_score = 0

        # Ship settings
        # self.ship_speed = 2
        self.ship_limit = 3

        # Bullet settings
        # self.bullet_speed = 1.5
        self.bullet_width = 3000
        self.bullet_height = 15
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3

        # Rocket settings
        self.rocket_speed = 1.3

        # Alien settings
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        # self.fleet_direction = 1

        # How quickly game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
