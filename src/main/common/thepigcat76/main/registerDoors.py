import pygame

class player():


	def __init__(self, door_number, x, y, scale):
		doorOpenSprite = pygame.image.load('src/main/assets/entities/characters/Character1/Animations/door_' + door_number + '_open.png')
		doorClosedSprite = pygame.image.load('src/main/assets/entities/characters/Character1/Animations/' + door_number + '.png')
		width = doorOpenSprite.get_width()
		height = doorOpenSprite.get_height()
		self.image = pygame.transform.scale(doorOpenSprite, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False


	def draw(self, surface, character_x, character_y):
		surface.blit(self.image, (character_x, character_y))
		
		