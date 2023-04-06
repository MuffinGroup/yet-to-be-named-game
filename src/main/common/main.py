import pygame
import registries.colors
import registries.animations
import registries.elements
import registries.buttons

#pygame initialization
pygame.init()
class Player:
    #Initial Player attribute assignment
    def __init__(currentImage):
        Player.defaultSpeed = 10
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.speed = Player.defaultSpeed
        Player.jumpvar = 16 #Important for jumping calculation
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
        Player.test = False
        Player.flying = 0
        Player.colliding = 0
        Player.allowJump = True
        Player.collidingTop = False
        Player.test2 = 0
        Player.n = 0
        Player.e = False

    def keybinds(self,camera_pos):
        global player_x
        global player_y
        self.doorhandling = 0 #Door mechanics
        player_x = self.rect.x #Camera following the player
        player_y = self.rect.y

        player_x, player_y = camera_pos #Assign variables to the camera position

        key = pygame.key.get_pressed() #Receive keyboard input
        if key[pygame.K_UP] and Player.jumpvar == 16 and Player.visible == True and Player.locked == False and Player.allowJump == True: #Jumping
            Player.jumpvar = -14.3
        elif key[pygame.K_SPACE] and Player.jumpvar == 16 and Player.visible == True and Player.locked == False and Player.allowJump == True: #Alternative jumping keybind
            Player.jumpvar = -14.3

        if Player.jumpvar == -14.3: #Play jump sound when the player jumps
            pygame.mixer.Sound.play(Player.jumpsound)

        if Player.jumpvar <= 15: #Jumping movement
            Player.n = -1
            if Player.jumpvar < 0:
                Player.n = 1
            Player.rect.y -= (Player.jumpvar**2)*0.17*Player.n
            Player.jumping = True
            Player.jumpvar += 1
        else:
            Player.jumpvar = 16
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
        elif key[pygame.K_LEFT] and Player.collidingLeft == False and Player.locked == False and Player.collidingLeft == False:
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
        if key[pygame.K_d] and Player.debuggingMode == False:
            pygame.time.wait(200)
            Player.debuggingMode = True
        elif key[pygame.K_d] and Player.debuggingMode == True and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.debuggingMode = False
            Player.flying == 0

        if key[pygame.K_0] and Player.debuggingMode == True and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.locked = True
            Player.debuggingMenu = True
        elif key[pygame.K_0] and Player.debuggingMode == True:
            pygame.time.wait(200)
            Player.locked = False
            Player.debuggingMenu = False

        if key[pygame.K_DOWN] and Player.visible == True and Player.debuggingMode == True and Player.locked == False and Player.flying == 1:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.y += Player.speed 
        else:
            Player.standing = True
            Player.walking = False
            
        if key[pygame.K_u] and Player.visible == True and Player.debuggingMode == True and Player.locked == False and Player.flying == 1:
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
            if Player.debuggingMode == True or Player.e == True:
                pygame.draw.rect(screen, (0, 255, 0), Player.rect, 4) #Drawing the hitbox to the screen	

    def renderDebugMenu(self):
        if Player.debuggingMenu == True:
            pygame.draw.rect(screen, registries.colors.BLUISH_GRAY, debug_menu, 10000)
            if toggleAdvMove.drawToggle(screen):
                if Player.flying > 1:
                    Player.flying = 0
                Player.flying += 1
                if Player.flying == 1:
                    print("selected")
                if Player.flying == 2:
                    print("not selected") 
            screen.blit(toggleAdvMoveText, (100, 135))
            if toggleCollisions.drawToggle(screen):
                if Player.colliding > 1:
                    Player.colliding = 0
                Player.colliding += 1
                if Player.colliding == 1:
                    print("selected")
                if Player.colliding == 2:
                    print("not selected") 
            screen.blit(toggleCollisionsText, (80, 235))

    def collisions(self):
        #Checking for collisions with element hitboxes
        if Player.rect.colliderect(placeholder_hitbox) or Player.rect.colliderect(tree_stump_hitbox):
            registries.elements.registerElements.colliding = True
        else:
            registries.elements.registerElements.colliding = False

        #Collisions on the left side
        if Player.facingLeft == True and Player.collidingRight == False and registries.elements.registerElements.colliding == True:
            Player.collidingLeft = True
        else:
            Player.collidingLeft = False
    
        #Collisions on the right side
        if Player.facingRight == True and Player.facingLeft == False and registries.elements.registerElements.colliding == True:
            Player.collidingRight = True
        else:
            Player.collidingRight = False

        if Player.rect.colliderect(floor_hitbox):
            Player.rect.y = 650
        if Player.rect.collidepoint(placeholder_hitbox.centerx, placeholder_hitbox.top):
            Player.rect.y -= placeholder.get_height()/1.6
        if not Player.rect.colliderect(placeholder_hitbox) and not Player.rect.colliderect(floor_hitbox) and Player.jumping == False:
            Player.rect.y += 0.1

    def collisionsUpdated(self):
        if Player.flying == 0:    
            if not Player.rect.colliderect(floor_hitbox) and not Player.rect.colliderect(placeholder_hitbox) and Player.jumping == False:
                Player.rect.y += 7
            elif Player.collidingTop == True:
                Player.rect.y -= 10
                print("b")

            if Player.rect.collidepoint(placeholder_hitbox.topleft) and Player.rect.collidepoint(placeholder_hitbox.x, placeholder_hitbox.centery) and Player.facingRight == True and Player.collidingLeft == False:
                Player.collidingRight = True
            elif Player.rect.collidepoint(placeholder_hitbox.topleft) and not Player.rect.collidepoint(placeholder_hitbox.x, placeholder_hitbox.centery) and Player.rect.y < 650 + placeholder.get_height():
                Player.collidingRight = True
            else:
                Player.collidingRight = False

            if Player.rect.collidepoint(placeholder_hitbox.topright) and Player.rect.collidepoint(placeholder_hitbox.x + placeholder.get_width(), placeholder_hitbox.centery) and Player.facingLeft == True and Player.collidingRight == False:
                Player.collidingLeft = True
            elif Player.rect.collidepoint(placeholder_hitbox.topright) and not Player.rect.collidepoint(placeholder_hitbox.x + placeholder.get_width(), placeholder_hitbox.centery) and Player.rect.y < 650 + placeholder.get_height():
                Player.collidingLeft = True
            else:
                Player.collidingLeft = False

            if Player.rect.collidepoint(placeholder_hitbox.center) and Player.facingLeft == True:
                while Player.rect.colliderect(placeholder_hitbox):
                    Player.rect.x += 1
                print("colliding center")
            elif Player.rect.collidepoint(placeholder_hitbox.center) and Player.facingRight == True:
                while Player.rect.colliderect(placeholder_hitbox):
                    Player.rect.x -= 1

            if Player.rect.collidepoint(placeholder_hitbox.centerx, placeholder_hitbox.top):
                Player.collidingTop = True
            elif Player.rect.collidepoint(placeholder_hitbox.x, placeholder_hitbox.top) and not Player.rect.collidepoint(placeholder_hitbox.x, placeholder_hitbox.centery) and Player.rect.y >= placeholder_hitbox.y + placeholder.get_height():
                print("collisions are weird")
            elif Player.rect.collidepoint(placeholder_hitbox.topleft) and Player.collidingRight == False: #jumping is temporary
                print("why???")
                Player.e = True
            else:
                Player.collidingTop = False
                Player.e = False
        

#Loading element textures
placeholder = registries.elements.registerElements("environment/blocks/cobble", 5)
wooden_sign = registries.elements.registerElements("environment/blocks/wooden_sign", 5)
tree_stump = registries.elements.registerElements("environment/blocks/tree_stump", 5)
placeholder3 = registries.elements.registerElements("environment/blocks/cobble", 5)

print(tree_stump.get_width())

#Loading element hitboxes
placeholder_hitbox = pygame.Rect((400, 700),(int(placeholder.get_width()), int(placeholder.get_height())))
tree_stump_hitbox = pygame.Rect((800, 730),(int(placeholder.get_width()), int(placeholder.get_width())))

#Loading floor and background
floor = pygame.image.load("src\main/assets/textures\levels\grass_floor.png")
floor_width = floor.get_width()
floor_height = floor.get_height()
floor = pygame.transform.scale(floor, (int(floor_width * 8), int(floor_height * 8)))
floor_hitbox = pygame.Rect((0, 850), (floor_width * 8, floor_height * 8))

font = pygame.font.SysFont('joystixmonospaceregular', 25)
text = font.render('Press 0 to open/close the debug menu', True, registries.colors.DARK_ORANGE)

debug_menu = pygame.Rect((70, 70), (300, 400))

toggleCollisionsText = font.render('collides', True, registries.colors.BLACK)
toggleCollisions = registries.buttons.registerButton("toggle", 300, 250,  12.0, "", registries.colors.BLACK, "")

toggleAdvMoveText = font.render('flying', True, registries.colors.BLACK)
toggleAdvMove = registries.buttons.registerButton("toggle", 300, 150,  12.0, "", registries.colors.BLACK, "")

screen_width = 1000
screen_height = 600

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

        print(int(Player.rect.y + (Player.jumpvar**2)*0.17*Player.n))

        #Player collision detection
        player.collisionsUpdated()
        
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

        pygame.draw.rect(world, registries.colors.WHITE, placeholder_hitbox, 1000)

        tree_stump.draw(world, tree_stump_hitbox)

        #Fill the background outside of the map
        screen.fill(registries.colors.AQUA)

        #Render the player
        player.render(world)

        #Render the map to the screen
        screen.blit(world, (player_x,player_y))

        if Player.debuggingMode == True:
            screen.blit(text, (320, 30))

        #Rendering the debug menu
        player.renderDebugMenu()

        #Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate

        clock.tick(200)
        pygame.display.flip()

if __name__ in "__main__":
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(screen,clock) # Run Main Loop