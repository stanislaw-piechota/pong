import pygame.font

class Scoreboard1():
    """class of scoreboard for second pad. All like in scoreboard in
    scoreboard.py file"""

    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        score = str(self.stats.b_hm)
        self.score_image = self.font.render(score, True, self.text_color,
                                            (0, 170, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = 900
        self.score_rect.centery = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
