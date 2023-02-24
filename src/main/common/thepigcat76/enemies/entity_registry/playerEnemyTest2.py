import pygame
import registerEnemies
import registerPlayer
from colors import*
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enemy Following Game")

# Set up the clock
clock = pygame.time.Clock()

jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
jumpsound.set_volume(0.25)

character_x = 0
character_y = 410

# Set up the character and enemy images
character_img = pygame.image.load("src\main\common\LS-P\Pictures\Character1.copy.png")
character_img=pygame.transform.scale(character_img,(250,250))
screen.blit(character_img,(character_x, character_y))
enemy_img = pygame.image.load("src\main\common\LS-P\Pictures\Oger2.png")
enemy_img=pygame.transform.scale(enemy_img,(400,400))
screen.blit(enemy_img,(340,190))

# Set up the character and enemy positions
character_pos = [width/2, height/2]
enemy_pos = [width/2 + 100, height/2 + 100]

# Set up the character and enemy speeds
character_speed = 5
enemy_speed = 2


# Set up the attack range
attack_range = 50

# Game loop
jumpvar = -16
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Move the character based on user input
    keys = pygame.key.get_pressed()
    Player = pygame.Rect(character_x, character_y, 40, 80)
    if keys[pygame.K_LEFT]:
        character_pos[0] -= character_speed
    if keys[pygame.K_RIGHT]:
        character_pos[0] += character_speed
    if keys[pygame.K_UP] and jumpvar == -16:
        jumpvar = 15

    if jumpvar == 15:
        pygame.mixer.Sound.play(jumpsound)

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        character_pos[1] -= (jumpvar**2)*0.17*n
        jumpvar -= 1
    # Calculate the distance between the character and the enemy
    distance = math.sqrt((character_pos[0] - enemy_pos[0])**2 + (character_pos[1] - enemy_pos[1])**2)
    
    # If the enemy is too close to the character, follow the character
    if distance < 200:
        enemy_dir = [character_pos[0] - enemy_pos[0], character_pos[1] - enemy_pos[1]]
        enemy_dir_norm = math.sqrt(enemy_dir[0]**2 + enemy_dir[1]**2)
        enemy_dir_unit = [enemy_dir[0]/enemy_dir_norm, enemy_dir[1]/enemy_dir_norm]
        enemy_pos[0] += enemy_speed * enemy_dir_unit[0]
        enemy_pos[1] += enemy_speed * enemy_dir_unit[1]
    
    # If the enemy is in range of the character, attack the character
    if distance < attack_range:
        # TODO: Implement attack logic
    
    # If the character is in range of the enemy, attack the enemy
        if distance < attack_range:
        # TODO: Implement attack logic
    
    # Clear the screen
            screen.fill((158,158,158))
    
    # Draw the character and enemy on the screen
    screen.blit(character_img, (character_pos[0]-character_img.get_width()/2, character_pos[1]-character_img.get_height()/2))
    screen.blit(enemy_img, (enemy_pos[0]-enemy_img.get_width()/2, enemy_pos[1]-enemy_img.get_height()/2))
    
    # Update the display
    pygame.display.update()
    screen.fill(COLORS.GRAY)
    
    # Limit the frame rate
    clock.tick(60)