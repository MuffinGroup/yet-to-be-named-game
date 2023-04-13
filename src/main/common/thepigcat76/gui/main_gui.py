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
test2 = gui.registerObject(100, 100, 100, 100, colors.DARK_ORANGE, 10)
test3 = gui.registerObject(200, 100, 100, 100, colors.DARK_ORANGE, 10)
test4 = gui.registerButton("button", 300, 500, 5, "test", colors.YELLOW, "joystixmonospaceregular")
test5 = gui.registerButton("toggle", 300, 700, 10, "test", colors.YELLOW, "joystixmonospaceregular")
test6 = gui.registerFont(30, "uwu", colors.GREEN)
test7 = gui.registerImages("elements/gui/icon/icon")
test8 = gui.registerChat(3, 30, colors.WHITE, colors.WHITE, colors.WHITE, 330, 270, 100, 800, 600, 300, 575, 735, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
        test8.event(event)
    test.draw(screen, colors.BLUISH_GRAY)
    #test2.drawObject(test.window)
    #test3.drawObject(test.window)
    #test6.drawFont(test.window, 100, 300)
    #if test4.draw(test.window, 0, 0, x, y):
        #print("e")
    #if test5.drawToggle(test.window, x, y):
        #print("weeee")
    #test7.drawImage(test.window, 300, 400)
    test8.drawChat(test.window)
    pygame.display.update()