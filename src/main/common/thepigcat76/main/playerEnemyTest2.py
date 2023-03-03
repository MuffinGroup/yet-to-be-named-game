import pygame
import registerDoors
import registerEnemies
import registerPlayer
from colors import*
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
scaleDoor = 10
scalePopUps = 3
doorClosedSprite = pygame.image.load('src/main/assets/elements/doors/door_1_closed.png')
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Muffin Group")
leftWall = pygame.draw.rect(screen, COLORS.BLACK, (0,0,2,1000), 0)
rightWall = pygame.draw.rect(screen, COLORS.BLACK, (1100,0,2,1000), 0)
door = pygame.draw.rect(screen, COLORS.BLACK, (1100,0,2,1000), 0)

# Set up the clock
clock = pygame.time.Clock()

jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
jumpsound.set_volume(0.25)

character_x = 0
character_y = 410

# Set up the character and enemy images
character_img = pygame.image.load("src\main/assets/entities/characters/Character1/Animations/Character1.png")
press_o = pygame.image.load('src/main/assets/gui/icon/press_o.png')
character_img=pygame.transform.scale(character_img,(250,250))
screen.blit(character_img,(character_x, character_y))
enemy1 = registerEnemies.enemies("oger", 275, 650, 10)
enemy_img = pygame.image.load("src\main/assets\entities\enemies\Oger2.png")
enemy_img=pygame.transform.scale(enemy_img,(400,400))
screen.blit(enemy_img,(340,190))
door_width = doorClosedSprite.get_width()
door_height = doorClosedSprite.get_height()
door_x = 100
door_y = 105
doorClosedSprite = pygame.transform.scale(doorClosedSprite, (int(door_width * scaleDoor), int(door_height * scaleDoor)))
press_o = pygame.transform.scale(press_o, (int(door_width * scalePopUps), int(door_height * scalePopUps)))
rect = doorClosedSprite.get_rect()
doorClosed = pygame.Rect(400, 200, 80, 80)

# Set up the character and enemy positions
character_pos = [width/2, height/2]
enemy_pos = [width/2 + 100, height/2 + 100]

# Set up the character and enemy speeds
character_speed = 5
enemy_speed = 2


# Set up the attack range
attack_range = 50

print(door_height)
print(door_width)
# Game loop
jumpvar = -16
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    Mousepos = pygame.mouse.get_pos()
    # Move the character based on user input
    keys = pygame.key.get_pressed()
    Player = pygame.Rect(character_x, character_y, 150, 1000)
    if keys[pygame.K_LEFT]:
        rect.x -= character_speed
    if keys[pygame.K_RIGHT]:
        rect.x += character_speed
    if keys[pygame.K_UP] and jumpvar == -16:
        jumpvar = 15
    if jumpvar == 15:
        pygame.mixer.Sound.play(jumpsound)

    if jumpvar >= -15:
        n = 1
        if jumpvar < 0:
            n = -1
        rect.y -= (jumpvar**2)*0.17*n
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

    if rect.colliderect(doorClosed):
        print("success")

    # Draw the character and enemy on the screen
    screen.blit(character_img, rect)
    enemy1.draw(screen, (enemy_pos[0]-enemy_img.get_width()/2, enemy_pos[1]-enemy_img.get_height()/2))
    screen.blit(press_o, (100, 100))
    pygame.draw.rect(screen, (0,0,0), doorClosed, 4)
    
    # Update the display
    pygame.display.update()
    screen.fill(COLORS.GRAY)
    
    # Limit the frame rate
    clock.tick(60)