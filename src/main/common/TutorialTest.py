import pygame
import math
import registries.colors
import registries.animations


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")
floor = pygame.image.load("src\main/assets/textures/elements/background/placeholder_floor.jpg")
door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_closed.png")

# Set screen dimensions
scale = 10
scale_bg = 3.25
scale_text = 0.4

# Set screen dimensions
screen_width = 1280
screen_height = 800
characterWidth = 32
characterHeight = 32

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load('src/main/assets/textures/elements/gui/icon/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

#Create Text
doorfont = pygame.font.Font('src/main/assets/fonts/joystixmonospaceregular.otf', 30)
text = doorfont.render('To Castle', True, registries.colors.BLACK)



#Create Sound
jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
jumpsound.set_volume(0.20)
doorsound = pygame.mixer.Sound("src\main/assets\sounds\Door_Closing.wav")

# Load character image
character_image = pygame.image.load("src/main/assets/textures/entities/characters/character_1/animations/character_1.png").convert_alpha()
character_image_inverted = pygame.transform.flip(character_image, True, False)
introducer_image = pygame.image.load("src/main/assets/textures/entities/npc/npc.png")

#Image dimensions
image_width = character_image.get_width()
image_height = character_image.get_height()
character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))
character_image_inverted = pygame.transform.scale(character_image_inverted, (int(image_width * scale), int(image_height * scale)))
door_width = door.get_width()
door_height = door.get_height()
door = pygame.transform.scale(door, (int(door_width * scale/2), int(door_height * scale/2)))
int_widht = introducer_image.get_width()
int_height = introducer_image.get_height()
introducer_image = pygame.transform.scale(introducer_image, (int(int_widht * scale), int(int_height * scale)))
background_widht = background.get_width()
background_height = background.get_height()
background = pygame.transform.scale(background, (int(background_widht * scale_bg), int(background_height * scale_bg)))
currentSprite = character_image

# Set initial position
character_x = 0
character_y = 410

# Set character speed
character_speed = 5


#define all functions

textfont = pygame.font.Font('src/main/assets/fonts/joystixmonospaceregular.otf', 20)

int10 = textfont.render('Hello!', True, registries.colors.BLACK)
int11 = textfont.render('Nice to see you!', True, registries.colors.BLACK)
int12 = textfont.render('In this game you will find', True, registries.colors.BLACK)
int13 = textfont.render('some nice levels with enemies,', True, registries.colors.BLACK)
int14 = textfont.render('interesting tasks and much more!', True, registries.colors.BLACK)
int15 = textfont.render('Press Enter', True, registries.colors.BLACK)

int20 = textfont.render('Before you start,', True, registries.colors.BLACK)
int21 = textfont.render('you should learn how to move and act.', True, registries.colors.BLACK)
int22 = textfont.render('I will explain this now', True, registries.colors.BLACK)
int23 = textfont.render('Press Enter', True, registries.colors.BLACK)

int30 = textfont.render('First we learn how to walk.', True, registries.colors.BLACK)
int31 = textfont.render('To walk forward press RIGHT or d', True, registries.colors.BLACK)
int32 = textfont.render('Great!', True, registries.colors.BLACK)
int33 = textfont.render('To walk back press LEFT or a', True, registries.colors.BLACK)
int34 = textfont.render('Well done!', True, registries.colors.BLACK)

int40 = textfont.render('If you want to be faster', True, registries.colors.BLACK)
int41 = textfont.render('you can press SHIFT to sprint.', True, registries.colors.BLACK)
int42 = textfont.render('That`s faster, right?', True, registries.colors.BLACK)

int50 = textfont.render('Sometimes you have to jump.', True, registries.colors.BLACK)
int51 = textfont.render('For this press UP or SPACE.', True, registries.colors.BLACK)
int52 = textfont.render('Nice jump!', True, registries.colors.BLACK)

int60 = textfont.render('Now you know how to move.', True, registries.colors.BLACK)
int61 = textfont.render('But of course there are some enemies.', True, registries.colors.BLACK)
int62 = textfont.render('So you have to attack them.', True, registries.colors.BLACK)
int63 = textfont.render('For this press F', True, registries.colors.BLACK)
int64 = textfont.render('Try it out on this oger!', True, registries.colors.BLACK)
int65 = textfont.render('Good job!', True, registries.colors.BLACK)

int70 = textfont.render('Now you got the controls.', True, registries.colors.BLACK)
int71 = textfont.render('If you are ready go to the door.', True, registries.colors.BLACK)
int72 = textfont.render('This door will bring you to the castle.', True, registries.colors.BLACK)
int73 = textfont.render('And now press DOWN or s', True, registries.colors.BLACK)
int74 = textfont.render('to start the game.', True, registries.colors.BLACK)
int75 = textfont.render('Good luck!', True, registries.colors.BLACK)


Info1 = True
Info2 = False
Info3_1 = False
Info3_2 = False
Info4_1 = False
Info4_2 = False
Info5_1 = False
Info5_2 = False
Info6_1 = False
Info6_2 = False
Info7 = False


def introduction():

    pygame.init()
    global character_x, character_y, character_speed, visible, walking, Info1, Info2, Info3_1, Info3_2, Info4_1, Info4_2, Info5_1,Info5_2, Info6_1,Info6_2, Info7
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)


    if Info1 == True:
        screen.blit(int10, (100,100))
        screen.blit(int11, (100,125))
        screen.blit(int12, (100,150))
        screen.blit(int13, (100,175))
        screen.blit(int14, (100,200))
        screen.blit(int15, (100,250))
        if keys[pygame.K_RETURN]:
            Info1 = False
            Info2 = True


    if Info2 == True:
        screen.blit(int20, (100,100))
        screen.blit(int21, (100,125))
        screen.blit(int22, (100,150))
        screen.blit(int23, (100,175))
        if keys[pygame.K_RETURN]:
            Info2 = False
            Info3_1 = True

    
    if Info3_1 == True:
        screen.blit(int30, (100,100))
        screen.blit(int31, (100,125))
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
        if character_x >= 300:
            Info3_1 = False
            Info3_2 = True
    
    if Info3_2 == True:
        screen.blit(int30, (100,100))
        screen.blit(int31, (100,125))
        screen.blit(int32, (100,150))
        screen.blit(int33, (100,175))
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
        if character_x <= 100:
            screen.blit(int34, (100,200))
            pygame.time.wait(500)
            standing = True
            walking = False
            Info3_2 = False
            Info4_1 = True

        
    if Info4_1 == True:
        screen.blit(int40, (100,100))
        screen.blit(int41, (100,125))
        if keys[pygame.K_LSHIFT] and keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
            character_speed = 7.5
            character_x -= character_speed
            standing = False
            walking = True
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
            character_speed = 7.5
            character_x += character_speed
            standing = False
            walking = True
        elif keys[pygame.K_RSHIFT] and keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
            character_speed = 7.5
            character_x += character_speed
            standing = False
            walking = True
        elif keys[pygame.K_RSHIFT] and keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
            character_speed = 7.5
            character_x -= character_speed
            standing = False
            walking = True
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
            character_speed = 7.5
            character_x += character_speed
            standing = False
            walking = True
        elif keys[pygame.K_LSHIFT] and keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
            character_speed = 7.5
            character_x -= character_speed
            standing = False
            walking = True
        elif keys[pygame.K_RSHIFT] and keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
            character_speed = 7.5
            character_x += character_speed
            standing = False
            walking = True
        elif keys[pygame.K_RSHIFT] and keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
            character_speed = 7.5
            character_x -= character_speed
            standing = False
            walking = True
        else:
            character_speed = 5
            standing = True
            walking = False
        if character_speed == 7.5 and character_x >= 500:
            Info4_1 = False
            Info4_2 = True
            standing = True
            walking = False
        
    if Info4_2 == True:
        screen.blit(int40, (100,100))
        screen.blit(int41, (100,125))
        screen.blit(int42, (100,150))
        pygame.time.wait(500)
        Info4_2 = False
        Info5_1 = True

    if Info5_1 == True:
        screen.blit(int50, (100,100))
        screen.blit(int51, (100,125))
        if keys[pygame.K_UP]:
            jumping = True
            jumpvar = -15
            Info5_1 = False
            Info5_2 = True
        elif keys[pygame.K_SPACE]:
            jumping = True
            jumpvar = -15
            Info5_1 = False
            Info5_2 = True
        else:
            jumping = False
            standing = True

    if Info5_2 == True:
        screen.blit(int50, (100,100))
        screen.blit(int51, (100,125))
        screen.blit(int52, (100,100))
        pygame.time.wait(500)
        Info5_2 = False
        Info6_1 = True
        

def draw():
    # Draw the character and update the screen
    screen.fill(registries.colors.BLACK)
    screen.blit(background, (-200,0))
    screen.blit(floor, (0,730))
    screen.blit(door, (990,420))
    screen.blit(introducer_image, (850, 400))
    screen.blit(text, (1030,310))
    introduction()

    if visible == True:
        screen.blit(character_image, (character_x, character_y))
    pygame.display.update()
    

value = 0
WalkingValue = 0


# Game loop
running = True
jumpvar = -16
doorhandling = 0
visible = True
standing = True
walking = False
jumping = False
while running:
    clock.tick(180)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            running = False
            pygame.quit()

    if value >= len(registries.animations.idle_sprite):
        value = 0

    currentSprite = registries.animations.idle_sprite[value]

    if WalkingValue >= len(registries.animations.walking_sprite):
        WalkingValue = 0
    
    if jumpvar == 15:
        pygame.mixer.Sound.play(jumpsound)

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        character_y -= (jumpvar**2)*0.17*n
        jumpvar -= 1

    if doorhandling == 1:
        door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_open.png")
        door = pygame.transform.scale(door, (int(door_width * scale/2), int(door_height * scale/2)))

    if walking == True:
        currentSprite = registries.animations.walking_sprite[WalkingValue]

    draw()
    currentSprite = pygame.transform.scale(currentSprite, (int(characterWidth * scale), int(characterHeight * scale)))    
    if visible == True:
        screen.blit(currentSprite, (character_x, character_y))
    pygame.display.update()

    if doorhandling == 1:
        pygame.time.wait(500)
        pygame.mixer.Sound.play(doorsound)
        door = pygame.image.load("src\main/assets/textures\elements\doors\door_1_closed.png")
        door = pygame.transform.scale(door, (int(door_width * scale/2), int(door_height * scale/2)))
        visible = False
        doorhandling = 0

    if standing == True:
        value += 1

    if walking == True:
        WalkingValue += 1

    clock.tick(69)