import pygame

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()

message_sent8 = ""
message_sent7 = ""
message_sent6 = ""
message_sent5 = ""
message_sent4 = ""
message_sent3 = ""
message_sent2 = ""
message_sent1 = ""
message_sent = ""
user_input = ""
sample = "i"
inputLocked = False
renderMarker = 0
defaultPos = 330
lessThanOneChar = True
x = defaultPos
selected = True
frame = pygame.Rect(270, 100, 800, 600)
chat_box = pygame.Rect(300, 575, 735, 100)

#Load background
background = pygame.image.load("src\main/assets/textures\elements/background\placeholder_background_1.jpg")

# Create a screen surface
screen = pygame.display.set_mode((1280, 800), pygame.RESIZABLE)

textfont = pygame.font.Font("src\main/assets/fonts/joystixmonospaceregular.otf", 30)

while True:
    key = pygame.key.get_pressed()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN and not inputLocked == True:
            if event.key == pygame.K_BACKSPACE and lessThanOneChar == False:
                user_input = user_input[0:-1]
                x -= sample_text.get_width()
            elif event.key == pygame.K_TAB and user_text.get_width() < chat_box.width - sample_text.get_width() * 4:
                user_input += "    "
                x += sample_text.get_width() * 4
            elif not event.key == pygame.K_BACKSPACE and not event.key == pygame.K_LALT and not event.key == pygame.K_RALT and not event.key == pygame.K_LSHIFT and not event.key == pygame.K_RIGHT and not event.key == pygame.K_LEFT and not event.key == pygame.K_UP and not event.key == pygame.K_DOWN and not event.key == pygame.K_LCTRL and not event.key == pygame.K_RCTRL and not event.key == pygame.K_RSHIFT and not event.key == pygame.K_RETURN and user_text.get_width() < chat_box.width - sample_text.get_width() * 4:
                user_input += event.unicode
                x += sample_text.get_width()
            if event.key == pygame.K_RETURN and lessThanOneChar == False:
                print("ew")
                message_sent8 = message_sent7
                message_sent7 = message_sent6
                message_sent6 = message_sent5
                message_sent5 = message_sent4
                message_sent4 = message_sent3
                message_sent3 = message_sent2
                message_sent2 = message_sent1
                message_sent1 = message_sent
                message_sent = user_input
                user_input = ""
                x = defaultPos
                
        #Very obvious easter eggs
        if message_sent == "/joke":
            message_sent = "ReadyPlayerOne14"
        elif message_sent == "css":
            message_sent = "not so god stuff stop it!"
            
    screen.fill((0,0,0))
    sample_text = textfont.render(sample, False, (0, 0, 0))
    user_text = textfont.render(user_input, True, (255, 255, 255))
    message_text = textfont.render(message_sent, True, (255, 255, 255))
    message_text1 = textfont.render(message_sent1, True, (255, 255, 255))
    message_text2 = textfont.render(message_sent2, True, (255, 255, 255))
    message_text3 = textfont.render(message_sent3, True, (255, 255, 255))
    message_text4 = textfont.render(message_sent4, True, (255, 255, 255))
    message_text5 = textfont.render(message_sent5, True, (255, 255, 255))
    message_text6 = textfont.render(message_sent6, True, (255, 255, 255))
    message_text7 = textfont.render(message_sent7, True, (255, 255, 255))
    message_text8 = textfont.render(message_sent8, True, (255, 255, 255))
    screen.blit(user_text, (330 ,600))
    screen.blit(message_text8, (330, 100))
    screen.blit(message_text7, (330, 150))
    screen.blit(message_text6, (330, 200))
    screen.blit(message_text5, (330, 250))
    screen.blit(message_text4, (330, 300))
    screen.blit(message_text3, (330, 350))
    screen.blit(message_text2, (330, 400))
    screen.blit(message_text1, (330, 450))
    screen.blit(message_text, (330, 500))
    pygame.draw.rect(screen, (255, 255, 255), frame, 5)
    pygame.draw.rect(screen, (255, 255, 255), chat_box, 5)
    
    if user_text.get_width() >= sample_text.get_width():
        lessThanOneChar = False
    else: 
        lessThanOneChar = True
        
    if selected == False:
        inputLocked = True
    else:
        inputLocked = False
    
    if renderMarker >= 99:
        renderMarker = 0
    else:
        pygame.time.wait(10)
        renderMarker += 1
    
    if renderMarker <= 60 and inputLocked == False:
        pygame.draw.line(screen, (255, 255, 255), (x, 600), (x, 600 + user_text.get_height()), 5)
    clock.tick(600)
    pygame.display.update()