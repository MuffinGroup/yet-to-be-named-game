import pygame
import colors

pygame.init()
textfont = pygame.font.SysFont('joystixmonospaceregular', 20)
int10 = textfont.render('Hello!', True, colors.BLACK)
int11 = textfont.render('Nice to see you!', True, colors.BLACK)
int12 = textfont.render('In this game you will find', True, colors.BLACK)
int13 = textfont.render('some nice levels with enemies,', True, colors.BLACK)
int14 = textfont.render('interesting tasks and much more!', True, colors.BLACK)
int15 = textfont.render('Press Enter', True, colors.BLACK)

int20 = textfont.render('Before you start,', True, colors.BLACK)
int21 = textfont.render('you should learn how to move and act.', True, colors.BLACK)
int22 = textfont.render('I will explain this now', True, colors.BLACK)
int23 = textfont.render('Press Enter', True, colors.BLACK)

int30 = textfont.render('First we learn how to walk.', True, colors.BLACK)
int31 = textfont.render('To walk forward press RIGHT or d', True, colors.BLACK)
int32 = textfont.render('Great!', True, colors.BLACK)
int33 = textfont.render('To walk back press LEFT or a', True, colors.BLACK)
int33 = textfont.render('Well done!', True, colors.BLACK)



def introduction(screen):
    screen.blit(int10, (100,100))
    screen.blit(int11, (100,125))
    screen.blit(int12, (100,150))
    screen.blit(int13, (100,175))
    screen.blit(int14, (100,200))
    screen.blit(int15, (100,250))
    