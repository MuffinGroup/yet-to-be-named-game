import pygame


def game():
    screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
    player = pygame.Rect(100, 500, 100, 100)
    # NOTE: refactored object to object_ because object is a reserved keyword in python
    object_ = pygame.Rect((1400, 600), (100, 100))
    x = -16
    modifier = 1

    while True:
        clock = pygame.time.Clock()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if keys[pygame.K_RIGHT]:
            player.x += 1
        if keys[pygame.K_LEFT]:
            player.x -= 1
        if keys[pygame.K_UP]:
            player.y -= 1
        if keys[pygame.K_DOWN]:
            player.y += 1
        if keys[pygame.K_0] and x == -16:
            x = 15

        if x == 15:
            object_.y -= 3 * 1.1 * modifier
            object_.x -= 12
            if object_.x < 650:
                modifier = -1
            if object_.x <= 100:
                object_.x = 100
                object_.y = 500

        screen.fill((90, 90, 90))
        pygame.draw.rect(screen, (255, 255, 255), player, 1000)
        pygame.draw.rect(screen, (255, 0, 255), object_, 500)
        pygame.display.flip()
        clock.tick(600)


game()
