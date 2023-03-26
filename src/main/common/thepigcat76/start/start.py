import pygame
import registerButton
import colors
import animations

pygame.init()
screen = pygame.display.set_mode((720,720), pygame.RESIZABLE)
icon = pygame.image.load('src\main/assets/textures/elements\gui/icon\muffin_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
start_button = registerButton.Button("button" ,350, 250, 6.0, "start", colors.BLACK, "joystixmonospaceregular")
options_button = registerButton.Button("button", 350, 450,  6.0, "options", colors.BLACK, "joystixmonospaceregular")
quit_button = registerButton.Button("button", 350, 650,  6.0, "quit", colors.BLACK, "joystixmonospaceregular")
smallfont = pygame.font.SysFont("joystixmonospaceregular", 40)
name = smallfont.render("YET TO BE NAMED GAME" , True , colors.DARKER_GRAY)
start_background = pygame.image.load("src/main/assets/textures/elements/background/placeholder_startscreen.jpg")
clock = pygame.time.Clock()

while True:
    #screen.blit(img, (0, 0))
	screen.blit(start_background, (0,0))

	if start_button.drawAnimated(screen, animations.startButton, 0, 0, 6, -125, -25):
		print("Pressed Start")
	if options_button.drawAnimated(screen, animations.optionsButton, 48, 48, 6, -90, -25):
		print("optionals")
	if quit_button.drawAnimated(screen, animations.quitButton, 0, 0, 6, -125, -25):
		pygame.quit
		print("Pressed Quit")
		print("Closed successful")
		exit()

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
			print("Closed successful")
			exit()
	screen.blit(name , (40, 50))
	pygame.display.update()
	clock.tick(60)