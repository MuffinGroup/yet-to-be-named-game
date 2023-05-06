import pygame

class notification:
    def __init__(self, path, scale, x, y):
        self.x, self.y = x, y
        self.finished = False
        self.notification_bar = pygame.image.load(path)
        self.scaledTexture = pygame.transform.scale(self.notification_bar, (self.notification_bar.get_width() * scale, self.notification_bar.get_height() * scale))

    def render(self, surface):
        if not self.x + self.scaledTexture.get_width() <= surface.get_width():
            self.x -= 10
        else:
            self.finished = True
        if self.finished == True and self.x <= surface.get_width() - self.scaledTexture.get_width():
            self.x = surface.get_width() - self.scaledTexture.get_width()
        surface.blit(self.scaledTexture, (self.x, self.y))

class infoToast:
    def __init__(self):
        pass

    def render(self):
        pass