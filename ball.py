import pygame

class Ball():
    """class of ball"""

    def __init__(self, screen):
        #initialization, and setting attributes
        self.screen = screen

        #importing picture of ball
        self.image = pygame.image.load('images/ball1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        #position at the begenning
        self.rect.centerx = 600
        self.rect.centery = 350

    def blitme(self):
        #making ball visible
        self.screen.blit(self.image, self.rect)
