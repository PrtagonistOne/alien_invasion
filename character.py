import pygame
from settings import Settings


class Character:
    """A class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = Settings()

        # Load the ship image and get its rect.
        self.image = pygame.transform.smoothscale(
            pygame.image.load('images/alien_character.bmp'), (70, 100))

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom of the screen.
        self.rect.midbottom = self.screen_rect.center

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
