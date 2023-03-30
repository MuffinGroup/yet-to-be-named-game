import pygame
import gui

# Initialize Pygame
pygame.init()

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")
test = gui.registerGui(100, 100)

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
    
    test.blitGui(screen)
    pygame.display.update()