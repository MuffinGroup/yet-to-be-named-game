import pygame

class registerElements():
	def __init__(self, elementLocation, scale):
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawElement(self, x, y):
		self.rect = pygame.Rect((x * self.scaledTexture.get_width()), (y * self.scaledTexture.get_height()),(self.scaledTexture.get_width(), self.scaledTexture.get_height()))