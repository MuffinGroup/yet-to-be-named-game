import pygame

pygame.init
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("test")
clock = pygame.time.Clock()
img = pygame.image.load('src//main//assets//icon//icon.png')
pygame.display.set_icon(img)

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Closed succesful")
                pygame.quit
                exit()
        #screen.blit(img, (0, 0))
        screen.fill((255,255,255))
        pygame.display.update()
        clock.tick(60)