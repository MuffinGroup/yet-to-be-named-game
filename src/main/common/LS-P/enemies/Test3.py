import pygame
import random

# initialize pygame
pygame.init()

# set up the window
window_width = 1000
window_height = 700
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Collect Items Game")

# load the graphics for the character and the items
character_image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png")
character_image=pygame.transform.scale(character_image,(250,250))
character_image.blit(character_image,(340,190))
character_rect = character_image.get_rect()
character_rect.center = (window_width // 2, window_height // 2)

item_images = [pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png"), pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy - Kopie.png")]
item_rects = []
for i in range(10):
    item_rect = item_images[i % len(item_images)].get_rect()
    item_rect.center = (random.randint(50, window_width - 50), random.randint(50, window_height - 50))
    item_rects.append(item_rect)

# set up the font for the inventory display
font = pygame.font.SysFont(None, 30)

# set up the variables for the game loop
inventory = [None] * 4  # an empty inventory
inventory_rects = []  # the rects for displaying the inventory
for i in range(4):
    rect = pygame.Rect(50 + i * 80, 10, 70, 70)
    inventory_rects.append(rect)

item_counts = [0] * 4  # a list to store the count of items in each field of the inventory
all_items_collected = False  # a flag for whether all items have been collected

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # check for collision between the character and the items
    for i, item_rect in enumerate(item_rects):
        if character_rect.colliderect(item_rect):
            # add the item to the inventory
            for j in range(len(inventory)):
                if inventory[j] is None:
                    inventory[j] = item_images[i % len(item_images)]
                    item_counts[j] += 1
                    if all(count == 1 for count in item_counts):
                        all_items_collected = True
                    break
            item_rect.center = (random.randint(50, window_width - 50), random.randint(50, window_height - 50))

    # handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
        character_rect.move_ip(5, 0)
    if keys[pygame.K_UP]:
        character_rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
        character_rect.move_ip(0, 5)

    # draw the graphics
    game_window.fill((255, 255, 255))
    game_window.blit(character_image, character_rect)
    for item_rect in item_rects:
        game_window.blit(item_images[0], item_rect)  # only display the first item image for all items
    for i, item in enumerate(inventory):
        if item is not None:
            inventory_rect = inventory_rects[i]
            game_window.blit(item, inventory_rect)
            count_text = font.render(str(item_counts[i]), True, (0, 0, 0))
            count_rect = count_text.get_rect(center=inventory_rect.center)
            game_window.blit(count_text, count_rect)

    # check if all items have been collected
    if all_items_collected:
     count_text = font.render(f"All items collected: {sum(item_counts)}", True, (0, 0, 0))
     count_rect = count_text.get_rect(center=(window_width // 2, window_height - 30))
     game_window.blit(count_text, count_rect)

pygame.display.update()
