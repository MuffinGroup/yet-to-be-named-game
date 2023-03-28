import pygame
import colors
import json_testing

# Initialize Pygame
pygame.init()

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

textfont = pygame.font.SysFont('joystixmonospaceregular', 30)
text = textfont.render(str(json_testing.test), True, colors.WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            
    screen.blit(text, (330,310))
    pygame.display.update()