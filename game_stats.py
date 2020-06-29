import game_functions as gf

class Game_stats():
    """class of static input of the game"""

    def __init__(self, settings):
        #setting attributes
        self.game_active = False
        self.a_win = False
        self.a_hm = 0
        self.b_win = False
        self.b_hm = 0

        #reseting after starting program
        self.reset_stats(settings)

    def reset_stats(self, settings):
        #function for reseting
        self.a_hm = 0
        self.b_hm = 0
        settings.dirx = gf.make_x()
        settings.diry = gf.make_y()
        settings.pad_height = 90

