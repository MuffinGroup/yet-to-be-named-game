import pygame
import colors
import animations


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")
floor = pygame.image.load("src\main/assets/textures/elements/background/placeholder_floor.jpg")
door = pygame.image.load("src/main/assets/textures/elements/doors/door_1_closed.png")

# Set screen dimensions (I'd suggest the Nether Dimension..........................btw, this is the 500th commit)
scale = 10
scale_bg = 3.25

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
doorfont = pygame.font.SysFont('joystixmonospaceregular', 30)
text = doorfont.render('To Castle', True, colors.BLACK)



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
current_sprite = character_image

# Set initial position
character_x = 0
character_y = 410

# Set character speed
character_speed = 5

def draw():
    # Draw the character and update the screen
    screen.fill(colors.BLACK)
    screen.blit(background, (-200,0))
    screen.blit(floor, (0,730))
    screen.blit(door, (990,420))
    screen.blit(introducer_image, (850, 400))
    screen.blit(text, (1030,310))

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
        currentSprite = animations.walking_sprite[WalkingValue]

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
