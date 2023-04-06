import pygame
import registries.colors
import registries.animations
import registries.elements
import registries.buttons
from pygame.locals import *

#pygame initialization
pygame.init()
class Player:
    #Initial Player attribute assignment
    def __init__(currentImage):
        Player.defaultSpeed = 10
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.speed = Player.defaultSpeed
        Player.jumpvar = -16 #Important for jumping calculation
        Player.facingRight = True
        Player.facingLeft = False
        Player.standing = True
        Player.jumping = False
        Player.walking = False
        Player.collidingLeft = False
        Player.collidingRight = False
        Player.rect = pygame.Rect((180,301),(100, 200)) # Create the players hitbox
        Player.animationFrameUpdate = 1
        Player.debuggingMode = False
        Player.visible = True
        Player.locked = False
        Player.debuggingMenu = False
        Player.test = False
        Player.flying = 0
        Player.colliding = 0
        Player.allowJump = True

    
#Loading element textures
placeholder = registries.elements.registerElements("environment/blocks/cobble", 5)
wooden_sign = registries.elements.registerElements("environment/blocks/wooden_sign", 5)
tree_stump = registries.elements.registerElements("environment/blocks/tree_stump", 5)
placeholder3 = registries.elements.registerElements("environment/blocks/cobble", 5)

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','2','2','2','2','2','0','0','0','0','0','0','0'],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
            ['2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','2','2'],
            ['1','1','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1'],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

print(tree_stump.get_width())

#Loading element hitboxes
placeholder_hitbox = pygame.Rect((400, 750),(int(placeholder.get_width()), int(placeholder.get_height())))
tree_stump_hitbox = pygame.Rect((800, 730),(int(placeholder.get_width()), int(placeholder.get_width())))

grassElement = pygame.image.load("src\main/assets/textures\elements\Environment\Blocks\grass_dirt.png")
grass_width = grassElement.get_width()
grass_height = grassElement.get_height()

dirtElement = pygame.image.load("src\main/assets/textures\elements\Environment\Blocks\Dirt.png")
dirt_width = dirtElement.get_width()
dirt_height = dirtElement.get_height()

font = pygame.font.SysFont('joystixmonospaceregular', 25)
text = font.render('Press 0 to open/close the debug menu', True, registries.colors.DARK_ORANGE)

debug_menu = pygame.Rect((70, 70), (300, 400))

toggleCollisionsText = font.render('collides', True, registries.colors.BLACK)
toggleCollisions = registries.buttons.registerButton("toggle", 300, 250,  12.0, "", registries.colors.BLACK, "")

toggleAdvMoveText = font.render('flying', True, registries.colors.BLACK)
toggleAdvMove = registries.buttons.registerButton("toggle", 300, 150,  12.0, "", registries.colors.BLACK, "")

screen_width = 1000
screen_height = 600

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types



def Main(screen,clock):
    world = pygame.Surface((8000,8000)) # Create Map
    player = Player() # Initialize Player Class
    camera_pos = (-100,-312) #camera starting position
    player_rect = pygame.Rect((50, 50), (32, 32))
    test_rect = pygame.Rect(100,100,100,50)

    #values for animation calculation
    idleValue = 0
    walkingValue = 0

    moving_right = False
    moving_left = False

    player_y_momentum = 0
    air_timer = 0

    while True:
        #idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        #loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0

        tile_rects = []
        y = 0
        for row in game_map:
            x = 0
            for tile in row:
                if tile == '1':
                    world.blit(dirtElement, (x * grass_width, y * grass_width))
                if tile == '2':
                    world.blit(grassElement, (x * grass_width, y * grass_width))
                if tile != '0':
                    tile_rects.append(pygame.Rect(x * grass_width, y * grass_width, grass_width, grass_width))
                x += 1
            y += 1

        player_movement = [0, 0]
        if moving_right:
            player_movement[0] += 2
        if moving_left:
            player_movement[0] -= 2
        player_movement[1] += player_y_momentum
        player_y_momentum += 0.2
        if player_y_momentum > 3:
            player_y_momentum = 3

        player_rect, collisions = move(player_rect, player_movement, tile_rects)

        if collisions['bottom']:
            player_y_momentum = 0
            air_timer = 0
        else:
            air_timer += 1
        

        world.blit(Player.currentSprite, (player_rect.x, player_rect.y))

        for event in pygame.event.get(): # event loop
            if event.type == pygame.QUIT: # check for window quit
                pygame.quit() # stop pygame
            
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    moving_right = True
                if event.key == K_LEFT:
                    moving_left = True
                if event.key == K_UP:
                    if air_timer < 6:
                        player_y_momentum = -5
            if event.type == KEYUP:
                if event.key == K_RIGHT:
                    moving_right = False
                if event.key == K_LEFT:
                    moving_left = False

        screen.blit(world, (0, 0))
        world.fill(registries.colors.AQUA)
        pygame.display.update() # update display
        clock.tick(60) # maintain 60 fps

if __name__ in "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(screen,clock) # Run Main Loop