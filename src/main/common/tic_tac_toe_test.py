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
                pygame.draw.rect(screen, (255, 255, 255), frame, 3)
            if frame.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, (111, 0, 69), frame, 3)
            if tile == 1:
                pygame.draw.rect(screen, (0, 0, 255), frame, 3)
            if tile == 2:
                pygame.draw.rect(screen, (255, 0, 0), frame, 3)
            if frame.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0] == 1:
                ttt_map[frame.y//100][frame.x//100] = 1
            if all(cell == 1 for cell in row):
                print("player won!")
            for col in range(3):
                if all(ttt_map[row][col] == 1 for row in range(3)):
                    print("player won!")

            # Check diagonals
            if all(ttt_map[i][i] == 1 for i in range(3)):
                print("player won!")
            if all(ttt_map[i][2 - i] == 1 for i in range(3)):
                print("player won!")      
            x += 1
        y += 1

    print(ttt_map)
    pygame.display.update()