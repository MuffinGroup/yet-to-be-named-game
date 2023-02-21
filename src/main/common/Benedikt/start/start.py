import pygame
import registerButton
from colors import *

pygame.init()
mouse = pygame.mouse.get_pos
screen = pygame.display.set_mode((720,720))
color_light = (COLORS.RED)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel',35)
start = smallfont.render('Start Game' , True , COLORS.WHITE)
quit = smallfont.render('Quit Game' , True , COLORS.WHITE)
icon = pygame.image.load('src//main//assets//icon//icon.png')
icon_selected = pygame.image.load('src//main//assets//icon//icon_selected.png')
pygame.display.set_icon(icon)
start_button = registerButton.Button(100, 100, icon, icon_selected, 0.8)
clock = pygame.time.Clock()

while True:

	screen.fill(COLORS.GRAY)

	if start_button.draw(screen):
		print('START')
	
	if mouse == (width, height):
		print("success")

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
			exit()
			print("Closed successful")
	pygame.display.update()
    #screen.blit(img, (0, 0))