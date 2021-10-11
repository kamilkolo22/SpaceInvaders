class Settings:
    """Klasa przechowywująca ustawienia gry"""

    def __init__(self):
        """Inicjalizajca ustawień gry"""
        # Ustawienia ekranu
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ustawienia statku
        self.ship_limit = 3

        # Ustawienia pocisków
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Ustawienia obcych
        self.fleet_drop_speed = 3

        self.speedup_scale = 1.3
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjializacja ustawien, które się zmieniają w czsie gry"""
        self.ship_speed = 1.5
        self.bullet_speed = 2.0
        self.alien_speed = 0.5
        self.alien_points = 50

        # 1 w prawo, -1 w lewo
        self.fleet_direction = 1

    def increase_speed(self):
        """Zmiana ustawień szybkości"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
