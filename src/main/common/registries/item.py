import pygame

pygame.init()

class registerItem():
    def __init__(self, id, name, texturePath):
        self.texture = pygame.image.load("src\main/assets/textures\elements/" + texturePath + ".png")
        self.hitbox = self.texture.get_rect()
    
    def drawItem(self, surface):
        surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))