import pygame
import registerPlayer
from colors import *

pygame.init()
#
###
class Player:
    def __init__(currentImage):
        Player.rightImage = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1.png") # Create Player Image
        Player.leftImage = pygame.transform.flip(Player.rightImage, True, False)
        Player.jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
        Player.jumpsound.set_volume(0.25)
        Player.currentImage = Player.rightImage
        Player.image_speed= 5 
        Player.rect = pygame.Rect((50,50),(30,30)) # Create Player Rect
    def move(self,camera_pos):
        self.running = True
        jumpvar = -16
        self.doorhandling = 0
        self.visible = True
        self.standing = True
        self.walking = False
        self.jumping = False
        pos_x,pos_y = camera_pos # Split camara_pos
        #
        key = pygame.key.get_pressed() # Get Keyboard Input
<<<<<<< HEAD
        if key[pygame.K_UP] and jumpvar == -16 and self.visible == True:
=======
        if key[pygame.K_UP] and jumpvar == -16 and self.visible == True: # Check Keyif keys[pygame.K_UP] and jumpvar == -16 and visible == True:
            standing = False
            jumping = True
>>>>>>> 871fb3483673b7e93c29a7560eb5bf29c3ebfefd
            jumpvar = 15
        elif key[pygame.K_SPACE] and jumpvar == -16 and self.visible == True:
            jumpvar = 15

        if jumpvar == 15:
            pygame.mixer.Sound.play(Player.jumpsound)

        if jumpvar >= -15:
            n = 1
            if jumpvar < 0:
                n = -1
            self.rect.y -= (jumpvar**2)*0.17*n
            pos_y += (jumpvar**2)*0.17*n
            jumpvar -= 1

        if key[pygame.K_LEFT] and self.visible == True:
            self.standing = False
            self.walking = True
            Player.currentImage = Player.leftImage
            self.rect.x -= Player.image_speed 
            pos_x += Player.image_speed
        if key[pygame.K_RIGHT] and self.visible == True:
            self.standing = False
            self.walking = True
            Player.currentImage = Player.rightImage
            self.rect.x += Player.image_speed 
            pos_x -= Player.image_speed 
        #
        if self.rect.x < 0: # Simple Sides Collision
            self.rect.x = 0 # Reset Player Rect Coord
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.rect.x > 1980: #Set the Player`s moving range
            self.rect.x = 1980
            pos_x = camera_pos[0]
        elif self.rect.y > 1980:
            self.rect.y = 1980
            pos_y = camera_pos[1]

        if self.walking == True:
            print("yes")
        #
        return (pos_x,pos_y) # Return New Camera Pos
    def render(self,display):
        if self.visible == True:
            Player.currentImage= pygame.transform.scale(Player.currentImage,(250,250))
            display.blit(self.currentImage,(self.rect.x,self.rect.y))
background = pygame.image.load("src\main/assets\elements/background\Background final2.jpg")
background=pygame.transform.scale(background,(2000,2000))

def Main(display,clock):
    world = pygame.Surface((2000,2000)) # Create Map Surface
     
    #
    player = Player() # Initialize Player Class
    camera_pos = (192,192) # Create Camara Starting Position 
    #
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or(event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
                pygame.quit()
                return
        
        camera_pos = player.move(camera_pos) # Run Player Move Function And Return New Camera Pos
        
        player.render(world) # Render The Player
        display.fill(COLORS.WHITE) # Fill The Background White To Avoid Smearing
        display.blit(world,camera_pos) # Render Map To The Display
        world.blit(background, (0,0))
        #
        pygame.display.flip()
###
#
if __name__ in "__main__":
    display = pygame.display.set_mode((1000,600), pygame.RESIZABLE)
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    Main(display,clock) # Run Main Loop