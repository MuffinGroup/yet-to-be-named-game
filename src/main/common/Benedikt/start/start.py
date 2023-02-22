import pygame
import registerButton
from colors import *

pygame.init()
mouse = pygame.mouse.get_pos
screen = pygame.display.set_mode((720,720), pygame.RESIZABLE)
smallfont = pygame.font.SysFont('Corbel',35)
start = smallfont.render('Start Game' , True , COLORS.WHITE)
quit = smallfont.render('Quit Game' , True , COLORS.WHITE)
icon = pygame.image.load('src//main//assets//gui//icon//icon.png')
icon_selected = pygame.image.load('src//main//assets//gui//icon//icon_selected.png')
button = pygame.image.load('src//main//assets//gui//button.png')
button_selected = pygame.image.load('src//main//assets//gui//button_selected.png')
pygame.display.set_icon(icon)
start_button = registerButton.Button("button" ,200, 100, 6.0, "start", COLORS.BLACK, "joystixmonospaceregular")
options_button = registerButton.Button("button", 200, 300,  6.0, "options", COLORS.BLACK, "joystixmonospaceregular")
quit_button = registerButton.Button("button", 200, 500,  6.0, "quit", COLORS.BLACK, "joystixmonospaceregular")
clock = pygame.time.Clock()

while True:
    #screen.blit(img, (0, 0))
	screen.fill(COLORS.GRAY)

	if start_button.draw(screen):
		print("Pressed Start")
	if options_button.draw(screen):
		print("Pressed Options")
	if quit_button.draw(screen):
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
	pygame.display.update()
	clock.tick(60)