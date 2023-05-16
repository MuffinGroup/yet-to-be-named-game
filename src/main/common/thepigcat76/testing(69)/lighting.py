import pygame
pygame.init()
screen=pygame.display.set_mode((640, 480))
light=pygame.image.load('src\main/assets/textures\elements/test\circle.png')
while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: break
    else:
        screen.fill(pygame.color.Color('Red'))
        for x in range(0, 640, 20):
            pygame.draw.line(screen, pygame.color.Color('Green'), (x, 0), (x, 480), 3)
        filter = pygame.surface.Surface((640, 480))
        filter.fill(pygame.color.Color('Grey'))
        filter.blit(light, pygame.mouse.get_pos())
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        pygame.display.flip()
        continue
    break