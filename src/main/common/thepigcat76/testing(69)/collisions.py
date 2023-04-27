import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
player = pygame.Rect((500, 100), (100, 100))
object = pygame.Rect((500, 50), (100, 200))
object2 = pygame.Rect((600, 200), (100, 200))

def collisions_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collisions_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collisions_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

moving_right = False
moving_left = False

player_y_momentum = 0
air_timer = 0


while True:
    tile_rects = [object, object2]
    key = pygame.key.get_pressed()

    player_movement = [0, 0]

    if moving_right:
        player_movement[0] += 2
    if moving_left:
        player_movement[0] -= 2
    player_movement[1] += player_y_momentum
    player_y_momentum += 0.2
    if player_y_momentum > 3:
        player_y_momentum = 3

    player, collisions = move(player, player_movement, tile_rects)

    if collisions['bottom']:
        player_y_momentum = 0
        air_timer = 0
    else:
        air_timer += 1

    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT: # check for window quit
            pygame.quit() # stop pygame
            exit() # stop script
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_UP:
                if air_timer < 6:
                    player_y_momentum = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_LEFT:
                moving_left = False

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 255, 0), object2, 100)
    pygame.draw.rect(screen, (255, 255, 0), object, 100)
    pygame.draw.rect(screen, (255, 0, 255), player, 100)
    pygame.display.update()