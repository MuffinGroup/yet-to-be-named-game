#Importieren u.initialisieren der Pygame-Bibliothek
import pygame
pygame.init()

#Variablen/KONSTANTEN setzen
screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
FPS=60
SCHWARZ=(0,0,0)
WEISS  =(255,255,255)
GRAU   =(155,155,155)
spielaktiv=True

#gegner
gegnerBILD=pygame.image.load("src\main/assets\elements/background\Background final2.jpg")
bildgroessen=gegnerBILD.get_rect()
print(bildgroessen)
print(bildgroessen.center[0])
print(bildgroessen.center[1])
print(bildgroessen.width)
print(bildgroessen.height)

#Definieren und Öffnen eines neuen Fensters
gegnerBILD=pygame.image.load("src\main/assets\entities\enemies\Oger2.png")
gegnerBild=pygame.transform.scale(gegnerBILD,(400,400))
screen.blit(gegnerBild,(400,400))
fenster=pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Grafiken nutzen")
clock=pygame.time.Clock()

#Schleife Hauptprogramm
while spielaktiv:
    #Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        #beenden bei [ESC] oder [X]
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
            spielaktiv=False

    #Spielfeld/figuren zeichnen
    fenster.blit(gegnerBILD,(0,0))
    
    #Fenster aktualisieren
    pygame.display.flip()
    clock.tick(FPS)
    
    #Spielfeld löschen
    fenster.fill(GRAU)

    



