import pygame

pygame.init()

FONT = pygame.font.SysFont("Sans", 20)
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)

loop = True
start_time = None
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                start_time = pygame.time.get_ticks()

    screen.fill(BG_COLOR)

    if start_time:
        time_since_enter = pygame.time.get_ticks() - start_time
        message = 'Milliseconds since enter: ' + str(time_since_enter)
        screen.blit(FONT.render(message, True, TEXT_COLOR), (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()