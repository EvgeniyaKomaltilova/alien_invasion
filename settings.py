class Settings:
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        """Изициализирует настройки игры"""
        # Параметры экрана
        self.screen_widht = 900
        self.screen_height = 600
        self.bg_color = (50, 0, 100)
        # Настройки корабля
        self.ship_speed = 10
        # Параметры снаряда
        self.bullet_speed = 10
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (0, 0, 0)
        self.bullets_allowed = 3
