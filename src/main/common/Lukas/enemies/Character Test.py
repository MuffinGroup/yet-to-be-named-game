import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 640
screen_height = 480

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Load character image
character_image = pygame.image.load("src\main\common\Lukas\Pictures\.png")

# Set initial position
character_x = screen_width // 1
character_y = screen_height // 1

# Set character speed
character_speed = 1

# Game loop
running = True
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
    if keys[pygame.K_UP]:
        character_y -= character_speed
    if keys[pygame.K_DOWN]:
        character_y += character_speed

    # Draw the character and update the screen
    screen.blit(character_image, (character_x, character_y))
    pygame.display.update()

# Quit Pygame
pygame.quit()
