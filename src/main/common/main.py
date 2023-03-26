import pygame
import registries.colors
import registries.animations
import registries.element

pygame.init()

class Player:
    def __init__(currentImage):
        Player.defaultSpeed = 10
        Player.rightImage = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png") # Create Player Image
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.currentSprite = Player.rightImage
        Player.image_speed= Player.defaultSpeed
        Player.jumpvar = -16
        Player.facingRight = True
        Player.facingLeft = False
        Player.standing = True
        Player.jumping = False
        Player.walking = False
        Player.colliding = False
        Player.rect = pygame.Rect((480,600),(30,30)) # Create Player Rect
        Player.countup = 1

    def move(self,camera_pos):
        self.running = True
        self.doorhandling = 0
        self.visible = True
        global pos_x
        global pos_y
        pos_x,pos_y = camera_pos # Split camara_pos
        
        key = pygame.key.get_pressed() # Get Keyboard Input
        if key[pygame.K_UP] and Player.jumpvar == -16 and self.visible == True and Player.colliding == False: # Check Keyif keys[pygame.K_UP] and jumpvar == -16 and visible == True:
            Player.jumpvar = 14.3
        elif key[pygame.K_SPACE] and Player.jumpvar == -16 and self.visible == True and Player.colliding == False:
            Player.jumpvar = 14.3

        if Player.jumpvar == 14.3:
            pygame.mixer.Sound.play(Player.jumpsound)

        if Player.jumpvar >= -15:
            n = 1
            if Player.jumpvar < 0:
                n = -1
            self.rect.y -= (Player.jumpvar**2)*0.17*n
            pos_y += (Player.jumpvar**2)*0.17*n
            Player.jumping = True
            Player.jumpvar -= 1
        else:
            Player.jumpvar = -16

        if key[pygame.K_RIGHT] and self.visible == True and Player.colliding == False:
            Player.standing = False
            Player.facingLeft = False
            Player.facingRight = True
            self.rect.x += Player.image_speed 
            pos_x -= Player.image_speed
        else:
            Player.standing = True
            Player.walking = False
        
        if key[pygame.K_LEFT] and self.visible == True and Player.colliding == False:
            Player.standing = False
            Player.facingLeft = True
            Player.facingRight = True
            self.rect.x -= Player.image_speed 
            pos_x += Player.image_speed
        else:
            Player.standing = True
            Player.walking = False

        if key[pygame.K_LEFT] and self.visible == True or key[pygame.K_RIGHT] and self.visible == True:
            Player.walking = True
        
        if Player.walking == True and key[pygame.K_RSHIFT] or key[pygame.K_LSHIFT]:
            Player.image_speed = 18
            Player.countUp = 2
        else:
            Player.image_speed = Player.defaultSpeed

        #For debugging purposes
        if key[pygame.K_p]:
            print(Player.rect.x)

        if self.rect.x < 380: # Simple Sides Collision
            self.rect.x = 380 # Reset Player Rect Coord
            Player.standing = True
            Player.walking = False
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.rect.x > 1980: #Set the Player`s moving range
            self.rect.x = 1980
            Player.standing = True
            Player.walking = False
            pos_x = camera_pos[0]
        elif self.rect.y > 1980:
            self.rect.y = 1980
            Player.standing = True
            Player.jumping = False
            Player.walking = False
            pos_y = camera_pos[1]
        
        return (pos_x,pos_y) # Return New Camera Pos
    
    def render(self,screen):
        if self.visible == True:
            Player.currentSprite = pygame.transform.scale(Player.currentSprite,(250,250))
            screen.blit(self.currentSprite,(self.rect.x,self.rect.y))

floor = pygame.image.load("src\main/assets/textures\levels\grass_floor.png")
floor_width = floor.get_width()
floor_height = floor.get_height()
floor = pygame.transform.scale(floor, (int(floor_width * 8), int(floor_height * 8)))
wooden_sign = registries.element.registerElements("environment/blocks/wooden_sign", 480, 770, 5)
placeholder = registries.element.registerElements("environment/blocks/cobble", 1980, 770, 5)

background = pygame.image.load("src\main/assets/textures\levels/background.png")
background_width = background.get_width()
background_height = background.get_height()
background = pygame.transform.scale(background, (int(background_width * 3), int(background_height * 3)))

def Main(screen,clock):
    world = pygame.Surface((8000,8000)) # Create Map Surface
     
    player = Player() # Initialize Player Class
    camera_pos = (-100,-312) # Create Camara Starting Position 
    
    #values for animation calculation
    idleValue = 0
    WalkingValue = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                return

        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        Player.currentSprite = registries.animations.idle_sprite[idleValue]

        if WalkingValue >= len(registries.animations.walking_spriteNew):
            WalkingValue = 0
        
        camera_pos = player.move(camera_pos) # Run Player Move Function And Return New Camera Pos

        #Player position detection
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_spriteNew[WalkingValue]

        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)
        
        world.fill(registries.colors.AQUA)
        world.blit(floor, (-500,850))
        wooden_sign.draw(world)
        placeholder.draw(world)
        screen.fill(registries.colors.WHITE) # Fill The background White To Avoid Smearing
        player.render(world) # Render The Player
        screen.blit(world, (pos_x,pos_y)) # Render Map To The screen

        if Player.standing == True:
            idleValue += 1

        if Player.walking == True:
            WalkingValue += Player.countup

        clock.tick(200)
        pygame.display.flip()


if __name__ in "__main__":
    screen = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(screen,clock) # Run Main Loop