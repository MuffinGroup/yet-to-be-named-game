import pygame
from colors import*

# Initialize Pygame
pygame.init()
clock=pygame.time.Clock()

# Set screen dimensions
screen_width = 1000
screen_height = 600

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height))

# Load character image
character_image = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1.png").convert_alpha()
character_image=pygame.transform.scale(character_image,(250,250))
screen.blit(character_image,(340,190))

# Set initial position
character_x = screen_width // 10
character_y = screen_height // 10


# Set character speed
character_speed =40

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
     screen.fill(COLORS.GRAY)
     screen.blit(character_image, (character_x, character_y))
     pygame.display.update()
     clock.tick(60)

pygame.quit()
