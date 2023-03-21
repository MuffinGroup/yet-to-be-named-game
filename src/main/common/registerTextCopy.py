import pygame
import colors
import json

pygame.init()
language = "german"
textfont = pygame.font.SysFont('joystixmonospaceregular', 20)

if language == "english":
    with open("src/main/assets/lang/en_us.json", "r") as f:
        data = json.load(f)
    print(data["introduction_1"])
    
Info1Line1 = textfont.render(data["introduction_1"], True, colors.BLACK)