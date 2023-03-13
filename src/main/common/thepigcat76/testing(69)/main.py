import pygame
pygame.init()
#
###
class Player:
    def __init__(currentImage):
        Player.rightImage = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1.png") # Create Player Image
        Player.leftImage = pygame.transform.flip(Player.rightImage, True, False)
        Player.currentImage = Player.rightImage
        Player.image_speed= 5 
        Player.rect = pygame.Rect((50,50),(30,30)) # Create Player Rect
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
        #
        camera_pos = player.move(camera_pos) # Run Player Move Function And Return New Camera Pos
        #
        display.fill(colors["WHITE"]) # Fill The Background White To Avoid Smearing
        player.render(world) # Render The Player
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
    #
    global colors # Difign Colors
    colors = {
    "WHITE":(255,255,255),
    "RED"  :(255,0,0),
    "GREEN":(0,255,0),
    "BLUE" :(0,0,255),
    "BLACK":(0,0,0)
    }
    Main(display,clock) # Run Main Loop