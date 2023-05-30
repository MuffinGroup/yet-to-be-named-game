from registries.elements import *

pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
grassElement = registerElement("elements/Environment/blocks/grass_dirt", 3)
dirtElement = registerElement("elements/Environment/blocks/Dirt", 3)
coarseDirtElement = registerElement("elements/Environment/blocks/Coarse_Dirt", 3)
coarseGrassElement = registerElement("elements/Environment/blocks/Coarse_Grass", 3)
selectionPos = 0
rect_array = []
checked = {"checked_0": False, "checked_1": False, "checked_2": False, "checked_3": False}

while True:
    screen.fill((0, 0, 0))
    selectionBox1 = pygame.Rect(((2 + selectionPos) * 96, 4 * 96), (96, 96))
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if selectionPos < 3:
                selectionPos += 1
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if selectionPos > 0:
                selectionPos -= 1

    dirtElement.drawElement(screen, 2, 4, rect_array)
    grassElement.drawElement(screen, 3, 4, rect_array)
    coarseDirtElement.drawElement(screen, 4, 4, rect_array)
    coarseGrassElement.drawElement(screen, 5, 4, rect_array)
    pygame.draw.rect(screen, (255, 255, 255), selectionBox1, 3)

    pygame.display.flip()