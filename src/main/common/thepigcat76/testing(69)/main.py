import pygame
from colors import *
import animations

class main():
    #Pygame initialization
    pygame.init()
    #Setup for fps
    clock = pygame.time.Clock()

    #Loading world elements
    background = pygame.image.load("src/main/assets/elements/background/hallway.jpg")
    floor = pygame.image.load("src\main/assets/elements/background/floor.jpg")
    door_closed = pygame.image.load("src\main/assets\elements\doors\door_1_closed.png")
    door_open = pygame.image.load("src\main/assets\elements\doors\door_1_open.png")

    #Loading utility stuff
    icon = pygame.image.load('src/main/assets/gui/icon/icon.png')

    #Assigning variables
    #Character size
    characterWidth = 32
    characterHeight = 32

    #Screen size
    screen_width = 1280
    screen_height = 800

    #Defining scale for character scaling
    scale = 10

    #character position
    character_x = 150
    character_y = 410

    #camera position
    camera_x = 192
    camera_y = 192

    #character speed
    character_speed = 5
    
    #values for animation calculation
    value = 0
    WalkingValue = 0

    #Door 
    doorOpen = False

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Muffin Group")

    jumpsound = pygame.mixer.Sound("src/main/assets/sounds/entities/jump.wav")
    doorsound = pygame.mixer.Sound("src\main/assets\sounds\entities\Door_Closing.wav")
    character_image_main = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha
    character_image = pygame.image.load("src/main/assets/entities/characters/Character1/Animations/Character1.png").convert_alpha()

    # Create a screen surface
    leftWall = pygame.draw.rect(screen, (0,0,0), (0,0,2,1000), 0)
    rightWall = pygame.draw.rect(screen, (0,0,0), (1100,0,2,1000), 0)

    #Create Sound
    jumpsound.set_volume(0.01)

    # Load character image
    character_image_inverted = pygame.transform.flip(character_image, True, False)

    #Image dimensions
    image_width = character_image.get_width()
    image_height = character_image.get_height()
    character_image = pygame.transform.scale(character_image, (int(image_width * scale), int(image_height * scale)))
    character_image_inverted = pygame.transform.scale(character_image_inverted, (int(image_width * scale), int(image_height * scale)))
    currentDoorSprite = door_closed
    door_width = currentDoorSprite.get_width()
    door_height = currentDoorSprite.get_height()
    currentSprite = character_image

    # Set initial position

    # Set character speed


    # Game loop
    running = True
    jumpvar = -16
    visible = True
    standing = True
    walking = False
    jumping = False

    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        if value >= len(animations.idle_sprite):
            value = 0

        currentSprite = animations.idle_sprite[value]

        if WalkingValue >= len(animations.walking_sprite):
            WalkingValue = 0
    
        # Handle keyboard input
        keys = pygame.key.get_pressed()
        Spieler = pygame.Rect(character_x, character_y, 40, 80)
        Door = pygame.Rect(990, 410, 40, 80)

        if keys[pygame.K_LEFT] and not Spieler.colliderect(leftWall) and visible == True:
            standing = False
            walking = True
            character_x -= character_speed
            character_image = character_image_inverted
        elif keys[pygame.K_a] and not Spieler.colliderect(leftWall) and visible == True:
            standing = False
            walking = True
            character_x -= character_speed
            character_image = character_image_inverted
        else:
            standing = True
            walking = False

        if keys[pygame.K_RIGHT] and not Spieler.colliderect(rightWall) and visible == True:
            standing = False
            walking = True
            character_x += character_speed
        elif keys[pygame.K_d] and not Spieler.colliderect(rightWall) and visible == True:
            standing = False
            walking = True
            character_x += character_speed
        else:
            standing = True
            walking = False

        if keys[pygame.K_UP] and jumpvar == -16 and visible == True:
            standing = False
            jumping = True
            jumpvar = 15
        elif keys[pygame.K_SPACE] and jumpvar == -16 and visible == True:
            standing = False
            jumping = True
            jumpvar = 15

        if keys[pygame.K_DOWN] and Spieler.colliderect(Door) and visible == True:
            doorOpen = True
        elif keys[pygame.K_s] and Spieler.colliderect(Door) and visible == True:
            doorOpen = True

        if jumpvar == 15:
            pygame.mixer.Sound.play(jumpsound)

        if jumpvar >= -15:
            n = 1
            if jumpvar < 0:
                n = -1
            character_y -= (jumpvar**2)*0.17*n
            jumpvar -= 1

        if doorOpen == True:
            currentDoorSprite = door_open
        else:
            currentDoorSprite = door_closed

        if walking == True:
            currentSprite = animations.walking_sprite[WalkingValue]

        # Draw the character and update the screen
        screen.fill(COLORS.BLACK)
        screen.blit(background, (0,0))
        screen.blit(floor, (0,730))
        currentDoorSprite = pygame.transform.scale(currentDoorSprite, (int(door_width * scale/2), int(door_height * scale/2)))
        screen.blit(currentDoorSprite, (990,420))

        currentSprite = pygame.transform.scale(currentSprite, (int(characterWidth * scale), int(characterHeight * scale)))    
        if visible == True:
            screen.blit(currentSprite, (character_x, character_y))
        pygame.display.update()

        if doorOpen == True:
            pygame.time.wait(500)
            pygame.mixer.Sound.play(doorsound)
            visible = False
            doorOpen = 0

        if standing == True:
            value += 1

        if walking == True:
            WalkingValue += 1

        clock.tick(69)

class Player:
    def __init__(image):
        Player.image = pygame.image.load("src\main\common\LS-P/Pictures\Character1.copy.png") # Create Player Image 🍆
        Player.image=pygame.transform.scale(Player.image,(250,250)) #🍆
        Player.image_speed= 5 #🍆
        Player.rect = pygame.Rect((50,50),(30,30)) # Create Player Rect🍆
    def move(self,camera_pos):
        pos_x,pos_y = camera_pos # Split camara_pos🍆
        #
        key = pygame.key.get_pressed() # Get Keyboard Input🍆
        if key[pygame.K_UP]: # Check Key
            self.rect.y -= Player.image_speed # Move Player Rect Coord
            pos_y +=  Player.image_speed # Move Camara Coord Against Player Rect
        if key[pygame.K_LEFT]:
            self.rect.x -= Player.image_speed 
            pos_x += Player.image_speed 
        if key[pygame.K_DOWN]:
            self.rect.y += Player.image_speed 
            pos_y -= Player.image_speed 
        if key[pygame.K_RIGHT]:
            self.rect.x += Player.image_speed 
            pos_x -= Player.image_speed 
        #
        if self.rect.x < 0: # Simple Sides Collision
            self.rect.x = 0 # Reset Player Rect Coord
            pos_x = camera_pos[0] #Reset Camera Pos Coord
        elif self.rect.x > 1980: #Set the Player`s moving range
            self.rect.x = 1980
            pos_x = camera_pos[0]
        if self.rect.y < 0:
            self.rect.y = 0
            pos_y = camera_pos[1]
        elif self.rect.y > 1980:
            self.rect.y = 1980
            pos_y = camera_pos[1]
        #
        return (pos_x,pos_y) # Return New Camera Pos
    def render(self,display):
        display.blit(self.image,(self.rect.x,self.rect.y))
###
#
#
###
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
    display = pygame.display.set_mode((1000,600))
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