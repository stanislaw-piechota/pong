import pygame

class Pad1():
    """class of the right pad. All like in pad.py file"""

    def __init__(self, settings, screen):
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.pad_width, settings.pad_height)
        self.rect.centerx = 1190
        self.rect.centery = 350

        self.y = float(self.rect.y)

        self.color = settings.pad_color

        self.moving_up = False
        self.moving_down = False

    def update(self, settings):
        if self.moving_up and self.rect.top >= 0:
            self.rect.y -= settings.pad_speed_factor
        elif self.moving_down and self.rect.bottom <= 700:
            self.rect.y += settings.pad_speed_factor

    def draw_pad(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

