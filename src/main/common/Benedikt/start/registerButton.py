import pygame

#button class
class Button():
	def __init__(self, x, y, image, selected_image, scale):
		width = image.get_width()
		height = image.get_height()
		self.selected_image = pygame.transform.scale(selected_image, (int(width + scale), int(height * scale)))
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if not self.rect.collidepoint(pos):
			surface.blit(self.image, (self.rect.x, self.rect.y))
		elif self.rect.collidepoint(pos):
			surface.blit(self.selected_image, (self.rect.x, self.rect.y))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen

		return action