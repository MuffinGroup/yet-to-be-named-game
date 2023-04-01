import pygame
import registries.colors
import registries.animations
import registries.element

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
        Player.rect = pygame.Rect((180,650),(100, 200)) # Create the players hitbox
        Player.animationFrameUpdate = 1
        Player.debuggingMode = False
        Player.visible = True
        Player.locked = False
        Player.debuggingMenu = False

    def keybinds(self,camera_pos):
        global player_x
        global player_y
        self.doorhandling = 0 #Door mechanics
        player_x = self.rect.x #Camera following the player
        player_y = self.rect.y

        player_x, player_y = camera_pos #Assign variables to the camera position

        key = pygame.key.get_pressed() #Receive keyboard input
        if key[pygame.K_UP] and Player.jumpvar == -16 and Player.visible == True and Player.locked == False: #Jumping
            Player.jumpvar = 14.3
        elif key[pygame.K_SPACE] and Player.jumpvar == -16 and Player.visible == True and Player.locked == False: #Alternative jumping keybind
            Player.jumpvar = 14.3

        if Player.jumpvar == 14.3: #Play jump sound when the player jumps
            pygame.mixer.Sound.play(Player.jumpsound)

        if Player.jumpvar >= -15: #Jumping movement
            n = 1
            if Player.jumpvar < 0:
                n = -1
            self.rect.y -= (Player.jumpvar**2)*0.17*n
            Player.jumping = True
            Player.jumpvar -= 1
        else:
            Player.jumpvar = -16
            Player.jumping = False

        if key[pygame.K_RIGHT] and Player.visible == True and Player.collidingRight == True and Player.locked == False and Player.locked == False: #Player walking
            Player.facingLeft = False
            Player.facingRight = True
        elif key[pygame.K_RIGHT] and Player.collidingRight == False and Player.locked == False:
            Player.facingLeft = False
            Player.facingRight = True
            Player.standing = False
            self.rect.x += Player.speed
        else:
            Player.standing = True
            Player.walking = False

        if key[pygame.K_LEFT] and Player.visible == True and Player.collidingLeft == True and Player.locked == False: #Player walking
            Player.facingLeft = True
            Player.facingRight = False
        elif key[pygame.K_LEFT] and Player.collidingLeft == False and Player.locked == False:
            Player.facingLeft = True
            Player.facingRight = False
            Player.standing = False
            self.rect.x -= Player.speed
        else:
            Player.standing = True
            Player.walking = False

        if Player.collidingLeft == True:
            print("colliding left")
        if Player.collidingRight == True:
            print("colliding right")

        #Debug mode to help developers
        if key[pygame.K_d] and Player.locked == False:
            Player.debuggingMode = True

        if key[pygame.K_0] and Player.debuggingMode == True and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.locked = True
            Player.debuggingMenu = True
            print("e")
        elif key[pygame.K_0] and Player.debuggingMode == True:
            pygame.time.wait(200)
            Player.debuggingMenu = False
            print("o")

        if key[pygame.K_DOWN] and Player.visible == True and registries.element.registerElements.colliding == False and Player.debuggingMode == True and Player.locked == False:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.y += Player.speed 
        else:
            Player.standing = True
            Player.walking = False
            
        if key[pygame.K_u] and Player.visible == True and registries.element.registerElements.colliding == False and Player.debuggingMode == True and Player.locked == False:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.y -= Player.speed 
        else:
            Player.standing = True
            Player.walking = False

        if key[pygame.K_p] and Player.debuggingMode == True:
            print(Player.rect.x)
    
    #End of debugging mode functions

        if key[pygame.K_LEFT] and Player.visible == True and Player.locked == False or key[pygame.K_RIGHT] and Player.visible == True  and Player.locked == False: #Walking animations
            Player.walking = True

        if Player.walking == True and key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]: #Sprinting
            Player.speed = 18
            Player.countUp = 2
        else:
            Player.speed = Player.defaultSpeed

        return (-self.rect.x + 380, -self.rect.y + 300) # Return new player position
    
    def render(self,screen): #Player and player hitbox rendering
        if Player.visible == True:
            Player.currentSprite = pygame.transform.scale(Player.currentSprite,(250,250))
            screen.blit(self.currentSprite,(self.rect.x - 75,self.rect.y-50)) #Drawing the player to the screen
            if Player.debuggingMode == True:
                pygame.draw.rect(screen, (0, 255, 0), Player.rect, 4) #Drawing the hitbox to the screen

    def collisions(self):
        #Checking for collisions with element hitboxes
        if Player.rect.colliderect(placeholder_hitbox) or Player.rect.colliderect(tree_stump_hitbox):
            registries.element.registerElements.colliding = True
        else:
            registries.element.registerElements.colliding = False

        #Collisions on the left side
        if Player.facingLeft == True and Player.collidingRight == False and registries.element.registerElements.colliding == True:
            Player.collidingLeft = True
        else:
            Player.collidingLeft = False
    
        #Collisions on the right side
        if Player.facingRight == True and Player.facingLeft == False and registries.element.registerElements.colliding == True:
            Player.collidingRight = True
        else:
            Player.collidingRight = False

        if Player.debuggingMode == False:
            if not Player.rect.colliderect(floor_hitbox) and Player.jumping == False:
                Player.rect.y += 0.1
            if Player.rect.colliderect(floor_hitbox) and Player.jumping == False:
                Player.rect.y = 650
            
            if Player.rect.colliderect(placeholder_hitbox):
                Player.rect.y = placeholder_hitbox.y - placeholder.get_height() * 1.25
            elif Player.rect.colliderect(floor_hitbox) and Player.jumping == False and Player.rect.colliderect(placeholder_hitbox) and Player.jumping == False:
                Player.rect.y = 650

#Loading element textures
placeholder = registries.element.registerElements("environment/blocks/cobble", 5)
wooden_sign = registries.element.registerElements("environment/blocks/wooden_sign", 5)
tree_stump = registries.element.registerElements("environment/blocks/tree_stump", 5)
placeholder3 = registries.element.registerElements("environment/blocks/cobble", 5)

print(tree_stump.get_width())

#Loading element hitboxes
placeholder_hitbox = pygame.Rect((400, 650),(int(placeholder.get_width()), int(placeholder.get_height())))
tree_stump_hitbox = pygame.Rect((800, 730),(int(placeholder.get_width()), int(placeholder.get_width())))

#Loading floor and background
floor = pygame.image.load("src\main/assets/textures\levels\grass_floor.png")
floor_width = floor.get_width()
floor_height = floor.get_height()
floor = pygame.transform.scale(floor, (int(floor_width * 8), int(floor_height * 8)))
floor_hitbox = pygame.Rect((0, 850), (floor_width * 8, floor_height * 8))

font = pygame.font.SysFont('joystixmonospaceregular', 25)
text = font.render('Press 0 to open/close the debug menu', True, registries.colors.DARK_ORANGE)

debug_menu = pygame.Rect((100, 100), (100, 100))

def Main(screen,clock):
    world = pygame.Surface((8000,8000)) # Create Map
    player = Player() # Initialize Player Class
    camera_pos = (-100,-312) #camera starting position

    #values for animation calculation
    idleValue = 0
    walkingValue = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                return
        #idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        #loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0

        #Player collision detection
        player.collisions()
        
        #Player movement
        camera_pos = player.keybinds(camera_pos) 

        #Movement animation rendering
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_sprite[walkingValue]
        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        #Render background
        world.fill(registries.colors.AQUA)

        #Render floor
        world.blit(floor, floor_hitbox)

        #pygame.draw.rect(world, registries.colors.GREEN, floor_hitbox, 10) #<-- debugging purposes
        
        #Draw elements to the screen
        placeholder.draw(world, placeholder_hitbox)

        tree_stump.draw(world, tree_stump_hitbox)

        #Fill the background outside of the map
        screen.fill(registries.colors.AQUA)

        #Render the player
        player.render(world)

        #Render the map to the screen
        screen.blit(world, (player_x,player_y))

        if Player.debuggingMode == True:
            screen.blit(text, (320, 30))
        
        if Player.debuggingMenu == True:
            pygame.draw.rect(screen, registries.colors.PURPLE, debug_menu, 10000)

        #Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate

        clock.tick(200)
        pygame.display.flip()

if __name__ in "__main__":
    screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(screen,clock) # Run Main Loop