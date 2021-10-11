import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Klasa do zarządzania statkiem"""

    def __init__(self, ai_game):
        """Inicjalizacja statku i jego połozenia"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Wczytanie obrazu statku
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.bmp'),
            (100, 100))
        self.rect = self.image.get_rect()

        # Umiejscowienie statku
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        # Poruszanie się statku
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Uaktualnienie położenia statku"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Uaktualnienie obiektu rect
        self.rect.x = self.x

    def blitme(self):
        """Wyswietlenie statku kosmicznego"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Umieszczenie statku na środku"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
