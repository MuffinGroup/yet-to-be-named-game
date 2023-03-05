import pygame
from colors import *


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src/main/assets/elements/background/hallway.jpg")
floor = pygame.image.load("src\main/assets/elements/background/floor.jpg")
door = pygame.image.load("src/main/assets/elements/doors/door_1_closed.png")

characterWidth = 32
characterHeight = 32

scale = 10

idle_sprite0 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(1).png")
idle_sprite1 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(2).png")
idle_sprite2 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(3).png")
idle_sprite3 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(4).png")
idle_sprite4 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(5).png")
idle_sprite5 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(6).png")
idle_sprite6 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(7).png")
idle_sprite7 = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1Idle/1Idle(8).png")

walking_sprite0 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(1).png")
walking_sprite1 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(2).png")
walking_sprite2 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(3).png")
walking_sprite3 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(4).png")
walking_sprite4 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(5).png")
walking_sprite5 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(6).png")
walking_sprite6 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(7).png")
walking_sprite7 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(8).png")
walking_sprite8 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(9).png")
walking_sprite9 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(10).png")
walking_sprite10 = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1running/1Running(11).png")

idle_sprite = [idle_sprite0, idle_sprite1, idle_sprite2, idle_sprite3, idle_sprite4, idle_sprite5, idle_sprite6, idle_sprite7]
walking_sprite = [walking_sprite0, walking_sprite1, walking_sprite2, walking_sprite3, walking_sprite4, walking_sprite5, walking_sprite6, walking_sprite7, walking_sprite8, walking_sprite9, walking_sprite10]
# Set screen dimensions
scale = 10

# Set screen dimensions
screen_width = 1280
screen_height = 800

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load('src/main/assets/gui/icon/icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

#Create Sound
jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
jumpsound.set_volume(0.25)
doorsound = pygame.mixer.Sound("src\main/assets\sounds\entities\Door_Closing.wav")

# Load character image
character_image = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha()
character_image_inverted = pygame.transform.flip(character_image, True, False)

#Image dimensions
image_width = character_image.get_width()
image_height = character_image.get_height()
character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))
character_image_inverted = pygame.transform.scale(character_image_inverted, (int(image_width * scale), int(image_height * scale)))
door_width = door.get_width()
door_height = door.get_height()
door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))
currentSprite = character_image
# Sizes door: 320, 320

# Set initial position
character_x = 150
character_y = 410

# Set character speed
character_speed = 5

def draw():
    # Draw the character and update the screen
    screen.fill(COLORS.BLACK)
    screen.blit(background, (0,0))
    screen.blit(floor, (0,730))
    screen.blit(door, (990,410))

value = 0
WalkingValue = 0

# Game loop
running = True
jumpvar = -16
doorhandling = 0
visible = True
standing = True
walking = False
while running:
    clock.tick(180)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    if value >= len(idle_sprite):
        value = 0

    currentSprite = idle_sprite[value]

    if value >= len(walking_sprite):
        value = 0
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    Spieler = pygame.Rect(character_x, character_y, 40, 80)
    Door = pygame.Rect(990, 410, 40, 80)
    if keys[pygame.K_LEFT] or keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
        standing = False
        walking = True
        character_x -= character_speed
    else:
        standing = True
    if keys[pygame.K_RIGHT] or keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
        standing = False
        walking = True
        character_x += character_speed
    else:
        standing = True
    if keys[pygame.K_UP] and jumpvar == -16 and visible == True:
        standing = False
        jumpvar = 15
    elif keys[pygame.K_SPACE] and jumpvar == -16 and visible == True:
        jumpvar = 15
    if keys[pygame.K_DOWN] or keys[pygame.K_s] and Spieler.colliderect(Door) and visible == True:
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
        door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))

    draw()
    currentSprite = pygame.transform.scale(currentSprite, (int(characterWidth * scale), int(characterHeight * scale)))    
    if visible == True:
        screen.blit(currentSprite, (character_x, character_y))
    pygame.display.update()

    if doorhandling == 1:
        pygame.time.wait(500)
        pygame.mixer.Sound.play(doorsound)
        door = pygame.image.load("src/main/assets/elements/doors/door_1_closed.png")
        door = pygame.transform.scale(door, (int(door_width * scale), int(door_height * scale)))
        visible = False
        doorhandling = 0

    if standing == True:
        pygame.time.delay(180)
        value += 1

    if walking == True:
        pygame.time.delay(180)
        WalkingValue += 1

    clock.tick(69)

# Quit Pygame