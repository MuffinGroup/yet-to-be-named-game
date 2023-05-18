import pygame
import registries.elements
import pickle
from os import path

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
cobble = registries.elements.registerElement("elements\Environment\Blocks\cobble", 3)

map = [[ 1, 1, 1],
       [ 1, 1, 1]]

run = True
while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	
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
	for row in range(len(map) + 1):
		x = 0
		for i in range(len(map[0]) + 1):
			selectionBox = pygame.Rect((x * 96, y * 96), (96, 96))
			if not selectionBox.collidepoint(pygame.mouse.get_pos()):
				pygame.draw.rect(screen, (255, 255, 255), selectionBox, 3)
			else:
				pygame.draw.rect(screen, (255, 0, 255), selectionBox, 3)
			x += 1
		y += 1

	clock.tick(60)
	pygame.display.update()