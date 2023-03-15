import pygame
import colors


def introduction():
    textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
    int10 = textfont.render('Hello!', True, colors.BLACK)
    int11 = textfont.render('Nice to see you!', True, colors.BLACK)
    int12 = textfont.render('In this game you will find', True, colors.BLACK)
    int13 = textfont.render('some nice levels with enemies,', True, colors.BLACK)
    int14 = textfont.render('interesting tasks and much more!', True, colors.BLACK)
    int15 = textfont.render('Next: Enter')
