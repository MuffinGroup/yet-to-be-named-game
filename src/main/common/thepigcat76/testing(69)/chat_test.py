import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

user_input = ""
message_sent = ""
inputLocked = False
renderMarker = 0
defaultPos = 330
x = defaultPos

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

textfont = pygame.font.SysFont('joystixmonospaceregular', 30)

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not inputLocked == True:
            if event.key == pygame.K_BACKSPACE and not x == 330:
                user_input = user_input[0:-1]
                x -= 25
            elif event.key == pygame.K_RETURN:
                message_sent = user_input
                user_input = ""
                x = defaultPos
            elif not event.key == pygame.K_BACKSPACE:
                user_input += event.unicode
                x += 25
            
    screen.fill((0,0,0))
    user_text = textfont.render(user_input, True, (255, 255, 255))
    message_text = textfont.render(message_sent, True, (255, 255, 255))
    screen.blit(user_text, (330,310))
    screen.blit(message_text, (330,210))
    
    if renderMarker >= 99:
        renderMarker = 0
    else:
        pygame.time.wait(10)
        renderMarker += 1
    
    if renderMarker <= 60:
        pygame.draw.line(screen, (255, 255, 255), (x, 310), (x, 310 + user_text.get_height()), 5)
    clock.tick(600)
    pygame.display.update()