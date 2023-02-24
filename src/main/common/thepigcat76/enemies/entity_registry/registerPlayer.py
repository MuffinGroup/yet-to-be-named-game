import pygame

class player():


	def __init__(self, image, x, y, scale):
		right_image = pygame.transform.flip(image, True, False)
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False


	def draw(self, surface, character_x, character_y):
		surface.blit(self.image, (character_x, character_y))
		
		