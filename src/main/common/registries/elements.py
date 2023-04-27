import pygame

class registerElement():
	def __init__(self, elementLocation, scale):
		self.scale = scale
		self.xModifier = 0
		self.yModifier = 0
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawElement(self, surface, x, y, debuggingmode):
		self.rect = pygame.Rect((x * 96, y * 96), (self.scaledTexture.get_width(), self.scaledTexture.get_height()))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		if debuggingmode == True:
			pygame.draw.rect(surface, (255, 255, 255), self.rect, 3)