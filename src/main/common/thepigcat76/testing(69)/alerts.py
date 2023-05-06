import pygame

class notification:
    def __init__(self, path, startX, startY, scale):
        self.notification_bar = pygame.image.load(path)
        self.scaledTexture = pygame.transform.scale(self.notification_bar, (self.notification_bar.get_width() * scale, self.notification_bar.get_height() * scale))
        self.startX, self.startY = startX, startY

    def render(self, surface):
        surface.blit(self.scaledTexture, (self.startX, self.startY))

class infoToast:
    def __init__(self):
        pass

    def render(self):
        pass