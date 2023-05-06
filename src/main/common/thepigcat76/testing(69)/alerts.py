import pygame

class notification:
    def __init__(self, path, scale, x, y, text, stopTimer):
        self.x, self.y = x, y
        self.timer = 0
        self.stopTimer = stopTimer
        self.finished = False
        self.notification_bar = pygame.image.load(path)
        self.scaledTexture = pygame.transform.scale(self.notification_bar, (self.notification_bar.get_width() * scale, self.notification_bar.get_height() * scale))

    def render(self, surface):
        if self.timer >= self.stopTimer:
           self.timer = self.stopTimer
        else:
            self.timer += 1

        if not self.x + self.scaledTexture.get_width() <= surface.get_width() and self.finished == False:
            self.x -= 10
        else:
            self.finished = True

        if self.finished == True and self.timer == self.stopTimer and not self.x >= surface.get_width() + self.scaledTexture.get_width():
            self.x += 10
        elif self.finished == False:
            self.timer = 0
        if self.finished == True and self.x <= surface.get_width() - self.scaledTexture.get_width() and not self.timer == self.stopTimer:
            self.x = surface.get_width() - self.scaledTexture.get_width()
        surface.blit(self.scaledTexture, (self.x, self.y))
        #use self.finished = False to reset the bar

class infoToast:
    def __init__(self):
        pass

    def render(self):
        pass