import pygame.font

class Scoreboard():
    """Class of scoreboard for first pad"""

    def __init__(self, screen, stats):
        #initialization and setting attributes, and position of scoreboard
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        #preparing score
        score = str(self.stats.a_hm)
        self.score_image = self.font.render(score, True, self.text_color,
                                            (0, 170, 0))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = 300
        self.score_rect.centery = 20

    def show_score(self):
        #changing scoreboard on the screen
        self.screen.blit(self.score_image, self.score_rect)
