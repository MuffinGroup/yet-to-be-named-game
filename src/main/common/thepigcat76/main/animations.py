import pygame
from pygame.locals import *

# Initiate pygame and give permission
# to use pygame's functionality
pygame.init()

# Create a display surface object
# of specific dimension
window = pygame.display.set_mode((600, 600))

# Create a list of different sprites
# that you want to use in the animation
image_sprite0 =  pygame.image.load("src/main/assets/entities/player/standard/animations/character_standard1.png")
image_sprite1 =  pygame.image.load("src/main/assets/entities/player/standard/animations/character_standard2.png")
image_sprite2 =  pygame.image.load("src/main/assets/entities/player/standard/animations/character_standard3.png")
image_sprite3 =  pygame.image.load("src/main/assets/entities/player/standard/animations/character_standard4.png")
image_sprite4 =  pygame.image.load("src/main/assets/entities/player/standard/animations/character_standard5.png")

height = 32
width = 32
scale = 10

image_sprite0 = pygame.transform.scale(image_sprite0, (int(width * scale), int(height * scale)))
image_sprite1 = pygame.transform.scale(image_sprite1, (int(width * scale), int(height * scale)))
image_sprite2 = pygame.transform.scale(image_sprite2, (int(width * scale), int(height * scale)))
image_sprite3 = pygame.transform.scale(image_sprite3, (int(width * scale), int(height * scale)))
image_sprite4 = pygame.transform.scale(image_sprite4, (int(width * scale), int(height * scale)))

# Creating a new clock object to
# track the amount of time
clock = pygame.time.Clock()

# Creating a new variable
# We will use this variable to
# iterate over the sprite list
value = 0


image_sprite = [image_sprite0, image_sprite1, image_sprite2, image_sprite3, image_sprite4]
# Creating a boolean variable that
# we will use to run the while loop
run = True

# Creating an infinite loop
# to run our game
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # Setting the framerate to 3fps just
    # to see the result properly
    clock.tick(6)

    # Setting 0 in value variable if its
    # value is greater than the length
    # of our sprite list
    if value >= len(image_sprite):
        value = 0

    # Storing the sprite image in an
    # image variable
    image = image_sprite[value]

    # Creating a variable to store the starting
    # x and y coordinate
    x = 150

    # Changing the y coordinate
    # according the value stored
    # in our value variable
    if value == 0:
        y = 200
    else:
        y = 200

    # Displaying the image in our game window
    window.blit(image, (x, y))

    # Updating the display surface
    pygame.display.update()

    # Filling the window with black color
    window.fill((0, 0, 0))

    # Increasing the value of value variable by 1
    # after every iteration
    value += 1