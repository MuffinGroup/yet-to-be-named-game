import pygame
import registerButton
from colors import *

pygame.init()
mouse = pygame.mouse.get_pos
screen = pygame.display.set_mode((720,720))
smallfont = pygame.font.SysFont('Corbel',35)
start = smallfont.render('Start Game' , True , COLORS.WHITE)
quit = smallfont.render('Quit Game' , True , COLORS.WHITE)
icon = pygame.image.load('src//main//assets//icon//icon.png')
icon_selected = pygame.image.load('src//main//assets//icon//icon_selected.png')
pygame.display.set_icon(icon)
start_button = registerButton.Button(250, 100, icon, icon_selected, 0.8, "start", COLORS.BLACK, "joystixmonospaceregular")
quit_button = registerButton.Button(250, 400, icon, icon_selected, 0.8, "quit", COLORS.BLACK, "joystixmonospaceregular")
clock = pygame.time.Clock()

while True:
    #screen.blit(img, (0, 0))
	screen.fill(COLORS.GRAY)

	if start_button.draw(screen):
		print("Pressed Start")
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