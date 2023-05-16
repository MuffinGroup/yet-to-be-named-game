import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
light = pygame.image.load('src\main/assets/textures\elements/test\circle.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(pygame.color.Color("Red"))
    filter = pygame.surface.Surface((640, 480))
    filter.fill(pygame.color.Color('Grey'))
    filter.blit(light, pygame.mouse.get_pos())
    screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
    pygame.display.update()