import pygame

#button class

class registerElements():
	def __init__(self, elementLocation, x, y, scale):
		image = pygame.image.load("src\main/assets/textures\elements/" + elementLocation + ".png")
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = pygame.Rect((x, y),(self.image.get_width(), self.image.get_height()))

	def draw(self, surface, player):
			surface.blit(self.image, (self.rect.x, self.rect.y))
			if player.colliderect(self.rect):
				print("e")