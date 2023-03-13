import pygame

class Player():
    def __init__(currentImage):
        Player.rightImage = pygame.image.load("src\main/assets\entities\characters\Character1\Animations\Character1.png") # Create Player Image
        Player.leftImage = pygame.transform.flip(Player.rightImage, True, False)
        Player.currentImage = Player.rightImage
        Player.image_speed= 5 
        Player.rect = pygame.Rect((50,50),(30,30)) # Create Player Rect
    def move(self,camera_pos):
         self.running = True
         self.jumpvar = -16
         self.doorhandling = 0
         self.visible = True
         self.standing = True
         self.walking = False
         self.jumping = False
         pos_x,pos_y = camera_pos # Split camara_pos
         key = pygame.key.get_pressed() # Get Keyboard Input
         if key[pygame.K_UP] and self.visible == True: # Check Key
            self.rect.y -= Player.image_speed # Move Player Rect Coord
            pos_y +=  Player.image_speed # Move Camara Coord Against Player Rect
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