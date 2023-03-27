import pygame

#button class

class registerElements():
	def __init__(self, elementLocation, x, y, scale):
		image = pygame.image.load("src\main/assets/textures\elements/" + elementLocation + ".png")
		width = image.get_width()
		height = image.get_height()
		registerElements.colliding = False
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = pygame.Rect((x, y),(int(width * scale), int(height * scale)))

	def draw(self, surface, player):
			surface.blit(self.image, (self.rect.x, self.rect.y))
			if player.colliderect(self.rect):
				registerElements.colliding = True
			else:
				registerElements.colliding = False