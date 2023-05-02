import pygame

screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)
player = pygame.Rect(100, 500, 100, 100)
object = pygame.Rect((300, 300), (100, 100))
jumping = False
x = 12
modifier = 1
jumped = False

while True:
	clock = pygame.time.Clock()
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	if keys[pygame.K_RIGHT]:
		player.x += 10
	if keys[pygame.K_LEFT]:
		player.x -= 10
	if keys[pygame.K_UP]:
		player.y -= 10
	if keys[pygame.K_DOWN]:
		player.y += 10
	if keys[pygame.K_0]:
		jumped = True
	else:
		jumped = False
	if jumped == True:
		object.y += 100
    
	screen.fill((90, 90, 90))
	pygame.draw.rect(screen, (255, 255, 255), player, 1000)
	pygame.draw.rect(screen, (255, 0, 255), object, 500)
	pygame.display.flip()
	clock.tick(60)