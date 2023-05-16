import sys

import pygame

try:
    import item  # pyright: ignore
except ImportError:
    print("Local import needs fixing")
    sys.exit(1)

pygame.init()

player = pygame.Rect((300, 400), (100, 100))
slots = []
for i in range(4):
    print(i)
    slots.append(pygame.Rect((78 * i + 50, 50), (80, 80)))
    print(len(slots))
test = item.registerItem("test", "Test", "Environment/Blocks/wooden_sign")

screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
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
    if key[pygame.K_UP]:
        player.y -= 1
    if key[pygame.K_DOWN]:
        player.y += 1
    # Das hier ist der 1000ste commit. Checkt das Video hier ab: https://www.youtube.com/watch?v=dQw4w9WgXcQ

    screen.fill((255, 255, 255))
    test.drawItem(screen)
    pygame.draw.rect(screen, (255, 0, 255), player, 1000)

    for i in range(len(slots)):
        pygame.draw.rect(screen, (0, 0, 0), slots[i], 5)

    pygame.display.flip()
