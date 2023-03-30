import pygame

pygame.init()
class registerGui():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y),(int(32 * 5), int(32 * 5)))

    def blitGui(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect, 4)