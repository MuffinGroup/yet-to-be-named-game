import pygame

class player():
	def __init__(self, player_name, x, y, scale):
		image = pygame.image.load('src/main/assets/characters/Character1/Animations/' + player_name + '.png')
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface, character_x, character_y, character_speed, jumpsound):
		surface.blit(self.image, (character_x, character_y))
		keys = pygame.key.get_pressed()
		Spieler = pygame.Rect(character_x, character_y, 40, 80)
		jumpvar = -16
		
		if keys[pygame.K_LEFT]:
			character_x -= character_speed	
		if keys[pygame.K_RIGHT]:
			character_x += character_speed
		if keys[pygame.K_UP] and jumpvar == -16:
			jumpvar = 15

		if jumpvar == 15:
			pygame.mixer.Sound.play(jumpsound)

		if jumpvar >= -15:
			n = 1
			if jumpvar < 0:
				n = -1
			character_y -= (jumpvar**2)*0.17*n
			jumpvar -= 1

