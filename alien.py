import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Klasa jednego obcego"""

    def __init__(self, ai_game):
        """Inicjalizacja obcego i jego położenia"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Wczytywanie obrazu
        self.image = pygame.transform.scale(
            pygame.image.load('images/alien.bmp'),
            (50, 50))
        self.rect = self.image.get_rect()

        # Umieszczenie obcego na ekranie
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Zwraca True jeśli obcy jest przy krawędzi"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left < 0:
            return True

    def update(self):
        """Przesunięcie obcego w prawo"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
