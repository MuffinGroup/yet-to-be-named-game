from pygame.locals import *
import pygame
import sys
import random
import time
import os
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('outline test')
WINDOWWIDTH = 500
WINDOWHEIGHT = 300
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
display = pygame.Surface((250, 150))

test_img = pygame.image.load('src\main/assets/textures\elements\Environment\decoration\poppy.png').convert()
test_img.set_colorkey((0, 0, 0))
# text_img = pygame.image.load('text.png').convert()
# text_img.set_colorkey((0,0,0))

# method 1


def outline_mask(img, loc):
    mask = pygame.mask.from_surface(img)
    mask_outline = mask.outline()
    n = 0
    for point in mask_outline:
        mask_outline[n] = (point[0] + loc[0], point[1] + loc[1])
        n += 1
    pygame.draw.polygon(display, (255, 255, 255), mask_outline, 3)

# method 2


def perfect_outline(img, loc):
    mask = pygame.mask.from_surface(img)
    mask_surf = mask.to_surface()
    mask_surf.set_colorkey((0, 0, 0))
    display.blit(mask_surf, (loc[0]-1, loc[1]))
    display.blit(mask_surf, (loc[0]+1, loc[1]))
    display.blit(mask_surf, (loc[0], loc[1]-1))
    display.blit(mask_surf, (loc[0], loc[1]+1))

# method 3


def perfect_outline_2(img, loc):
    mask = pygame.mask.from_surface(img)
    mask_outline = mask.outline()
    mask_surf = pygame.Surface(img.get_size())
    for pixel in mask_outline:
        mask_surf.set_at(pixel, (255, 255, 255))
    mask_surf.set_colorkey((0, 0, 0))
    display.blit(mask_surf, (loc[0]-1, loc[1]))
    display.blit(mask_surf, (loc[0]+1, loc[1]))
    display.blit(mask_surf, (loc[0], loc[1]-1))
    display.blit(mask_surf, (loc[0], loc[1]+1))


show = False
mode = 0

# Loop ------------------------------------------------------- #
while True:
    # Background --------------------------------------------- #
    display.fill((255,0,255))
    pygame.draw.rect(display, (255, 255, 255), pygame.Rect(0, 0, 250, 150), 1)
    # display.blit(text_img,(10,70))
    if mode == 0:
        outline_mask(test_img, (10, 10))
    elif mode == 1:
        pass
        # perfect_outline(test_img,(100,10))
        # this line can be added back in (remove the pass too) if Pygame 2 is being used
    else:
        perfect_outline_2(test_img, (190, 10))
    if show:
        display.blit(test_img, (10, 10))
        display.blit(test_img, (100, 10))
        display.blit(test_img, (190, 10))
    # Buttons ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_s:
                show = not show
            if event.key == K_a:
                mode += 1
                if mode > 2:
                    mode = 0
    # Update ------------------------------------------------- #
    screen.blit(pygame.transform.scale(display, (WINDOWWIDTH, WINDOWHEIGHT)), (0, 0))
    pygame.display.update()
