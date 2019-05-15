import game_functions as gf
from random import randint

class Settings():
    """class of parameters of some objects"""

    def __init__(self):
        #setting attributes
        
        #screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (0, 170, 0)

        #pad settings
        self.pad_speed_factor = 3
        self.pad_width = 20
        self.pad_height = 80
        self.pad_color = 250, 250, 250

        #ball settings
        self.dirx = gf.make_x()
        self.diry = gf.make_y()
