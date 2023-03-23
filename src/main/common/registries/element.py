import pygame
import element

#button class

class registerElements():
	def __init__(self, elementLocation, x, y, scale):
		image = pygame.image.load("src\main/assets/textures\elements/" + elementLocation + ".png")
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def draw(self, surface):
			surface.blit(self.image, (self.rect.x, self.rect.y))

class testing():
	element = element.registerElements("environment/blocks/wooden_sign", 500, 500, 10)
	screen = pygame.display.set_mode((720, 720))
	running = True
	while running:
		element.draw(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit
				running = False
		pygame.display.flip()