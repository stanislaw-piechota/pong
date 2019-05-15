class Game_stats():
    """class of static input of the game"""

    def __init__(self):
        #setting attributes
        self.game_active = False
        self.a_win = False
        self.a_hm = 0
        self.b_win = False
        self.b_hm = 0
        self.accel = 0

        #reseting after starting program
        self.reset_stats()

    def reset_stats(self):
        #function for reseting
        self.a_hm = 0
        self.b_hm = 0
        self.accel = 0

    def update_accel(self):
        if self.a_hm + self.b_hm == 0:
            self.accel = 1
        else:
            self.accel = (self.a_hm + self.b_hm) * 2
