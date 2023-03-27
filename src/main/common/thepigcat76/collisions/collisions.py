import pygame

pygame.init()


screen = pygame.display.set_mode((720, 720), pygame.RESIZABLE)
image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png")
image = pygame.transform.scale(image, (int(image.get_width() * 10), int(image.get_height() * 10)))
rect = image.get_rect()
speed = 1
obstacle = pygame.Rect((400, 200, 80, 80))

while True:
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if key[pygame.K_RIGHT]:
        rect.x += speed
    if key[pygame.K_LEFT]:
        rect.x -= speed
    if key[pygame.K_UP]:
        rect.y -= speed
    if key[pygame.K_DOWN]:
        rect.y += speed
    screen.fill((255, 255, 255))
    screen.blit(image, rect)
    pygame.draw.rect(screen, (255, 0, 0), rect, 4)
    if rect.colliderect(obstacle):
        pygame.draw.rect(screen, (0, 255, 0), rect, 4)

    pygame.draw.rect(screen, (0,0,0), obstacle, 4)
    pygame.display.flip()