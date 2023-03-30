import pygame

pygame.init()
class registerGui():
    def __init__(self, x, y):
        self.window = pygame.Rect((x, y),(int(32 * 5), int(32 * 5)))

    def blitGui(self, surface, color, outline):
        pygame.draw.rect(surface, color, self.window, outline)

    def addObject(self, object):
        pass

    def addText(self, text):
        pass

    def addButton(self, button):
        pass

    def addToggle(self, button):
        pass

    def addSlot(self, slot):
        pass