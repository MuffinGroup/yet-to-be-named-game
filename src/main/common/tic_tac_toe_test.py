import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

ttt_map = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

inputLocked = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    y = 0
    for row in ttt_map:
        x = 0
        for tile in row:
            frame = pygame.Rect((x * 100, y * 100), (100, 100))
            if tile == 0:
                if frame.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1 and inputLocked == False:
                    ttt_map[frame.y//100][frame.x//100] = 1
                    inputLocked = True
                else:
                    pygame.draw.rect(screen, (255, 255, 255), frame, 3)
            if tile == 1:
                pygame.draw.rect(screen, (255, 0, 255), frame, 3)
            if tile == 2:
                pygame.draw.rect(screen, (255, 0, 0), frame, 3)


            if inputLocked == True:
                ttt_map[random.randint(0, 2)][random.randint(0, 2)] = 2
                inputLocked = False

            x += 1
            if all(row) == 1 and not any(row) == 2:
                print("player won!")
            elif all(row) == 2:
                print("bot won!")
        y += 1

    print(ttt_map)
    pygame.display.update()