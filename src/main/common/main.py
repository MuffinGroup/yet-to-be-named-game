import pygame
import colors
import animations
import output

pygame.init()

class Player:
    def __init__(currentImage):
        Player.rightImage = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png") # Create Player Image
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.currentSprite = Player.rightImage
        Player.image_speed= 5 
        Player.jumpvar = -16
        Player.standingRight = True
        Player.standingLeft = False
        Player.standing = True
        Player.jumpingRight = False
        Player.jumpingLeft = False
        Player.jumping = False
        Player.walkingRight = False
        Player.walkingLeft = False
        Player.walking = False
        Player.rect = pygame.Rect((50,50),(30,30)) # Create Player Rect

    def move(self,camera_pos):
        self.running = True
        self.doorhandling = 0
        self.visible = True
        pos_x,pos_y = camera_pos # Split camara_pos
        
        key = pygame.key.get_pressed() # Get Keyboard Input
        if key[pygame.K_UP] and Player.jumpvar == -16 and self.visible == True: # Check Keyif keys[pygame.K_UP] and jumpvar == -16 and visible == True:
            Player.standing = False
            Player.jumpvar = 15
        elif key[pygame.K_SPACE] and Player.jumpvar == -16 and self.visible == True:
            Player.jumpvar = 15

        if Player.jumpvar == 15:
            pygame.mixer.Sound.play(Player.jumpsound)

        if Player.jumpvar >= -15:
            n = 1
            if Player.jumpvar < 0:
                n = -1
            self.rect.y -= (Player.jumpvar**2)*0.17*n
            pos_y += (Player.jumpvar**2)*0.17*n
            Player.jumping = True
            Player.jumpvar -= 1

        if key[pygame.K_LEFT] and self.visible == True:
            Player.walkingLeft = True
            Player.standing = False
            Player.standingLeft = True
            self.rect.x -= Player.image_speed 
            pos_x += Player.image_speed
        else:
            Player.walkingLeft = False

        if key[pygame.K_RIGHT] and self.visible == True:
            Player.walkingRight = True
            Player.standing = False
            Player.standingRight = True
            self.rect.x += Player.image_speed 
            pos_x -= Player.image_speed
        else:
            Player.walkingRight = False
        
        if self.rect.x < 0: # Simple Sides Collision
            self.rect.x = 0 # Reset Player Rect Coord
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.rect.x > 1980: #Set the Player`s moving range
            self.rect.x = 1980
            pos_x = camera_pos[0]
        elif self.rect.y > 1980:
            self.rect.y = 1980
            pos_y = camera_pos[1]

        if Player.standingLeft == True or Player.standingRight == True:
            Player.standing = True

        if Player.walkingLeft == True or Player.walkingRight == True:
            Player.walking = True
        
        return (pos_x,pos_y) # Return New Camera Pos
    
    def render(self,display):
        if self.visible == True:
            Player.currentSprite= pygame.transform.scale(Player.currentSprite,(250,250))
            display.blit(self.currentSprite,(self.rect.x,self.rect.y))

background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_0.jpg")
background= pygame.transform.scale(background,(2000,2000))

def Main(display,clock):
    world = pygame.Surface((2000,2000)) # Create Map Surface
     
    player = Player() # Initialize Player Class
    camera_pos = (192,192) # Create Camara Starting Position 
    
    #values for animation calculation
    idleValue = 0
    WalkingValue = 0

    output.log("Started succesfully")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                output.log("Closed successfully")
                return

        if idleValue >= len(animations.idle_sprite):
            idleValue = 0

        Player.currentSprite = animations.idle_sprite[idleValue]

        if WalkingValue >= len(animations.walking_sprite):
            WalkingValue = 0
        
        camera_pos = player.move(camera_pos) # Run Player Move Function And Return New Camera Pos

        #Player position detection
        if Player.walkingRight == True:
            Player.currentSprite = animations.walking_sprite[WalkingValue]
            
        if Player.walkingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        if Player.standingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)
        
        player.render(world) # Render The Player
        display.fill(colors.WHITE) # Fill The Background White To Avoid Smearing
        display.blit(world,camera_pos) # Render Map To The Display
        world.blit(background, (0,0))

        if Player.standing == True:
            idleValue += 1

        if Player.walking == True:
            WalkingValue += 1
        
        pygame.display.flip()


if __name__ in "__main__":
    display = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(display,clock) # Run Main Loop