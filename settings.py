class Settings:
    """Класс для хранения всех настроек игры"""

    def __init__(self):
        """Изициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # Темп ускорения игры
        self.speedup_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры"""
        self.ship_speed = 8.0
        self.bullet_speed = 10.0
        self.alien_speed = 0.8
        # fleet_direction = 1 означает движение вправо, а -1 - влево
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки скорости"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale