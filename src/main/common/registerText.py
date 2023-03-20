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

int40 = textfont.render('If you want to be faster', True, colors.BLACK)
int41 = textfont.render('you can press SHIFT to sprint.', True, colors.BLACK)
int42 = textfont.render('That`s faster, right?', True, colors.BLACK)

int50 = textfont.render('Sometimes you have to jump.', True, colors.BLACK)
int51 = textfont.render('For this press UP or SPACE.', True, colors.BLACK)
int52 = textfont.render('Nice jump!', True, colors.BLACK)

int60 = textfont.render('Now you know how to move.', True, colors.BLACK)
int61 = textfont.render('But of course there are some enemies.', True, colors.BLACK)
int62 = textfont.render('So you have to attack them.', True, colors.BLACK)
int63 = textfont.render('For this press F', True, colors.BLACK)
int64 = textfont.render('Try it out on this oger!', True, colors.BLACK)
int65 = textfont.render('Good job!', True, colors.BLACK)

int70 = textfont.render('Now you got the controls.', True, colors.BLACK)
int71 = textfont.render('If you are ready go to the door.', True, colors.BLACK)
int72 = textfont.render('This door will bring you to the castle.', True, colors.BLACK)
int73 = textfont.render('And now press DOWN or s', True, colors.BLACK)
int74 = textfont.render('to start the game.', True, colors.BLACK)
int75 = textfont.render('Good luck!', True, colors.BLACK)


Info1 = 'on'
Info2 = 'off'
Info3 = 'off'
Info4 = 'off'
Info5 = 'off'
Info6 = 'off'
Info7 = 'off'


def introduction(running, jumpvar, doorhandling, visible, standing, walking, jumping, character_speed, character_x, character_y, leftWall, rightWall, screen):

    pygame.init()
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)

    global Info1, Info2, Info3, Info4, Info5, Info6, Info7

    if Info1 == 'on':
        screen.blit(int10, (100,100))
        screen.blit(int11, (100,125))
        screen.blit(int12, (100,150))
        screen.blit(int13, (100,175))
        screen.blit(int14, (100,200))
        screen.blit(int15, (100,250))
        if keys[pygame.K_KP_ENTER]:
            print('enter')
            Info1 = 'off'
            Info2 = 'on'

    if Info2 == 'on':
        screen.blit(int20, (100,100))
        screen.blit(int21, (100,125))
        screen.blit(int22, (100,150))
        screen.blit(int23, (100,175))
        