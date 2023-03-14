import pygame
from colors import *


def introduction():
    textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
    int10 = textfont.render('Hello!', True, COLORS.BLACK)
    int11 = textfont.render('Nice to see you!', True, COLORS.BLACK)
    int12 = textfont.render('In this game you will find', True, COLORS.BLACK)
    int13 = textfont.render('some nice levels with enemies,', True, COLORS.BLACK)
    int14 = textfont.render('interesting tasks and much more!', True, COLORS.BLACK)
    int15 = textfont.render('Next: Enter')