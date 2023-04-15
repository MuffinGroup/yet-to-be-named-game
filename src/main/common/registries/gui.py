import pygame

pygame.init()
class registerGui():
    def __init__(self, x, y, width, height, backgroundImage, imagePath):
        if backgroundImage == True:
            self.bgImage = pygame.image.load("src/main/assets/textures/elements/background/" + imagePath + ".png")
            self.backgroundImage = True
        else:
            self.backgroundImage = False
        self.window = pygame.Surface((width, height))
        self.x, self.y = x,y
        
    def draw(self, surface, color=None):
        surface.blit(self.window, (self.x, self.y))
        if color == None:
            self.window.fill((0, 0, 0))
        else:
            self.window.fill(color)
        if self.backgroundImage == True:
            self.window.blit(self.bgImage, (0, 0))

class registerObject():
    def __init__(self, x, y, width, height, color, borderWidth):
        self.color = color
        self.width = width
        self.height = height
        self.borderWidth = borderWidth
        self.rect = pygame.Rect(x, y, width, height)

    def drawObject(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, self.borderWidth)

class registerButton():
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
		self.toggled = False
		self.selected = False
		self.test = 0

	#draw function is not used atm 
	def draw(self, surface, xTextOffset, yTextOffset, xTextureOffset, yTextureOffset):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		surface.blit(self.image, (self.rect.x - xTextureOffset, self.rect.y - yTextureOffset))
		if not self.rect.collidepoint(pos):
			surface.blit(self.display_text , (self.rect.x - xTextOffset - xTextureOffset, self.rect.y - yTextOffset - yTextureOffset))
		elif self.rect.collidepoint(pos):
			pygame.draw.rect(surface, (255, 255, 255), (self.rect.x - xTextureOffset, self.rect.y - yTextureOffset, self.rect.width, self.rect.height), 5)
			surface.blit(self.selected_display_text4 , (self.rect.x - xTextOffset - xTextureOffset, self.rect.y - yTextOffset - yTextureOffset))
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
		

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action
	
	def drawAnimated(self, surface, animationArray, xOffset, yOffset, scale, xTextOffset, yTextOffset, xTextureOffset, yTextureOffset):
		action = False
		pos = pygame.mouse.get_pos()
		image = animationArray[self.value]
		width = image.get_width()
		height = image.get_height()
		buttonSprite = pygame.transform.scale(image, (int(width * scale), int(height * scale)))

		if self.value >= len(animationArray) - 1 and self.selected == True:
			self.value = len(animationArray) - 2
		elif self.selected == False:
			self.value = 0
		
		if not self.rect.collidepoint(pos):
			surface.blit(self.image, (self.rect.x, self.rect.y))
			surface.blit(self.display_text , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
			self.selected = False 
		else:
			self.selected = True
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True
				print("mouse collides")

		if self.selected == True and self.value < len(animationArray) - 1:
			self.value += 1

		if self.selected == True:
			surface.blit(buttonSprite, (self.rect.x - xOffset, self.rect.y - yOffset))

		if self.value < len(animationArray)/4 * 1:
			surface.blit(self.selected_display_text1 , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
		elif self.value < len(animationArray)/4 * 2:
			surface.blit(self.selected_display_text2 , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
		elif self.value < len(animationArray)/4 * 3:
			surface.blit(self.selected_display_text3 , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))
		elif self.value > len(animationArray)/4 * 3:
			surface.blit(self.selected_display_text4 , (self.rect.x - xTextOffset, self.rect.y - yTextOffset))

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		return action

	def drawToggle(self, surface, xTextureOffset, yTextureOffset):
		action = False
		pos = pygame.mouse.get_pos()

		if self.toggled == False or self.test == 0:
			surface.blit(self.image, (self.rect.x - xTextureOffset, self.rect.y - yTextureOffset))
			self.selected = False
		if self.toggled == True and self.test == 1:
			surface.blit(self.selected_image, (self.rect.x - xTextureOffset, self.rect.y - yTextureOffset))
			self.selected = True
		if self.toggled == True and self.test > 1:
			surface.blit(self.image, (self.rect.x, self.rect.y))
			self.test = 0
			self.selected = False

		if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.rect.collidepoint(pos):
			self.test += 1
			self.toggled = True
			action = True
			pygame.time.wait(100)

		if self.rect.collidepoint(pos):
			pygame.draw.rect(surface, (255, 255, 255), (self.rect.x - xTextureOffset, self.rect.y - yTextureOffset, self.rect.width, self.rect.height), 4)

		return action

	clock.tick(60)
 
class registerFont():
    def __init__(self, fontSize, displayText, color):
        self.font = pygame.font.Font("src\main/assets/fonts/joystixmonospaceregular.otf", fontSize)
        self.displayText = displayText
        self.color = color
        
    def drawFont(self, surface, x, y):
        self.text = self.font.render(self.displayText, True, self.color)
        surface.blit(self.text, (x, y))
    
class registerImages():
	def __init__(self, imagePath):
		self.image = pygame.image.load("src/main/assets/textures/" + imagePath + ".png")
	
	def drawImage(self, surface, x, y):
		surface.blit(self.image, (x, y))
  
class registerChat():
    def __init__(self, lines, fontSize, textColor, frameColor, chatBoxColor, markerDefaultPos, frameX, frameY, frameWidth, frameHeight, chatBoxX, chatBoxY, chatBoxWidth, chatBoxHeight):
        self.linesLoaded = []
        self.userInput = ""
        self.sample = "i"
        self.inputLocked = False
        self.selected = True
        self.frame = pygame.Rect((frameX, frameY), (frameWidth, frameHeight))
        self.chatBox = pygame.Rect((chatBoxX, chatBoxY), (chatBoxWidth, chatBoxHeight))
        self.font = pygame.font.Font("src\main/assets/fonts/joystixmonospaceregular.otf", fontSize)
        self.textColor = textColor
        self.frameColor = frameColor
        self.chatBoxColor = chatBoxColor
        self.renderMarker = 0
        self.lessThanOneChar = True
        self.markerDefaultPos = markerDefaultPos
        self.x = self.markerDefaultPos
        self.lines = lines
        self.sentMessage = False
        for i in range(lines + 1):
            self.line = ""
            self.linesLoaded.append(self.line)
    
    def event(self, event): #this has to be executed withing the event for loop look at main_gui for an example
        if event.type == pygame.KEYDOWN and self.inputLocked == False:
            if event.key == pygame.K_BACKSPACE and self.lessThanOneChar == False:
                self.userInput = self.userInput[0:-1]
                self.x -= self.sampleText.get_width()
            elif event.key == pygame.K_TAB and self.userText.get_width() < self.chatBox.width - self.sampleText.get_width() * 4:
                self.userInput += "    "
                self.x += self.sampleText.get_width() * 4
            elif not event.key == pygame.K_BACKSPACE and not event.key == pygame.K_LALT and not event.key == pygame.K_RALT and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT and not event.key == pygame.K_UP and not event.key == pygame.K_DOWN and not event.key == pygame.K_LCTRL and not event.key == pygame.K_RCTRL and not event.key == pygame.K_RSHIFT and not event.key == pygame.K_RETURN and self.userText.get_width() < self.chatBox.width - self.sampleText.get_width() * 4:
                self.userInput += event.unicode
                self.x += self.sampleText.get_width()
                
            if event.key == pygame.K_RETURN and self.lessThanOneChar == False:
                for i in range(self.lines): #len in main_gui is 3
                        self.linesLoaded[self.lines - i] = self.linesLoaded[self.lines - i - 1]
                self.linesLoaded[0] = self.userInput
                self.userInput = ""
                self.x = self.markerDefaultPos
                self.sentMessage = True
            else:
                self.sentMessage = False
            
    def drawChat(self, surface):
        self.sampleText = self.font.render(self.sample, False, (0, 0, 0))
        self.userText = self.font.render(self.userInput, True, self.textColor)
        
        for i in range(self.lines):
            self.message_text = self.font.render(self.linesLoaded[i], True, self.textColor)
            surface.blit(self.message_text, (self.markerDefaultPos, self.chatBox.y - 75 - 75 * i))
            
        surface.blit(self.userText, (330 ,600))
        pygame.draw.rect(surface, self.frameColor, self.frame, 5)
        pygame.draw.rect(surface, self.chatBoxColor, self.chatBox, 5)
        
        if self.userText.get_width() >= self.sampleText.get_width():
            self.lessThanOneChar = False
        else:
            self.lessThanOneChar = True
            
        if self.renderMarker >= 99:
            self.renderMarker = 0
        else:
            pygame.time.wait(10)
            self.renderMarker += 1
            
        if self.renderMarker <= 60 and self.inputLocked == False:
            pygame.draw.line(surface, (255, 255, 255), (self.x, 600), (self.x, 600 + self.userText.get_height()), 5)
        print(len(self.linesLoaded))
 