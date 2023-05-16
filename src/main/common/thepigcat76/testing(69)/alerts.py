import pygame

pygame.init()


class notification:
    def __init__(self, barPath, iconPath, scale, x, y, stopTimer):
        self.x, self.y = x, y
        self.timer = 0
        self.font = pygame.font.Font(
            "src\main/assets/fonts\joystixmonospaceregular.otf", 25
        )
        self.stopTimer = stopTimer
        self.finished = False
        self.notification_bar = pygame.image.load(barPath)
        self.scaledTexture = pygame.transform.scale(
            self.notification_bar,
            (
                self.notification_bar.get_width() * scale,
                self.notification_bar.get_height() * scale,
            ),
        )
        self.icon = pygame.image.load(iconPath)
        self.scaledIcon = pygame.transform.scale(self.icon, (64, 64))

    def render(self, surface, text1, text2, textColor):
        self.text1 = self.font.render(text1, True, textColor)
        self.text2 = self.font.render(text2, True, textColor)
        if self.timer >= self.stopTimer:
            self.timer = self.stopTimer
        else:
            self.timer += 1

        if (
            not self.x + self.scaledTexture.get_width() <= surface.get_width()
            and self.finished == False
        ):
            self.x -= 10
        else:
            self.finished = True

        if (
            self.finished == True
            and self.timer == self.stopTimer
            and not self.x >= surface.get_width() + self.scaledTexture.get_width()
        ):
            self.x += 10
        elif self.finished == False:
            self.timer = 0
        if (
            self.finished == True
            and self.x <= surface.get_width() - self.scaledTexture.get_width()
            and not self.timer == self.stopTimer
        ):
            self.x = surface.get_width() - self.scaledTexture.get_width()
        surface.blit(self.scaledTexture, (self.x, self.y))
        self.scaledTexture.blit(self.text1, (100, self.scaledTexture.get_height() // 6))
        self.scaledTexture.blit(
            self.text2, (100, self.scaledTexture.get_height() // 4 * 2)
        )
        self.scaledTexture.blit(self.scaledIcon, (16, 16))
        # use self.finished = False to reset the bar


class infoPanel:
    def __init__(self, panelPath, scale):
        self.visible = True
        self.font = pygame.font.Font(
            "src\main/assets/fonts\joystixmonospaceregular.otf", 25
        )
        self.panel = pygame.image.load(panelPath)
        self.scaledPanel = pygame.transform.scale(
            self.panel,
            (self.panel.get_width() * scale, self.panel.get_height() * scale),
        )

    def render(
        self,
        surface,
        x,
        y,
        text1,
        text2,
        text3,
        text4,
        text5,
        text6,
        text7,
        text8,
        text9,
        text10,
        text11,
        text12,
        textColor,
        xOffset,
        yOffset,
    ):
        self.text1 = self.font.render(text1, True, textColor)
        self.text2 = self.font.render(text2, True, textColor)
        self.text3 = self.font.render(text3, True, textColor)
        self.text4 = self.font.render(text4, True, textColor)
        self.text5 = self.font.render(text5, True, textColor)
        self.text6 = self.font.render(text6, True, textColor)
        self.text7 = self.font.render(text7, True, textColor)
        self.text8 = self.font.render(text8, True, textColor)
        self.text9 = self.font.render(text9, True, textColor)
        self.text10 = self.font.render(text10, True, textColor)
        self.text11 = self.font.render(text11, True, textColor)
        self.text12 = self.font.render(text12, True, textColor)
        if self.visible == True:
            surface.blit(self.scaledPanel, (x, y))
            self.scaledPanel.blit(self.text1, (16 - xOffset, 16 - yOffset))
            self.scaledPanel.blit(self.text2, (16 - xOffset, 48 - yOffset))
            self.scaledPanel.blit(self.text3, (16 - xOffset, 80 - yOffset))
            self.scaledPanel.blit(self.text4, (16 - xOffset, 112 - yOffset))
            self.scaledPanel.blit(self.text5, (16 - xOffset, 144 - yOffset))
            self.scaledPanel.blit(self.text6, (16 - xOffset, 160 - yOffset))
            self.scaledPanel.blit(self.text7, (16 - xOffset, 176 - yOffset))
            self.scaledPanel.blit(self.text8, (16 - xOffset, 192 - yOffset))
            self.scaledPanel.blit(self.text9, (16 - xOffset, 208 - yOffset))
            self.scaledPanel.blit(self.text10, (16 - xOffset, 224 - yOffset))
            self.scaledPanel.blit(self.text11, (16 - xOffset, 240 - yOffset))
            self.scaledPanel.blit(self.text12, (16 - xOffset, 256 - yOffset))


class infoPanelIcon:
    def __init__(self, panelPath, iconPath, scale):
        self.visible = True
        self.font = pygame.font.Font(
            "src\main/assets/fonts\joystixmonospaceregular.otf", 25
        )
        self.panel = pygame.image.load(panelPath)
        self.scaledPanel = pygame.transform.scale(
            self.panel,
            (self.panel.get_width() * scale, self.panel.get_height() * scale),
        )
        self.icon = pygame.image.load(iconPath)
        self.scaledIcon = pygame.transform.scale(self.icon, (15 * scale, 15 * scale))

    def render(
        self,
        surface,
        x,
        y,
        text1,
        text2,
        text3,
        text4,
        text5,
        text6,
        text7,
        text8,
        text9,
        text10,
        text11,
        text12,
        textColor,
        xOffset,
        yOffset,
    ):
        self.text1 = self.font.render(text1, True, textColor)
        self.text2 = self.font.render(text2, True, textColor)
        self.text3 = self.font.render(text3, True, textColor)
        self.text4 = self.font.render(text4, True, textColor)
        self.text5 = self.font.render(text5, True, textColor)
        self.text6 = self.font.render(text6, True, textColor)
        self.text7 = self.font.render(text7, True, textColor)
        self.text8 = self.font.render(text8, True, textColor)
        self.text9 = self.font.render(text9, True, textColor)
        self.text10 = self.font.render(text10, True, textColor)
        self.text11 = self.font.render(text11, True, textColor)
        self.text12 = self.font.render(text12, True, textColor)
        if self.visible == True:
            surface.blit(self.scaledPanel, (x, y))
            self.scaledPanel.blit(
                self.scaledIcon,
                (
                    self.scaledPanel.get_width() // 6 * 4.97,
                    self.scaledIcon.get_height() * 1.57,
                ),
            )
            self.scaledPanel.blit(
                self.text1,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text2,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 1.25 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text3,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 1.5 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text4,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 1.75 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text5,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 2 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text6,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 2.25 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text7,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 2.5 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text8,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 2.75 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text9,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 3 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text10,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 3.25 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text11,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 3.5 - yOffset,
                ),
            )
            self.scaledPanel.blit(
                self.text12,
                (
                    self.scaledPanel.get_width() // 5 - xOffset,
                    self.scaledPanel.get_height() // 5 * 3.75 - yOffset,
                ),
            )


class infoPanelAnimatedIcon:
    def __init__(self, panelPath, scale):
        self.visible = True
        self.scale = scale
        self.frame = 0
        self.font = pygame.font.Font(
            "src\main/assets/fonts\joystixmonospaceregular.otf", 25
        )
        self.panel = pygame.image.load(panelPath)
        self.scaledPanel = pygame.transform.scale(
            self.panel,
            (self.panel.get_width() * scale, self.panel.get_height() * scale),
        )

    def render(
        self,
        surface,
        x,
        y,
        text1,
        text2,
        text3,
        text4,
        text5,
        text6,
        text7,
        text8,
        text9,
        text10,
        textColor,
        xOffset,
        yOffset,
        animationArray,
    ):
        if not self.frame >= len(animationArray) - 1:
            self.frame += 1
        else:
            self.frame = 0
        self.texture = animationArray[self.frame]
        self.scaledTexture = pygame.transform.scale(
            self.texture, (15 * self.scale, 15 * self.scale)
        )
        self.text1 = self.font.render(text1, True, textColor)
        self.text2 = self.font.render(text2, True, textColor)
        self.text3 = self.font.render(text3, True, textColor)
        self.text4 = self.font.render(text4, True, textColor)
        self.text5 = self.font.render(text5, True, textColor)
        self.text5 = self.font.render(text6, True, textColor)
        self.text5 = self.font.render(text7, True, textColor)
        self.text5 = self.font.render(text8, True, textColor)
        self.text5 = self.font.render(text9, True, textColor)
        self.text5 = self.font.render(text10, True, textColor)
        if self.visible == True:
            surface.blit(self.scaledPanel, (x, y))
            self.scaledPanel.blit(
                self.scaledTexture,
                (
                    self.scaledPanel.get_width() // 6 * 4.97,
                    self.scaledTexture.get_height() * 1.57,
                ),
            )
            self.scaledPanel.blit(self.text1, (16 - xOffset, 16 - yOffset))
            self.scaledPanel.blit(self.text2, (16 - xOffset, 48 - yOffset))
            self.scaledPanel.blit(self.text3, (16 - xOffset, 80 - yOffset))
            self.scaledPanel.blit(self.text4, (16 - xOffset, 112 - yOffset))
            self.scaledPanel.blit(self.text5, (16 - xOffset, 144 - yOffset))
