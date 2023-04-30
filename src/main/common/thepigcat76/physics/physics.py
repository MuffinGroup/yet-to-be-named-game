import pygame

screen = pygame.display.set_mode((800,800), pygame.RESIZABLE)
player = pygame.Rect(100, 500, 100, 100)
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
	
	if keys[pygame.K_UP] and x == 12: #Jumping
		if modifier < 9.5: #Jump modifier cap
			modifier += 0.05
		print(modifier)
		jumped = True
	elif modifier != 1 and not x == -10.3 and jumped == True:
		x = -10.3
		print(player.y)
		jumped = False
	elif x == 12:
		modifier = 1
	
	if x <= 11: #Jumping movement
		n = -1
		if x < 0:
			n = 1
		player.y -= (x**2)*0.17*n*modifier
		jumping = True
		x += 1
	else:
		x = 12
		jumping = False
    
	screen.fill((90, 90, 90))
	pygame.draw.rect(screen, (255, 255, 255), player, 1000)
	pygame.display.flip()
	clock.tick(60)