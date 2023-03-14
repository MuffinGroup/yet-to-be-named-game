import pygame
import colors


def introduction():
    textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
    int10 = textfont.render('Hello!', True, colors.BLACK)
    int11 = textfont.render('Nice to see you!', True, colors.BLACK)
