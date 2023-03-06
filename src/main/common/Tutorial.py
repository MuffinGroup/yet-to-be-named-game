import pygame
import math
from colors import *
import animations
import registerIdles


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src\main/assets\elements/background\Tutorial.jpg")
floor = pygame.image.load("src\main/assets/elements/background/floor.jpg")
door = pygame.image.load("src/main/assets/elements/doors/door_1_closed.png")
text = pygame.image.load("src\main/assets\gui/texts\Text.png")

# Set screen dimensions
scale = 10
scale_bg = 1.5
scale_text = 0.4

# Set screen dimensions
screen_width = 1280
screen_height = 800
characterWidth = 32
characterHeight = 32

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load('src/main/assets/gui/icon/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

#Create Sound
jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
jumpsound.set_volume(0.20)
doorsound = pygame.mixer.Sound("src\main/assets\sounds\entities\Door_Closing.wav")

# Load character image
character_image = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha()
character_image_inverted = pygame.transform.flip(character_image, True, False)
introducer_image = pygame.image.load("src/main/assets/entities/enemies/Oger2.png")

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
text_widht = text.get_width()
text_height = text.get_height()
text = pygame.transform.scale(text, (int(text_widht * scale_text), int(text_height * scale_text)))
current_sprite = character_image

# Set initial position
character_x = 0
character_y = 410

# Set character speed
character_speed = 5

def draw():
    # Draw the character and update the screen
    screen.fill(COLORS.BLACK)
    screen.blit(background, (0,0))
    screen.blit(floor, (0,730))
    screen.blit(door, (990,420))
    screen.blit(text, (865, 220))
    screen.blit(introducer_image, (100, 150))
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

    if value >= len(animations.idle_sprite):
        value = 0

    currentSprite = animations.idle_sprite[value]

    if WalkingValue >= len(animations.walking_sprite):
        WalkingValue = 0
    
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

    if jumpvar == 15:
        pygame.mixer.Sound.play(jumpsound)

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        character_y -= (jumpvar**2)*0.17*n
        jumpvar -= 1

    if doorhandling == 1:
        door = pygame.image.load("src/main/assets/elements/doors/door_1_open.png")
        door = pygame.transform.scale(door, (int(door_width * scale/2), int(door_height * scale/2)))

    if walking == True:
        currentSprite = animations.walking_sprite[WalkingValue]

    draw()
    currentSprite = pygame.transform.scale(currentSprite, (int(characterWidth * scale), int(characterHeight * scale)))    
    if visible == True:
        screen.blit(currentSprite, (character_x, character_y))
    pygame.display.update()

    if doorhandling == 1:
        pygame.time.wait(500)
        pygame.mixer.Sound.play(doorsound)
        door = pygame.image.load("src\main/assets\elements\doors\door_1_closed.png")
        door = pygame.transform.scale(door, (int(door_width * scale/2), int(door_height * scale/2)))
        visible = False
        doorhandling = 0

    if standing == True:
        value += 1

    if walking == True:
        WalkingValue += 1

    clock.tick(69)