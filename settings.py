class Settings:
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Изициализирует настройки игры"""
        # Параметры экрана
        self.screen_widht = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        # Настройки корабля
        self.ship_speed = 10
        self.ship_limit = 3
        # Параметры снаряда
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
        # Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction = 1 означает движение вправо, а -1 - влево
        self.fleet_direction = 1
