import pygame

# Initialize Pygame
pygame.init()

#Load background
background = pygame.image.load("src/main/assets/background/floor - 1280 x 853.jpg")

# Set screen dimensions
scale = 10

# Set screen dimensions
screen_width = 1920
screen_height = 1280

# Create a screen surface
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
pygame.display.set_caption("Muffin Group")

# Load character image
character_image = pygame.image.load("src/main/assets/characters/Character1/Character1.png").convert_alpha()
#Image dimensions
image_width = character_image.get_width()
image_height = character_image.get_height()
character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))

# Set initial position
character_x = screen_width // 6
character_y = screen_height // 6

# Set character speed
character_speed = 5

def draw():
    # Draw the character and update the screen
    screen.blit(background, (0,0))
    screen.blit(character_image, (character_x, character_y))
    pygame.display.update()


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

    draw()

# Quit Pygame
pygame.quit()
