import pygame

pygame.init()

class registerItem():
    def __init__(self, id, name, texturePath):
        self.texture = pygame.image.load("src\main/assets/textures\elements/" + texturePath + ".png")
        self.texture = pygame.transform.scale(self.texture, (self.texture.get_width() * 2.5, self.texture.get_height() * 2.5))
        self.id = id
        self.hitbox = self.texture.get_rect()
    
    def drawItem(self, surface, x, y):
        surface.blit(self.texture, (x, y))