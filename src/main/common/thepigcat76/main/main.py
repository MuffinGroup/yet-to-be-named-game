import pygame
import colors
import animations

class main():
    #Pygame initialization
    pygame.init()
    #Setup for fps
    Clock = pygame.time.Clock()
    
    #Loading assets
    character_image = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha() #Makes the background invisible
    background = pygame.image.load("src/main/assets/elements/background/hallway.jpg")
    floor = pygame.image.load("src\main/assets/elements/background/floor.jpg")
    door_closed = pygame.image.load("src\main/assets\elements\doors\Door_1_closed_Überarbeitet.png")
    icon = pygame.image.load('src/main/assets/gui/icon/icon.png')
    jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
    doorsound = pygame.mixer.Sound("src\main/assets\sounds\entities\Door_Closing.wav")

    #Assigning variables
    #Character dimensions
    characterWidth = 32
    characterHeight = 32
    
    #Art scale
    scale = 10

    #Screen dimensions
    screen_width = 1280
    screen_height = 800

    # Set initial position
    character_x = 150
    character_y = 410
    
    # Set character speed
    character_speed = 5
    
    #Values for animations
    IdleValue = 0
    WalkingValue = 0
    
    # Game loop
    running = True

    #Character attributes
    jumpvar = -16
    doorhandling = 0
    visible = True
    standing = True
    walking = False
    jumping = False

    #Game loop
    while running:
        