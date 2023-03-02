import pygame

class door():

	def __init__(self, image, x, y, scale):
		doorClosedSprite = pygame.image.load(image)
		width = doorClosedSprite.get_width()
		height = doorClosedSprite.get_height()
		self.image = pygame.transform.scale(doorClosedSprite, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False

	def draw(self, surface):
		pos = pygame.mouse.get_pos()
		surface.blit(self.image, (self.rect.x, self.rect.y))
		if self.rect.collidepoint(pos):
			print("success")