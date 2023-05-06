import pygame

pygame.init()
class notification:
    def __init__(self, barPath, iconPath, scale, x, y, stopTimer):
        self.x, self.y = x, y
        self.timer = 0
        self.font = pygame.font.Font("src\main/assets/fonts\joystixmonospaceregular.otf", 25)
        self.stopTimer = stopTimer
        self.finished = False
        self.notification_bar = pygame.image.load(barPath)
        self.scaledTexture = pygame.transform.scale(self.notification_bar, (self.notification_bar.get_width() * scale, self.notification_bar.get_height() * scale))
        self.icon = pygame.image.load(iconPath)
        self.scaledIcon = pygame.transform.scale(self.icon, (64, 64))

    def render(self, surface, text1, text2, textColor):
        self.text1 = self.font.render(text1, True, textColor)
        self.text2 = self.font.render(text2, True, textColor)
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
        self.scaledTexture.blit(self.text1, (100, self.scaledTexture.get_height()//6))
        self.scaledTexture.blit(self.text2, (100, self.scaledTexture.get_height()//4*2))
        self.scaledTexture.blit(self.scaledIcon, (16, 16))
        #use self.finished = False to reset the bar

class infoToast:
    def __init__(self):
        pass

    def render(self):
        pass