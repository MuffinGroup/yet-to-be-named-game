import pygame
import registerButton
from colors import *

pygame.init()
mouse = pygame.mouse.get_pos
res = (720,720)
screen = pygame.display.set_mode(res)
color = (255,255,255)
color_light = (COLORS.RED)
color_dark = (100,100,100)
width = screen.get_width()
height = screen.get_height()
smallfont = pygame.font.SysFont('Corbel',35)
start = smallfont.render('Start Game' , True , color)
quit = smallfont.render('Quit Game' , True , color)
icon = pygame.image.load('src//main//assets//icon//icon.png')
icon_selected = pygame.image.load('src//main//assets//icon//icon_selected.png')
pygame.display.set_icon(icon)
start_button = registerButton.Button(100, 100, icon, 0.8)
clock = pygame.time.Clock()

run = True
while run:

	screen.fill(COLORS.GRAY)

	if start_button.draw(screen):
		print('START')
	
	if mouse == (width, height):
		print("success")

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
    #screen.blit(img, (0, 0))