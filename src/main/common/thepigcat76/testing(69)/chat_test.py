import pygame

# Initialize Pygame
pygame.init()

user_input = ""
inputLocked = False

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
        if event.type == pygame.KEYDOWN and not inputLocked == True:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[0:-1]
            elif event.key == pygame.K_RETURN:
                inputLocked = True
            else:
                user_input += event.unicode
            
    screen.fill((0,0,0))
    text = textfont.render(user_input, True, (255, 255, 255))
    screen.blit(text, (330,310))
    pygame.display.update()