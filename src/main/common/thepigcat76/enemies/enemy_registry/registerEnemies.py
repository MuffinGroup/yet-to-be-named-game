import pygame

class enemies():
    def __init__(self, enemy_name, scale, x, y): #, speed, tracking_range
        texture = pygame.image.load('src/main/assets/entities/' + enemy_name + '.png')
        width = texture.get_width
        height = texture.get_height
        self.texture = pygame.transform.scale(texture, (int(width * scale), int(height * scale)))
        self.rect = self.texture.get_rec
        self.rect.center = (x, y)

    def draw(self, surface):
        action = False
        Mousepos = pygame.mouse.get_pos
        surface.blit(self.texture, (self.rect.x, self.rect.y))
