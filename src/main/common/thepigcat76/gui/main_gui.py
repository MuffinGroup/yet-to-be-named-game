import pygame
import gui
import colors

# Initialize Pygame
pygame.init()

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)
test = gui.registerGui(100, 100, 1000, 1000, True, "placeholder_startscreen")
test2 = gui.registerObject(100, 100, 100, 100, colors.DARK_ORANGE, 10)
test3 = gui.registerObject(200, 100, 100, 100, colors.DARK_ORANGE, 10)
test4 = gui.registerButton("button", 300, 200, 5, "test", colors.YELLOW, "joystixmonospaceregular")
#test.registerRect(colors.WHITE, 100, 100, 50, 69, 69420, test2) #both rects are test.rect which means they can't co-exist. Replace the self with something else and add a surface operator

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
    test.draw(screen, colors.BLUISH_GRAY)
    test2.drawObject(test.window)
    test3.drawObject(test.window)
    if test4.draw(test.window, 0, 0):
        print("e")

    pygame.display.update()