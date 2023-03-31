import pygame

pygame.init()
class Rect():
    def __init__(self, x, y, width, height):
        self.object = pygame.Rect((x, y), (width, height))
            
    def drawRect(self, menu, color, outline):
        pygame.draw.rect(menu, color, self.object, outline)