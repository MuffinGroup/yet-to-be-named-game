
import pygame
import random

# Initialize Pygame
pygame.init()
clock=pygame.time.Clock()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set window title
pygame.display.set_caption("Collect Testing")

# Load character image
character_image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png").convert_alpha()
character_image=pygame.transform.scale(character_image,(250,250))
screen.blit(character_image,(340,190))
character_rect = character_image.get_rect()

# Load item image
item_image = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png").convert_alpha()
item_image=pygame.transform.scale(item_image,(250,250))
screen.blit(item_image,(340,190))
item_rect = item_image.get_rect()

#Starting position
character_x = 50
character_y = 50

# Set initial position of character and item
character_rect.centerx = SCREEN_WIDTH // 2
character_rect.centery = SCREEN_HEIGHT // 2
item_rect.centerx = random.randint(0, SCREEN_WIDTH)
item_rect.centery = random.randint(0, SCREEN_HEIGHT)

# Set initial score to zero
score = 0

#Set character speed
character_speed= 2

# Create font object
font = pygame.font.Font(None, 36)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            quit()
    
    
    # Handle events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
     character_x -= character_speed
    if keys[pygame.K_RIGHT]:
     character_x += character_speed
    if keys[pygame.K_UP]:
     character_y -= character_speed
    if keys[pygame.K_DOWN]:
      character_y += character_speed

    # Check if character is colliding with item
    if character_rect.colliderect(item_rect):
        # Update score
        score += 1
        # Move item to new random position
        item_rect.centerx = random.randint(0, SCREEN_WIDTH)
        item_rect.centery = random.randint(0, SCREEN_HEIGHT)

    # Fill screen with white color
    screen.fill(WHITE)

    # Draw character and item
    screen.blit(character_image,(character_x, character_y), character_rect)
    screen.blit(item_image, item_rect)

    # Draw score on screen
    score_text = font.render("Items Collected: {}".format(score), True, BLACK)
    screen.blit(score_text, (10, 10))

    # Update screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()

