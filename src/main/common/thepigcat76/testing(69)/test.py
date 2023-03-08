import pygame

pygame.init

screen = pygame.display.set_mode((100, 100), pygame.RESIZABLE)

background = pygame.image.load("src/main/assets/elements/background/hallway.jpg")
    
screen.blit(background, (0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update