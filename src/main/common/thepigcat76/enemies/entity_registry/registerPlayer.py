import pygame

class player():
	def __init__(self, player_name, x, y, scale, jumpsound_name, jumpsound_volume):
		image = pygame.image.load('src/main/assets/characters/Character1/Animations/' + player_name + '.png')
		jumpsound = pygame.mixer.Sound("src/main/assets/sounds/" + jumpsound_name +".wav")
		jumpsound.set_volume(jumpsound_volume) #Maximum is 1
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		#Will be executred during the while loop
		action = False
		pos = pygame.mouse.get_pos()
		surface.blit(self.image, (self.rect.x, self.rect.y))
		keys = pygame.key.get_pressed()
		Player = pygame.Rect(character_x, character_y, 40, 80)

		if keys[pygame.K_LEFT, pygame.K_s] and not Player.colliderect(leftWall):
			character_x -= character_speed
		if keys[pygame.K_RIGHT, pygame.K_w] and not Player.colliderect(rightWall):
			character_x += character_speed
		if keys[pygame.K_UP, pygame.K_SPACE] and jumpvar == -16:
			jumpvar = 15
		
		if jumpvar == 15:
			pygame.mixer.Sound.play(jumpsound)