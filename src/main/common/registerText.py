import pygame
from colors import *


def introduction():
    textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
    int10 = textfont.render('Hello!', True, COLORS.BLACK)
    int11 = textfont.render('Nice to see you!', True, COLORS.BLACK)
