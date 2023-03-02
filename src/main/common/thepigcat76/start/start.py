import pygame
import registerButton
from colors import *

start_background = pygame.image.load("src/main/assets/elements/background/start.jpg")

pygame.init()
smallfont = pygame.font.SysFont("joystixmonospaceregular", 40)
name = smallfont.render("YET TO BE NAMED GAME" , True , COLORS.DARKER_GRAY)
mouse = pygame.mouse.get_pos
screen = pygame.display.set_mode((720,720), pygame.RESIZABLE)
start = smallfont.render('Start Game' , True , COLORS.WHITE)
quit = smallfont.render('Quit Game' , True , COLORS.WHITE)
icon = pygame.image.load('src\main/assets\gui/icon\MuffinLogo.png')
icon_selected = pygame.image.load('src//main//assets//gui//icon//icon_selected.png')
button = pygame.image.load('src//main//assets//gui//button.png')
button_selected = pygame.image.load('src//main//assets//gui//button_selected.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
start_button = registerButton.Button("button" ,350, 250, 6.0, "start", COLORS.BLACK, "joystixmonospaceregular")
options_button = registerButton.Button("button", 350, 450,  6.0, "options", COLORS.BLACK, "joystixmonospaceregular")
quit_button = registerButton.Button("button", 350, 650,  6.0, "quit", COLORS.BLACK, "joystixmonospaceregular")
clock = pygame.time.Clock()

while True:
    #screen.blit(img, (0, 0))
	screen.blit(start_background, (0,0))

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
	screen.blit(name , (40, 50))
	pygame.display.update()
	clock.tick(60)