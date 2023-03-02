import pygame
import math
from colors import *

# Initialize Pygame
pygame.init()

# Define game window dimensions
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Load enemy image
enemy_img = pygame.image.load("src\main/assets\entities\enemies\Oger2.png")
enemy_img=pygame.transform.scale(enemy_img,(250,250))
screen.blit(enemy_img,(340,190))

# Define enemy class
class Enemy:
    def __init__(self, position, attack_range):
        self.position = position
        self.attack_range = attack_range
        self.speed = 10
    
    def update(self, player_position):
        dx = player_position[0] - self.position[0]
        dy = player_position[1] - self.position[1]
        distance = math.sqrt(dx**2 + dy**2)
        if distance != 0:
            self.position[0] += self.speed * dx / distance
            self.position[1] += self.speed * dy / distance
    
    def is_player_within_range(self, player_position):
        distance = math.sqrt((player_position[0] - self.position[0])**2 + (player_position[1] - self.position[1])**2)
        if distance <= self.attack_range:
            return True
        else:
            return False
    
    def attack(self):
        print("Enemy attacks!")
        
    def draw(self, surface):
        surface.blit(enemy_img, self.position)

# Initialize game window
screen = pygame.display.set_mode((screen_width, screen_height))

# Create enemy object
enemy = Enemy(position=[screen_width/2, screen_height/2], attack_range=10)

# Define game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get player position (in this example, it's the mouse position)
    player_position = pygame.mouse.get_pos()
    
    # Update enemy position
    enemy.update(player_position)
    
    # Check if player is within range
    if enemy.is_player_within_range(player_position):
        enemy.attack()
    
    # Draw game objects
    screen.fill(COLORS.WHITE)
    enemy.draw(screen)
    pygame.display.update()

    # Set game clock
    clock = pygame.time.Clock()
    clock.tick(60)

# Quit Pygame
pygame.quit()
