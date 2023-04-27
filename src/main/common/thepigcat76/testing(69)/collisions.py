import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
player = pygame.Rect((100, 100), (100, 100))
object = pygame.Rect((500, 300), (100, 100))
object2 = pygame.Rect((800, 200), (100, 100))
rectList = [object, object2]

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if key[pygame.K_RIGHT]:
        player.x += 1
    if key[pygame.K_LEFT]:
        player.x -= 1
    if key[pygame.K_DOWN]:
        player.y += 1
    if key[pygame.K_UP]:
        player.y -= 1

    screen.fill((0,0,0))
    pygame.draw.rect(screen, (0, 255, 0), object2, 100)
    pygame.draw.rect(screen, (255, 255, 0), object, 100)
    pygame.draw.rect(screen, (255, 0, 255), player, 100)
    pygame.display.update()