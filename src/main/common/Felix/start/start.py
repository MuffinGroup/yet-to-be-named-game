import pygame

pygame.init
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
img = pygame.image.load('yet-to-be-named-game\src\main\common\Felix\start\icon.png')
pygame.display.set_icon(img)
Spieler1 = pygame.image.load('yet-to-be-named-game\src\main//assets\characters\Character1\Character1.png')

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed succesful")
                pygame.quit
                exit()
        pygame.display.update()
        clock.tick(60)