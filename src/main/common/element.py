import pygame

pygame.init()
class element():
    def register_elements(self, elementCategory,elementName, registryName):
        element.registryName = pygame.image.load("src/main/assets/textures/elements/environment/" + elementCategory + "/" + elementName + ".png")

    def blitElement(surface, elementX, elementY):
        elementPos = (elementX, elementY)
        surface.blit(element.registryName, elementPos)

    def getRegistryName():
        return element.registryName