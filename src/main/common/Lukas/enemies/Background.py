#Importieren u.initialisieren der Pygame-Bibliothek
import pygame
pygame.init()

#Variablen/KONSTANTEN setzen
W, H= 800,600
FPS=60
SCHWARZ=(0,0,0)
WEISS  =(255,255,255)
GRAU   =(155,155,155)
spielaktiv=True

#gegner
gegnerBILD=pygame.image.load("src\main\common\Lukas\Pictures\Background image2.jpg")
bildgroessen=gegnerBILD.get_rect()
print(bildgroessen)
print(bildgroessen.center[0])
print(bildgroessen.center[1])
print(bildgroessen.width)
print(bildgroessen.height)

#Definieren und Öffnen eines neuen Fensters
fenster=pygame.display.set_mode((W,H))
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

    



