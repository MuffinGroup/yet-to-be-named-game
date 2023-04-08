import pygame

pygame.init()
class registerGui():
    def __init__(self, x, y, width, height):
        self.window = pygame.Surface((width, height))
        self.x, self.y = x,y
    
    def draw(self, surface, color):
        surface.blit(self.window, (self.x, self.y))
        self.window.fill(color)
