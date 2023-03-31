import pygame
import registerButton
import colors

pygame.init()
screen = pygame.display.set_mode((720,720), pygame.RESIZABLE)
icon = pygame.image.load('src\main/assets/textures/elements\gui/icon\muffin_icon.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("Muffin Group")
test = registerButton.Button("toggle", 350, 450,  12.0, "", colors.BLACK, "joystixmonospaceregular")
clock = pygame.time.Clock()

while True:
    #screen.blit(img, (0, 0))
	screen.fill(colors.PURPLE)

	if test.drawToggle(screen):
		print("toggled")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit
			exit()
	pygame.display.update()
	clock.tick(60)