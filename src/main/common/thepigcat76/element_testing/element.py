import pygame

pygame.init()
def register_elements(self, elementLocation, scale):
    image = pygame.image.load("src/main/assets/textures/elements/environment/" + elementLocation + ".png")
    self.width = image.get_width()
    self.height = image.get_height()
    self.image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))

def blitElement(self, surface, elementX, elementY):
    surface.blit(self.image, (elementX, elementY))

class testing():
    screen = pygame.display.set_mode((720,720), pygame.RESIZABLE)
    register_elements( "blocks/wooden_sign", 10)
    
    while True:
        for event in pygame.event.get():
              if event.type == pygame.QUIT:
                pygame.quit
                exit()
        blitElement(screen, 0, 0)
        pygame.display.update()