#version: 2.2.1
#game's code is compatibile with PEP8 requirements

#importing all objects and libraries
import pygame
import sys
from settings import Settings
from pad import Pad
from pad1 import Pad1
import game_functions as gf
from ball import Ball
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard
from scoreboard1 import Scoreboard1

def run_game():
    """main loop of the game"""
    #intialization of pygame library
    pygame.init()
    #initializing all needed objects
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    ball = Ball(screen)
    pad = Pad(settings, screen)
    pad1 = Pad1(settings, screen)
    stats = Game_stats()
    pygame.display.set_caption("Pong")
    sb = Scoreboard(screen, stats)
    sb1 = Scoreboard1(screen, stats)
    start_button = Button(screen, settings, "START")

    while True:
        #using functions from module
        if stats.game_active:
            pad.update(settings)
            pad1.update(settings)
            gf.update_ball(ball, settings, pad, pad1, stats, sb, sb1)
        gf.update_screen(settings, screen, pad, pad1, ball, stats,
                         start_button, sb, sb1)
        gf.check_events(settings, screen, pad, pad1, stats, start_button)
        gf.make_speed(stats)
        
#starting game
run_game()
