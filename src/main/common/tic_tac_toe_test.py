import pygame
import random
import sys

pygame.init()

screen = pygame.display.set_mode((800, 800))

ttt_map = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

inputLocked = True
input = 1
gameWon = False
gameLost = False
loseTimer = 0
selectedXPos = 0
selectedYPos = 0
clock = pygame.time.Clock()

while True:
    if selectedYPos > 2:
        selectedYPos = 0
    if selectedYPos < 0:
        selectedYPos = 2
    key = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            if selectedXPos >= 2:
                selectedXPos = 0
                selectedYPos += 1
            else:
                selectedXPos += 1
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            if selectedXPos <= 0 and not selectedYPos <= 0:
                selectedXPos = 2
                selectedYPos -= 1
            elif selectedXPos == 0 and selectedYPos == 0:
                 selectedYPos = 2
                 selectedXPos = 2
            elif selectedXPos != 0:
                selectedXPos -= 1
        if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
            selectedYPos += 1
        if event.type == pygame.KEYUP and event.key == pygame.K_UP:
            selectedYPos -= 1
             
    frameX, frameY = random.randint(0, 2), random.randint(0, 2)

    y = 0
    for row in ttt_map:
        x = 0
        for tile in row:
            frame = pygame.Rect((x * 100, y * 100), (100, 100))
            try:
                if ttt_map[selectedYPos][selectedXPos] == 0 and key[pygame.K_RETURN]:
                    ttt_map[selectedYPos][selectedXPos] = 1
                    inputLocked = True
            except:
                pass
            if x == selectedXPos and y == selectedYPos:
                pygame.draw.rect(screen, (255, 0, 255), frame, 3)
            else:
                pygame.draw.rect(screen, (255, 255, 255), frame, 3)
            if tile == 1:
                pygame.draw.line(screen, (255, 0, 0), frame.bottomleft, frame.topright, 7)
                pygame.draw.line(screen, (255, 0, 0), frame.bottomright, frame.topleft, 7)
            if tile == 2:
                pygame.draw.circle(screen, (255, 0, 255), frame.center, frame.width//2, 7)

            if inputLocked == True:
                if ttt_map[frameX][frameY] == 0:
                    pygame.time.wait(200)
                    ttt_map[frameX][frameY] = 2
                    inputLocked = False

            # Check lines
            if all(cell == 1 for cell in row):
                    gameWon = True
                    print(1)

            # Check columns
            for col in range(3):
                if all(ttt_map[row][col] == 1 for row in range(3)):
                    gameWon = True
                    print(2)

            # Check diagonals
            if all(ttt_map[i][i] == 1 for i in range(3)):
                    gameWon = True
                    print(3)

            if all(ttt_map[i][2 - i] == 1 for i in range(3)):
                    gameWon = True
                    print(4)

            # Bot winning
            # Check lines
            if all(cell == 2 for cell in row):
                    gameLost = True

            # Check columns
            for col in range(3):
                if all(ttt_map[row][col] == 2 for row in range(3)):
                    gameLost = True

            # Check diagonals
            if all(ttt_map[i][i] == 2 for i in range(3)):
                    gameLost = True
            
            if all(ttt_map[i][2 - i] == 2 for i in range(3)):
                    gameLost = True
    
            if gameWon == True:
                print("Player wins!")
                pygame.quit()
                sys.exit()

            if gameLost == True:
                if loseTimer < 180:
                     loseTimer += 1
                else:
                    print("Bot wins!")
                    pygame.quit()
                    sys.exit()

            x += 1
        y += 1

    clock.tick(100)
    pygame.display.update()