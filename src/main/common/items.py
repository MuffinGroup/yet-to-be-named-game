import pygame

pygame.init()

class registerItem():
    def __init__(self, id, texturePath):
        global pickingUp, finishedPickup
        pickingUp = False
        self.id = id
        self.pickedUp = False
        self.frame = 0
        self.xNewNew, self.yNewNew = 0, 0
        self.pickingUp = False
        finishedPickup = False
        self.texture = pygame.image.load("src\main/assets/textures/" + texturePath + ".png")
        self.texture = pygame.transform.scale(self.texture, (self.texture.get_width() * 2.5, self.texture.get_height() * 2.5))
    
    def drawItem(self, surface, player, x, y):
        global pickingUp, finishedPickup
        self.x, self.y = x, y
        if player.visible == True:
            if self.pickedUp == False:
                if self.xNewNew == 0 and self.yNewNew == 0:
                    self.hitbox = pygame.Rect((x, y), (self.texture.get_width(), self.texture.get_height()))
                    surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))
                else:
                    self.hitbox = pygame.Rect((self.xNewNew, self.yNewNew), (self.texture.get_width(), self.texture.get_height()))
                    surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))
            if self.pickedUp == True:
                player.holding = self
                self.texture = pygame.transform.scale(self.texture, (player.rect.width//1.5, player.rect.width//1.5))
                if player.facingRight == True:
                    self.xNew, self.yNew = player.rect.x + player.rect.width//16 + 20, player.rect.y + player.rect.height//2 + 15
                    self.flippedTexture = pygame.transform.rotate(self.texture, -90)
                else:
                    self.xNew, self.yNew = player.rect.x - player.rect.width//16 + 20, player.rect.y + player.rect.height//2 + 15
                    self.flippedTexture = pygame.transform.rotate(self.texture, 90)
                self.hitbox = pygame.Rect((self.xNew, self.yNew), (self.texture.get_width(), self.texture.get_height()))
                surface.blit(self.flippedTexture, (self.xNew, self.yNew))

            if player.rect.colliderect(self.hitbox):
                if pygame.key.get_pressed()[pygame.K_e]:
                    pickingUp = True

            if finishedPickup == True:
                self.pickedUp = True
                finishedPickup = False

    def drawGhostItem(self, surface, x, y):
        self.hitbox = pygame.Rect((x, y), (self.texture.get_width(), self.texture.get_height()))
        surface.blit(self.texture, (self.hitbox.x, self.hitbox.y))