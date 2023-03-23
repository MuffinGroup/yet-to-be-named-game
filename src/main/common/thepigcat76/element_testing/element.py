import pygame

pygame.init()
class self():
    global registryName
    global width
    global height
    def register_elements(self, elementCategory,elementName, registryName):
        registryName = pygame.image.load("src/main/assets/textures/elements/environment/" + elementCategory + "/" + elementName + ".png")
        registryName = pygame.transform.scale(registryName, (250,250))
        width = registryName.get_width()
        height = registryName.get_height()

    def blitElement(surface, elementX, elementY):
        elementPos = (elementX, elementY)
        surface.blit(registryName, elementPos)