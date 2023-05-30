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
		self.item = None
		self.hasItem = False
		self.texture = pygame.image.load("src/main/assets/textures/" + elementLocation + ".png")
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * scale, self.texture.get_height() * scale))

	def drawElement(self, surface, x, y, rectArray):
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect)

	def drawYOffsetElement(self, surface, x, y, rectArray, offset):
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier + offset), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier + offset))
		rectArray.append(self.rect)

	def drawRotatedElement(self, surface, x, y, flippedX, flippedY):
		self.flippedTexture = pygame.transform.flip(self.scaledTexture, flippedX, flippedY)
		surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))

	def drawPrecRotatedElement(self, surface, x, y, rectArray, rotationAngle):
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		self.flippedTexture = pygame.transform.rotate(self.scaledTexture, rotationAngle)
		surface.blit(self.flippedTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect)

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

	def drawDedicatedPedestalElement(self, surface, x, y, rectArray, player, acceptedItem):
		self.acceptedItem = acceptedItem
		self.rect1 = pygame.Rect((x * 96 + self.scale * 3 + self.xRectModifier, y * 96 + self.scale * 6 + self.yRectModifier), (self.scaledTexture.get_width() - self.scale * 6 + self.widthModifier, (self.scaledTexture.get_height() - self.scale * 6) + self.heightModifier))
		self.rect2 = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect1)
		if player.rect.colliderect(self.rect2) and player.holding != None and pygame.key.get_pressed()[pygame.K_e]:
			self.hasItem = True
		if self.hasItem == True:
			self.item = player.holding
			player.holding.pickedUp = False
			player.holding.yNewNew, player.holding.xNewNew = self.rect1.y - 24, self.rect1.x + self.rect1.width//2 - player.holding.hitbox.width//2
			if self.item == acceptedItem:
				return True
			else:
				return False
			
		if player.holding == None and self.hasItem == True:
			if player.rect.colliderect(self.rect2) and pygame.key.get_pressed()[pygame.K_e]:
				self.hasItem = False
				player.holding = self.item
				self.item.pickedUp = True
				self.item.xNewNew, self.item.yNewNew = 0, 0

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

class registerInvisibleElement():
	def __init__(self):
		self.xModifier = 0
		self.yModifier = 0
		self.xRectModifier = 0
		self.yRectModifier = 0
		self.widthModifier = 0
		self.heightModifier = 0

	def drawElement(self, x, y, rectArray):
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (96 + self.widthModifier, 96 + self.heightModifier))
		rectArray.append(self.rect)

class registerCallableAnimatedElement():
	def __init__(self, scale):
		self.scale = scale
		self.xModifier = 0
		self.yModifier = 0
		self.xRectModifier = 0
		self.yRectModifier = 0
		self.widthModifier = 0
		self.heightModifier = 0
		self.frame = 0

	def drawCallableAnimatedElement(self, surface, x, y, rectArray, animationArray):
		self.texture = animationArray[self.frame]
		self.animationArray = animationArray
		self.scaledTexture = pygame.transform.scale(self.texture, (self.texture.get_width() * self.scale, self.texture.get_height() * self.scale))
		self.rect = pygame.Rect((x * 96 + self.xRectModifier, y * 96 + self.yRectModifier), (self.scaledTexture.get_width() + self.widthModifier, self.scaledTexture.get_height() + self.heightModifier))
		surface.blit(self.scaledTexture, (x * 96 + self.xModifier, y * 96 + self.yModifier))
		rectArray.append(self.rect)

	def callAnimation(self):
		if not self.frame >= len(self.animationArray) - 1:
			self.frame += 1
		else:
			self.frame = len(self.animationArray) - 1

	def callEndlessAnimation(self):
		if not self.frame >= len(self.animationArray) - 1:
			self.frame += 1
		else:
			self.frame = 0

	def callResetAnimation(self):
		self.frame = 0