import pygame
from colors import *


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src/main/assets/background/floor - 1280 x 853.jpg")
floor = pygame.image.load("src/main/assets/background/boden.jpg")

# Set screen dimensions
scale = 10

# Set screen dimensions
screen_width = 1280
screen_height = 800

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
icon = pygame.image.load('src//main//assets//gui//icon//icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, (0,0,0), (-2,0,2,600), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1201,0,2,600), 0)

# Load character image
character_image = pygame.image.load("src/main/assets/characters/Character1/Animations/Character1.png").convert_alpha()

#Image dimensions
image_width = character_image.get_width()
image_height = character_image.get_height()
character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))

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
    screen.blit(character_image, (character_x, character_y))
    pygame.display.update()


# Game loop
running = True
jumpvar = -16
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= character_speed
    if keys[pygame.K_RIGHT]:
        character_x += character_speed
    if keys[pygame.K_UP] and jumpvar == -16:
        jumpvar = 15

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        character_y -= (jumpvar**2)*0.17*n
        jumpvar -= 1

    draw()
    clock.tick(60)

# Quit Pygame
pygame.quit()
