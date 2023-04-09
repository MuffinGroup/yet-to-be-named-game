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
        self.rectCount = 0    
    
    def registerRect(self, color, x, y, width, height, borderThickness, rectArray):
        self.rect = pygame.Rect(x, y, width, height)
        rectArray.append(self.rect)
        self.rectCount += 1
        self.rectColor = color
        self.borderThickness = borderThickness
        print(self.rectCount)
        
    def draw(self, surface, color, rectArray):
        surface.blit(self.window, (self.x, self.y))
        self.rect.x += 1
        if self.backgroundImage == True:
            self.window.fill(color)
            self.window.blit(self.bgImage, (0, 0))
        for loads in rectArray:
            self.window.blit(self.bgImage, (self.rect.x, self.rect.y))
            
