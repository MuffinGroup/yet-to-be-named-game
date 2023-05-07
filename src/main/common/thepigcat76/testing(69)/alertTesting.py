import pygame
from alerts import *

screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)
player = pygame.Rect(100, 500, 100, 100)
object = pygame.Rect((1400, 600), (100, 100))
jumping = False
x = -16
modifier = 1
jumped = False
e = False
example = notification("src\main/assets/textures\elements\gui/notification_bar.png", "src\main/assets/textures\elements\Environment\decoration\Plants\poppy.png", 3, screen.get_width(), 200, 100)
examplePanel = infoPanelIcon("src\main/assets/textures\elements\gui/info_panel_icon.png", "src\main/assets/textures\elements\gui/slot.png", 8)

while True:
	clock = pygame.time.Clock()
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
	if keys[pygame.K_RIGHT]:
		player.x += 10
	if keys[pygame.K_LEFT]:
		player.x -= 10
	if keys[pygame.K_UP]:
		player.y -= 10
	if keys[pygame.K_DOWN]:
		player.y += 10
	if keys[pygame.K_0] and x == -16:
		x = 15

	if x == 15:
		object.y -= 3*1.1*modifier
		object.x -= 12
		if object.x < 650:
			modifier = -1
		if object.x <= 100:
			object.x = 100
			object.y = 500

	screen.fill((90, 90, 90))
	pygame.draw.rect(screen, (255, 255, 255), player, 1000)
	pygame.draw.rect(screen, (255, 0, 255), object, 500)
	example.render(screen, "uwuuuuuuuu", "uuuuuuuu", (255, 255, 255))
	examplePanel.render(screen, screen.get_width()//20, screen.get_width()//20, "warum aa", "wieso", "weshalb", "wie", "was", (255, 255, 255), -10, -10)
	if pygame.key.get_pressed()[pygame.K_1]:
		example.finished = False
	print(example.x)
	pygame.display.flip()
	clock.tick(60)