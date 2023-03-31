import pygame

class registerElements():
	colliding = False
	def __init__(self, elementLocation, scale):
		image = pygame.image.load("src\main/assets/textures\elements/" + elementLocation + ".png")
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

	def draw(self, surface, hitbox):
			surface.blit(self.image, (hitbox))

	def get_width(self):
		width = self.image.get_width()
		return width
	
	def get_height(self):
		heigth = self.image.get_height()
		return heigth