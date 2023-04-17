import pygame

pygame.init()

class registerItem():
    def __init__(self, id, name, texturePath):
        self.texture = pygame.image.load("src\main/assets/textures\elements/" + texturePath + ".png")
        self.texture = pygame.transform.scale(self.texture, (self.texture.get_width() * 2.5, self.texture.get_height() * 2.5))
        self.id = id
    
    def drawItem(self, surface, x, y):
        pos = pygame.mouse.get_pos()
        self.hitbox = pygame.Rect((x, y), (self.texture.get_width(), self.texture.get_height()))
        self.hitbox.topright = (x, y)
        surface.blit(self.texture, (x, y))
        if self.hitbox.collidepoint(pos):
            pygame.draw.rect(surface, (255, 255, 255), self.hitbox, 10)
            print("item collides")
        print(str(pos) + str(self.hitbox.x) + ", " + str(self.hitbox.y))