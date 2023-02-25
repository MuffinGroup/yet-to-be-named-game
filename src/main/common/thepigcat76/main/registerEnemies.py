import pygame

class enemies():
	def __init__(self, enemy_name, x, y, scale):
		image = pygame.image.load('src/main/assets/entities/enemies/' + enemy_name + '.png')
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface, player_pos):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()
		surface.blit(self.image, player_pos)
		return action	

