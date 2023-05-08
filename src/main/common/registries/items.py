import pygame

pygame.init()

class registerItem():
    def __init__(self, id, texturePath):
        self.id = id
        self.pickedUp = False
        self.texture = pygame.image.load("src\main/assets/textures/" + texturePath + ".png")
        self.texture = pygame.transform.scale(self.texture, (self.texture.get_width() * 2.5, self.texture.get_height() * 2.5))
    
    def drawItem(self, surface, player, x, y):
        self.hitbox = pygame.Rect((x, y), (self.texture.get_width(), self.texture.get_height()))
        surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))
        if self.pickedUp == True:
            self.hitbox.x, self.hitbox.y = pygame.mouse.get_pos()
            self.hitbox.x -= self.texture.get_width()//2
            self.hitbox.y -= self.texture.get_height()//2
        if player.rect.colliderect(self.hitbox):
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.draw.rect(surface, (255, 255, 255), self.hitbox, 3)