import pygame
import colors


def introduction():
    textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
    int10 = textfont.render('Hello!', True, colors.BLACK)
    int11 = textfont.render('Nice to see you!', True, colors.BLACK)
    int12 = textfont.render('In this game you will find', True, colors.BLACK)
    int13 = textfont.render('some nice levels with enemies,', True, colors.BLACK)
    int14 = textfont.render('interesting tasks and much more!', True, colors.BLACK)
    int15 = textfont.render('Press Enter', True, colors.BLACK)

    screen_width = 1280
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

    screen.blit(int10, (100,100))
    screen.blit(int11, (100,125))
    screen.blit(int12, (100,150))
    screen.blit(int13, (100,175))
    screen.blit(int14, (100,200))
    screen.blit(int15, (100,225))
    