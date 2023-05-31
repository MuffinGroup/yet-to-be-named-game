from registries.elements import *

pygame.init()
screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
grassElement = registerElement("elements/Environment/blocks/grass_dirt", 3)
dirtElement = registerElement("elements/Environment/blocks/Dirt", 3)
coarseDirtElement = registerElement("elements/Environment/blocks/Coarse_Dirt", 3)
coarseGrassElement = registerElement("elements/Environment/blocks/Coarse_Grass", 3)
selectionPos = 0
checked1, checked2 = None, None
rect_array = []
selectedPedestal1, selectedPedestal2 = None, None
pedestals = [1, 2, 3, 4]

while True:
    checked = [checked1, checked2]
    screen.fill((0, 0, 0))
    selectionBox1 = pygame.Rect(((2 + selectionPos) * 96, 2 * 96), (96, 96))
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
        if event.type == pygame.KEYUP and event.key == pygame.K_RETURN:
            if checked1 == None:
                checked1 = selectionPos
            elif checked1 != selectionPos:
                checked2 = selectionPos
    
    if checked1 != None and checked2 != None:
        try:
            pedestals[checked1], pedestals[checked2] = pedestals[checked2], pedestals[checked1]
        except:
            pass
        checked1, checked2 = None, None

    if pedestals == [4, 3, 2, 1]:
        exit()

    x = 0
    for tile in pedestals:
        if tile == 1:
            grassElement.drawElement(screen, x + 2, 2, rect_array)
        if tile == 2:
            dirtElement.drawElement(screen, x + 2, 2, rect_array)
        if tile == 3:
            coarseGrassElement.drawElement(screen, x + 2, 2, rect_array)
        if tile == 4:
            coarseDirtElement.drawElement(screen, x + 2, 2, rect_array)
        x += 1

    pygame.draw.rect(screen, (255, 255, 255), selectionBox1, 3)
    print(checked)
    
    pygame.display.flip()