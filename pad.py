import pygame

class Pad():
    """class of left pad"""

    def __init__(self, settings, screen):
        #initialization and setting attributes
        self.screen = screen

        self.rect = pygame.Rect(0, 0, settings.pad_width, settings.pad_height)
        self.rect.centerx = 50
        self.rect.centery = 350

        self.y = float(self.rect.y)

        self.color = settings.pad_color

        self.moving_up = False
        self.moving_down = False

    def update(self, settings):
        #updating the position
        if self.moving_up and self.rect.top >= 0:
            self.rect.y -= settings.pad_speed_factor
        elif self.moving_down and self.rect.bottom <= 700:
            self.rect.y += settings.pad_speed_factor

    def draw_pad(self):
        #drawing pad on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
