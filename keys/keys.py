import pygame
import sys

class Keys:
    """Keys responder outputer"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))


    def run_game(self):
        """Start the main loop for game"""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_event(self, event):
        """Respond to keypresses."""
        print(event)

    def _check_keyup_event(self, event):
       print(event)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill((230,230,230))


k = Keys()
k.run_game()
