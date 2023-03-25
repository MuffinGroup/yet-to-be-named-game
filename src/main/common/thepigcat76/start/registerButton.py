import pygame
import animations

#button class

class Button():
	clock = pygame.time.Clock()
	def __init__(self, button_name, x, y, scale, display_text, text_color, font_type):
		image = pygame.image.load('src//main//assets//textures//elements//gui//' + button_name + '.png')
		self.value = 0
		selected_image = pygame.image.load('src//main//assets//textures//elements//gui//' + button_name + '_selected.png')
		width = image.get_width()
		height = image.get_height()
		smallfont = pygame.font.SysFont(font_type,35)
		self.selected_image = pygame.transform.scale(selected_image, (int(width * scale), int(height * scale)))
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.display_text = smallfont.render(display_text , True , text_color)
		self.selected_display_text1 = smallfont.render(display_text , True , (56, 56, 56))
		self.selected_display_text2 = smallfont.render(display_text , True , (80, 80, 80))
		self.selected_display_text3 = smallfont.render(display_text , True , (171, 171, 171))
		self.selected_display_text4 = smallfont.render(display_text , True , (255, 255, 255))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)
		self.clicked = False
		self.selected = False

	def draw(self, surface, xTextOffset, yTextOffset):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if not self.rect.collidepoint(pos):
			surface.blit(self.image, (self.rect.x, self.rect.y))
			surface.blit(self.display_text , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
		elif self.rect.collidepoint(pos):
			surface.blit(self.selected_image, (self.rect.x, self.rect.y))
			surface.blit(self.selected_display_text4 , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action
	
	def drawAnimated(self, surface, animationArray, xOffset, yOffset, scale):
		action = False
		pos = pygame.mouse.get_pos()
		image = animationArray[self.value]
		width = image.get_width()
		height = image.get_height()
		buttonSprite = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

		if self.value >= 31 and self.selected == True:
			self.value = 30
		elif self.selected == False:
			self.value = 0
		
		if not self.rect.collidepoint(pos):
			surface.blit(self.image, (self.rect.x, self.rect.y))
			surface.blit(self.display_text , (self.rect.x + 125, self.rect.y + 25))
			self.selected = False 
		else:
			self.selected = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if self.selected == True and self.value < 31:
			self.value += 1

		if self.selected == True:
			surface.blit(buttonSprite, (self.rect.x - xOffset, self.rect.y - yOffset))

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	clock.tick(60)