import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 800))

ttt_map = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

inputLocked = False
input = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    frameX, frameY = random.randint(0, 2), random.randint(0, 2)

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
                if ttt_map[frameX][frameY]:
                    ttt_map[frameX][frameY] = 2
                    inputLocked = False
                    
            # Check diagonals
            if all(ttt_map[i][i] == 1 for i in range(3)):
                print("player won!")
            if all(ttt_map[i][2 - i] == 1 for i in range(3)):
                print("player won!")
            x += 1
        y += 1

    print(inputLocked)
    pygame.display.update()