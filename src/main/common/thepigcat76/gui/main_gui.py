import pygame
import gui
import colors

# Initialize Pygame
pygame.init()

x = 100
y = 100
# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
test = gui.registerGui(x, y, 2000, 1000, False, "placeholder_startscreen")
test8 = gui.registerChat(3, 30, colors.WHITE, colors.WHITE, colors.WHITE, 330, 270, 100, 800, 600, 300, 575, 735, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
        test8.event(event)
    test.draw(screen, colors.BLUISH_GRAY)
    test8.drawChat(test.window)
    pygame.display.update()