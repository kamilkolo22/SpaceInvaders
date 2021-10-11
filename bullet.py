import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Klasa do zarządzania pociskami"""

    def __init__(self, ai_game):
        """Utworzenie obiektu w aktualnym połozeniu statku"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Utworzenie prostokąta w (0,0) i zdefiniowanie położenia
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """Poruszanie się pocisku"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Wyświetlenie pocisku"""
        pygame.draw.rect(self.screen, self.color, self.rect)
