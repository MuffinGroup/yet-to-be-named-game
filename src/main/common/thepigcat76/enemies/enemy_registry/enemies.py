import pygame
import registerEnemies

SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('enemy_testing')

#create button instances
enemy = registerEnemies.enemies("enemy1", 2, 100, 100)

#game loop
run = True
while run:

	screen.fill((202, 228, 241))

	enemy.draw(screen)

	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False

	pygame.display.update()

pygame.quit()
