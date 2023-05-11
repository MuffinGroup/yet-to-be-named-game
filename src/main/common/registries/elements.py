import pygame
import sys

class registerElement():
	def __init__(self, elementLocation, scale):
		self.scale = scale
		self.xModifier = 0
		self.yModifier = 0
		self.xRectModifier = 0
		self.yRectModifier = 0
		self.widthModifier = 0
		self.heightModifier = 0
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawElement(self, surface, x, y, rectArray):
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect)

	def drawRotatedElement(self, surface, x, y, flipped):
		if flipped == True:
			self.flippedTexture = pygame.transform.flip(self.scaledTexture, True, False)
			surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		else:
			surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))

	def drawStairElement(self, surface, x, y, flippedX, flippedY, rectArray):
		if flippedX == False and flippedY == False:
			self.flippedTexture = pygame.transform.flip(self.scaledTexture, False, False)
			self.rect1 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.scaledTexture.get_height()//2 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			self.rect2 = pygame.Rect((x * 96 + self.scaledTexture.get_width()//2 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width()//2 + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
			rectArray.append(self.rect1)
			rectArray.append(self.rect2)
		if flippedX == True and flippedY == False:
			self.flippedTexture = pygame.transform.flip(self.scaledTexture, True, False)
			self.rect1 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.scaledTexture.get_height()//2 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			self.rect2 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width()//2 + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
			rectArray.append(self.rect1)
			rectArray.append(self.rect2)
		if flippedX == False and flippedY == True:
			self.flippedTexture = pygame.transform.flip(self.scaledTexture, False, True)
			self.rect1 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			self.rect2 = pygame.Rect((x * 96 + self.scaledTexture.get_width()//2 + self.xRectModifier, y * 96 + self.scaledTexture.get_height()//2 + self.yRectModifier), (self.scaledTexture.get_width()//2 + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
			rectArray.append(self.rect1)
			rectArray.append(self.rect2)
		if flippedX == True and flippedY == True:
			self.flippedTexture = pygame.transform.flip(self.scaledTexture, True, True)
			self.rect1 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			self.rect2 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.scaledTexture.get_height()//2 + self.yRectModifier), (self.scaledTexture.get_width()//2 + self.widthModifier, self.scaledTexture.get_height()//2 + self.heightModifier))
			surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
			rectArray.append(self.rect1)
			rectArray.append(self.rect2)

	def drawPedestalElement(self, surface, x, y, rectArray):
		self.rect1 = pygame.Rect((x * 96 + self.scale * 3 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() - self.scale * 6 + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		self.rect2 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect1)

class registerAnimatedElement():
	def __init__(self, scale):
		self.scale = scale
		self.xModifier = 0
		self.yModifier = 0
		self.xRectModifier = 0
		self.yRectModifier = 0
		self.widthModifier = 0
		self.heightModifier = 0
		self.frame = 0

	def drawAnimatedElement(self, surface, x, y, rectArray, animationArray):
		if not self.frame >= len(animationArray) - 1:
			self.frame += 1
		else:
			self.frame = 0
		self.texture = animationArray[self.frame]
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * self.scale, self.texture.get_height() * self.scale))
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect)