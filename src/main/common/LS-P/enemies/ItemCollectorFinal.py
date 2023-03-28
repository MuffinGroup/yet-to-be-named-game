import pygame
import random

# initialize pygame
pygame.init()

# set up the game window
window_width = 1200
window_height = 700
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Collect Items Game")

# set up the character and items
character_image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png")
character_image=pygame.transform.scale(character_image,(250,250))
character_image.blit(character_image,(340,190))
currenSprite = character_image
currenSprite = pygame.transform.scale(currenSprite,(250,250))
character_rect = character_image.get_rect()
character_rect.center = (window_width//2, window_height//2)
item_images = [pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png"), pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy - Kopie.png")]
item_rects = []
for i in range(5):
    item_rect = item_images[i % len(item_images)].get_rect()
    item_rect.center = (random.randint(50, window_width-50), random.randint(50, window_height-50))
    item_rects.append(item_rect)

# set up the font for the display
font = pygame.font.SysFont(None, 30)

# set up variables for the game loop
score = 0
game_running = True

# define a function to check if the character has collided with an item
def check_collision(character_rect, item_rects):
    for item_rect in item_rects:
        if character_rect.colliderect(item_rect):
            item_rects.remove(item_rect)
            return True
    return False

# game loop
while game_running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    character_image.blit(character_image,(340,190))
       
    
    # handle key presses to move the character
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.move_ip(-1, 0)
    if keys[pygame.K_RIGHT]:
        character_rect.move_ip(1, 0)
    if keys[pygame.K_UP]:
        character_rect.move_ip(0, -1)
    if keys[pygame.K_DOWN]:
        character_rect.move_ip(0, 1)
        
    # check for collision with items
    if check_collision(character_rect, item_rects):
        score += 1
    
    # draw the game
    game_window.fill((255, 255, 255))
    game_window.blit(character_image, character_rect)
    for item_rect in item_rects:
        game_window.blit(item_images[item_rects.index(item_rect) % len(item_images)], item_rect)
    score_display = font.render("Items Collected: {}".format(score), True, (0, 0, 0))
    game_window.blit(score_display, (10, 10))
    pygame.display.update()

# quit pygame
pygame.quit()
