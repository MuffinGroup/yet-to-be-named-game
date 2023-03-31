import pygame
import buttons.colors
import buttons.registerButton
import gui

# Initialize Pygame
pygame.init()

#Load background
menu = pygame.Surface((800, 800))
element = gui.Rect(500, 100, 100, 100)
buttonTest = buttons.registerButton.Button("button", 300, 300, 6.0, "ererer", buttons.colors.PURPLE, "joystixmonospaceregular")

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()

    menu.fill(buttons.colors.BLUE)
    element.drawRect(menu, buttons.colors.ORANGE, 100)
    if buttonTest.draw(menu, 0, 0):
        print("e")
    screen.blit(menu, (100, 100))
    
    pygame.display.update()