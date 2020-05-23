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
