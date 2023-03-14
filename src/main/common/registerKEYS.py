import pygame

def keyinput():
    # Set initial position
    character_x = 0
    character_y = 410

    screen_width = 1280
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
    rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

    running = True
    jumpvar = -16
    doorhandling = 0
    visible = True
    standing = True
    walking = False
    jumping = False

    # Handle keyboard input
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)

    if keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
        standing = False
        walking = True
        character_x -= character_speed
    elif keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
        standing = False
        walking = True
        character_x -= character_speed
    else:
        standing = True
        walking = False

    if keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
        standing = False
        walking = True
        character_x += character_speed
    elif keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
        standing = False
        walking = True
        character_x += character_speed
    else:
        standing = True
        walking = False

    if keys[pygame.K_UP] and jumpvar == -16 and visible == True:
        standing = False
        jumping = True
        jumpvar = 15
    elif keys[pygame.K_SPACE] and jumpvar == -16 and visible == True:
        standing = False
        jumping = True
        jumpvar = 15

    if keys[pygame.K_DOWN] and Spieler.colliderect(Door) and visible == True:
        doorhandling = 1
    elif keys[pygame.K_s] and Spieler.colliderect(Door) and visible == True:
        doorhandling = 1

    if keys[pygame.K_LSHIFT] and keys[pygame.K_a] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_LSHIFT] and keys[pygame.K_d] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_RSHIFT] and keys[pygame.K_d] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_RSHIFT] and keys[pygame.K_a] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_RSHIFT] and keys[pygame.K_RIGHT] and visible == True:
        character_speed = 7.5
    elif keys[pygame.K_RSHIFT] and keys[pygame.K_LEFT] and visible == True:
        character_speed = 7.5
    else:
        character_speed = 5