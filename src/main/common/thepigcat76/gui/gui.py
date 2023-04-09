import pygame

pygame.init()
class registerGui():
    def __init__(self, x, y, width, height, backgroundImage, imagePath):
        if backgroundImage == True:
            self.bgImage = pygame.image.load("src/main/assets/textures/elements/background/" + imagePath + ".png")
            self.backgroundImage = True
        else:
            self.backgroundImage = False
        self.window = pygame.Surface((width, height))
        self.x, self.y = x,y
    
    def draw(self, surface, color):
        surface.blit(self.window, (self.x, self.y))
        if self.backgroundImage == True:
            self.window.blit(self.bgImage, (0, 0))
            print("we")
        else:
            self.window.fill(color)
