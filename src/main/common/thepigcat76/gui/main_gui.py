import pygame
import gui
import colors

# Initialize Pygame
pygame.init()

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
test = gui.registerGui(100, 100, 100, 100, True, "placeholder_startscreen")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
    test.draw(screen, colors.BLUISH_GRAY)

    pygame.display.update()