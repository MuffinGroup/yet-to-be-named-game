import pygame

class registerElement():
	def __init__(self, elementLocation, scale):
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawElement(self, surface, x, y, debuggingmode):
		self.rect = pygame.Rect((x * self.scaledTexture.get_width(), y * self.scaledTexture.get_height()), (self.scaledTexture.get_width(), self.scaledTexture.get_height()))
		surface.blit(self.scaledTexture, (x * self.scaledTexture.get_width(), y * self.scaledTexture.get_height()))
		if debuggingmode == True:
			pygame.draw.rect(surface, (255, 255, 255), self.rect, 3)

class registerLargeElement():
	def __init__(self, elementLocation, scale):
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawLargeElement(self, surface, x, y, debuggingmode):
		self.rect = pygame.Rect((x * self.scaledTexture.get_width(), y * self.scaledTexture.get_height()), (self.scaledTexture.get_width(), self.scaledTexture.get_height()))
		surface.blit(self.scaledTexture, (x * self.scaledTexture.get_width(), y * self.scaledTexture.get_height()))
		if debuggingmode == True:
			pygame.draw.rect(surface, (255, 255, 255), self.rect, 3)