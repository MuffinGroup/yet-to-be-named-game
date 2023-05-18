import pygame
import registries.elements
import registries.gui
from registries.colors import *
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()

chatBackground = registries.gui.registerGui(50, 50, 150, 50, False)
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
cobble = registries.elements.registerElement("elements\Environment\Blocks\cobble", 3)
textBox = registries.gui.registerTextBox(30, BLACK, BLACK, BLACK, 70, 50, 50, 150, 50)
textBoxOpen = False

map = [[ 1, 1, 1, 0, 0, 0],
       [ 1, 1, 1, 0, 0, 0],
       [ 1, 1, 1, 0, 0, 0]]

run = True
while run:
	screen.fill(BLUE)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
		try:
			textBox.event(event)
		except:
			pass
	
	tile_rects = []
	y = 0
	for row in map:
		x = 0
		for tile in row:
			if tile == 1:
				cobble.drawElement(screen, x, y, tile_rects)
			x += 1
		y += 1

	y = 0
	for row in range(len(map)):
		x = 0
		for i in range(len(map[0])):
			selectionBox = pygame.Rect((x * 96, y * 96), (96, 96))
			if not selectionBox.collidepoint(pygame.mouse.get_pos()):
				pygame.draw.rect(screen, (255, 255, 255), selectionBox, 3)
			elif selectionBox.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
				pygame.draw.rect(screen, (255, 0, 255), selectionBox, 3)
				try:
					map[selectionBox.y//96][selectionBox.x//96] = int(textBox.userInput)
				except:
					textBox.clear()
			x += 1
		y += 1
	
	if pygame.key.get_pressed()[pygame.K_t]:
		textBoxOpen = True
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		textBoxOpen = True

	if textBoxOpen == True:
		chatBackground.draw(screen, "default")
		textBox.draw(screen)

	clock.tick(60)
	pygame.display.update()