import pygame

# Initialize Pygame
pygame.init()

user_input = ""

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

textfont = pygame.font.SysFont('joystixmonospaceregular', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            user_input += event.unicode
            
    text = textfont.render(user_input, True, (255, 255, 255))
    screen.blit(text, (330,310))
    pygame.display.update()