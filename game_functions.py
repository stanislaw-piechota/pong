import pygame
import sys
from random import randint
from time import sleep
from button1 import Button1
from pad import Pad

def check_events(settings, screen, pad, pad1, stats, start_button):
    #reacting for clicking
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    pad.moving_up = True
                elif event.key == pygame.K_s:
                    pad.moving_down = True
                elif event.key == pygame.K_q:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    pad1.moving_up = True
                elif event.key == pygame.K_DOWN:
                    pad1.moving_down = True

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                check_start_button(stats, start_button, mouse_x, mouse_y)

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    pad.moving_up = False
                elif event.key == pygame.K_s:
                    pad.moving_down = False
                elif event.key == pygame.K_UP:
                    pad1.moving_up = False
                elif event.key == pygame.K_DOWN:
                    pad1.moving_down = False

def check_start_button(stats, start_button, mouse_x, mouse_y):
    #checking if starting button is clicked
    if start_button.rect.collidepoint(mouse_x, mouse_y):
        stats.game_active = True

def update_screen(settings, screen, pad, pad1, ball, stats, start_button, sb,
                  sb1):
    #updating the screen
    screen.fill(settings.bg_color)
    ball.blitme()
    
    pad.draw_pad()
    pad1.draw_pad()
    sb.show_score()
    sb1.show_score()
    #drawing buttons in case of beggining and ending
    #then setting new game
    if not stats.game_active and (stats.a_hm < 5 or stats.b_hm < 5):
        start_button.draw_button()

    if stats.game_active and stats.a_hm == 5:
        sb.prep_score()
        sb.show_score()
        end_button = Button1(screen, settings, stats)
        end_button.draw_button()
        pygame.display.flip()
        stats.reset_stats(settings)
        sb.prep_score()
        sb.show_score()
        sb1.prep_score()
        sb1.show_score()
        sleep(3)
        pygame.display.flip()
        stats.game_active = False

    elif stats.game_active and stats.b_hm == 5:
        sb1.prep_score()
        sb1.show_score()
        end_button = Button1(screen, settings, stats)
        end_button.draw_button()
        pygame.display.flip()
        stats.reset_stats(settings)
        sb.prep_score()
        sb1.show_score()
        sb1.prep_score()
        sb.show_score()
        sleep(3)
        pygame.display.flip()
        stats.game_active = False

    pygame.display.flip()

def make_table():
    table=[]
    j = float(1)
    for i in range(0, 100, 1):
        table.append(j/100)
        j+=1
    return table

def make_x():
    #setting direction of ball's x
    dirx = 0
    while dirx == 0:
        dirx = randint(-1, 1)
    """rnd = randint(1, 2)
    if rnd == 1:
        dirx = 1
    else:
        dirx = -1"""
    return dirx

def make_y():
    #setting direction of ball's y
    diry = 0
    """table = make_table()
    rnd = randint(1, 2)
    if rnd == 1:
        rnd = randint(0, 99)
        diry = table[rnd]
    else:
        rnd = -1 * randint(0, 99)
        diry = table[rnd]"""
    while diry == 0:
        diry = randint(-1, 1)
    return float(diry)

def update_ball(ball, settings, pad, pad1, stats, sb, sb1):
    #updating ball's position on the screen
    ball.rect.centerx += settings.dirx
    ball.rect.centery += settings.diry
    check_collisions(ball, settings, pad, pad1, stats, sb, sb1)

def check_collisions(ball, settings, pad, pad1, stats, sb, sb1):
    #checking if ball is in collision with sth
    if ball.rect.top <= 0 or ball.rect.bottom >= 700:
        settings.diry = -1 * settings.diry
    elif pad.rect.colliderect(ball):
        settings.dirx = -1 * settings.dirx
    elif pad1.rect.colliderect(ball):
        settings.dirx = -1 * settings.dirx
    elif ball.rect.right >= 1200:
        stats.a_win = True
        stats.a_hm += 1
        reset_game(ball, pad, pad1, stats, sb, sb1)
    elif ball.rect.left <=0:
        stats.b_win = True
        stats.b_hm += 1
        reset_game(ball, pad, pad1, stats, sb, sb1)

def reset_game(ball, pad, pad1, stats, sb, sb1):
    #setting default position
    ball.rect.center = ball.screen_rect.center
    pad.rect.center = 50, 350
    pad1.rect.center = 1150, 350
    update_score(stats, sb, sb1)
    sleep(3)
    stats.a_win = False
    stats.b_win = False

def update_score(stats, sb, sb1):
    #updating scoreboards
    if stats.a_win:
        sb.prep_score()
    elif stats.b_win:
        sb1.prep_score()
















    
