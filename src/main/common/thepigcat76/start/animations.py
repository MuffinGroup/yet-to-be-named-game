import pygame

#Thanks to Tim Cook aka PFornax from daskomikos discord server for helping us out with improving this <3
def load_animation(AlphaImageName, numberofsprites, timesLoaded, dictionary = None, format = "png"):
    if timesLoaded <= 0:
        print("timesLoaded must be 1 or above")
    while timesLoaded <= 0:
        pygame.quit()
        exit
    sprite_list = []
    for sprite in range(1, numberofsprites):
        currentimagename = str(dictionary)+"/"+str(AlphaImageName)+"("+str(sprite) + ")" + "." +str(format)
        image = pygame.image.load(currentimagename)
        for i in range(timesLoaded):
            sprite_list.append(image)
        #sprite_list.append(image6)
        #sprite_list.append(image7)
    return sprite_list

startButton = load_animation("StartButtonSel", 9, 4, "src/main/assets/textures/elements/gui/StartButtonSel")
optionsButton = load_animation("OptionButtonSel", 9, 4, "src/main/assets/textures/elements/gui/OptionsButtonSel")
quitButton = load_animation("QuitButtonSel", 9, 4, "src/main/assets/textures/elements/gui/QuitButtonSel")