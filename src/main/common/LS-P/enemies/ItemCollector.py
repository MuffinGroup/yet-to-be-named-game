import pygame
import random

# initialize pygame
pygame.init()

# set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controllable Character")

# set up clock
clock = pygame.time.Clock()

# define colors
black = (0, 0, 0)
white = (255, 255, 255)

# load images
character_image = pygame.image.load("src\main/assets/textures\entities\characters\character_1/animations\character_1.png").convert_alpha()
character_image=pygame.transform.scale(character_image,(250,250))
screen.blit(character_image,(340,190))
item_image = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png").convert_alpha()
item_image=pygame.transform.scale(item_image,(250,250))
screen.blit(item_image,(340,190))

# define character
class Character(pygame.sprite.Sprite):
 def __init__(self, x, y):
  super().__init__()
  self.image = character_image
  self.rect = self.image.get_rect()
  self.rect.x = x
  self.rect.y = y
  self.speed = 5
 def update(self):
   keys = pygame.key.get_pressed()
   if keys[pygame.K_LEFT]:
    self.rect.x -= self.speed
   elif keys[pygame.K_RIGHT]:
    self.rect.x += self.speed
   elif keys[pygame.K_UP]:
    self.rect.y -= self.speed
   elif keys[pygame.K_DOWN]:
    self.rect.y += self.speed

# define item
class Item(pygame.sprite.Sprite):
 def __init__(self):
   super().__init__()
   self.image = item_image
   self.rect = self.image.get_rect()
   self.rect.x = random.randint(0, screen_width - self.rect.width)
   self.rect.y = random.randint(0, screen_height - self.rect.height)

# create sprites
all_sprites = pygame.sprite.Group()
character = Character(0, 0)
item = Item()
all_sprites.add(character, item)

# main loop
running = True
while running:
 # handle events
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
      running = False
 
 # update sprites
 all_sprites.update()

 # check if item is in range
 if pygame.sprite.collide_rect(character, item):
  item.kill()
 
 # draw screen
 screen.fill(white)
 all_sprites.draw(screen)

 # update display
 pygame.display.update()

 # tick clock
 clock.tick(60)

# quit pygame
pygame.quit()