import pygame
import registerEnemies
import registerPlayer
from colors import *


# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

#Load background
background = pygame.image.load("src/main/assets/background/hallway.jpg")
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
leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

#Create Sound
jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
jumpsound.set_volume(0.01)

# Load character image
character_image = pygame.image.load("src/main/assets/characters/Character1/Animations/Character1.png").convert_alpha()

#Register Enemies
enemy = registerEnemies.enemies("oger", 275, 650, 10)
player = registerPlayer.player("Character1", 475, 570, 10)

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
    screen.fill(COLORS.BLACK)
    screen.blit(background, (0,0))
    screen.blit(floor, (0,730))
    enemy.draw(screen)
    player.draw(screen, character_x, character_y, 10, jumpsound)
    pygame.display.update()

running = True
while running:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw()
    clock.tick(60)

# Quit Pygame
pygame.quit()