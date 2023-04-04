import pygame

screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)
player = pygame.Rect(100, 100, 100, 100)

while True:
	keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	if keys[pygame.K_RIGHT] and collidingLeft == False:
		player.x += 1
		facingLeft = True
		facingRight = False
	if keys[pygame.K_LEFT]:
		player.x -= 1
		facingLeft = True
		facingRight = False
	if keys[pygame.K_UP]:
		player.y -= 1
	if keys[pygame.K_DOWN]:
		player.y += 1
    
	screen.fill((90, 90, 90))
	pygame.draw.rect(screen, (255, 255, 255), player, 1000)
	pygame.display.flip()