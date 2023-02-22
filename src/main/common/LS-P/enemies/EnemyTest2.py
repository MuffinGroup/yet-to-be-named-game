import pygame
import math

# Initialize Pygame
pygame.init()

# Set screen size
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load images
character_img = pygame.image.load("src\main\common\LS-P\Pictures\Character1.copy.png")
character_img=pygame.transform.scale(character_img,(250,250))
screen.blit(character_img,(340,190))
enemy_img = pygame.image.load("src\main\common\LS-P\Pictures\Oger.gif")

# Set character and enemy starting position
character_x = 50
character_y = 50
enemy_x = 400
enemy_y = 300

# Set enemy speed
enemy_speed = 2
character_img_speed=0.5

# Set distance at which enemy starts attacking character
attack_distance = 400

# Set enemy attack range
attack_range = 40

# Set character health and attack power
character_health = 500
character_attack_power = 20

# Set enemy health and attack power
enemy_health = 50
enemy_attack_power = 10

# Define function to calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get character movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_x -= 3
    if keys[pygame.K_RIGHT]:
        character_x += 3
    if keys[pygame.K_UP]:
        character_y -= 3
    if keys[pygame.K_DOWN]:
        character_y += 3

    # Move enemy towards character
    enemy_dx = character_x - enemy_x
    enemy_dy = character_y - enemy_y
    distance_to_character = distance(character_x, character_y, enemy_x, enemy_y)
    if distance_to_character < attack_distance:
        # If within attack distance, attack character
        if distance_to_character < attack_range:
            character_health -= enemy_attack_power
        # Otherwise, move towards character
        else:
            enemy_dx = enemy_dx / distance_to_character * enemy_speed
            enemy_dy = enemy_dy / distance_to_character * enemy_speed
            enemy_x += enemy_dx
            enemy_y += enemy_dy

    # Draw images on screen
    screen.fill((255, 255, 255))
    screen.blit(character_img, (character_x, character_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))

    # Display health bars for character and enemy
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, character_health, 10))
    pygame.draw.rect(screen, (255, 0, 0), (screen_width - 110, 10, enemy_health, 10))

    # Check if character or enemy health is 0 or below, end game if true
    if character_health <= 0 or enemy_health <= 0:
        pygame.quit()
        quit()

    # Update display
    pygame.display.update()
