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
    return sprite_list

walkingLoaded = 6

#walking_sprite = load_animation("1running", 8, 5, "src\main/assets/textures\entities\characters\character_1/animations/1Running", "png" ) 
idle_sprite = load_animation("1idle", 8, 6, "src\main/assets/textures\entities\characters\character_1/animations/1Idle", "png")
walking_sprite = load_animation("1running", 8, walkingLoaded, "src\main/assets/textures\entities\characters\character_1/animations/1Running", "png" )
startButton = load_animation("StartButtonSel", 9, 10, "src/main/assets/textures/elements/gui/StartButtonSel")
optionsButton = load_animation("OptionButtonSel", 9, 10, "src/main/assets/textures/elements/gui/OptionsButtonSel")
quitButton = load_animation("QuitButtonSel", 9, 10, "src/main/assets/textures/elements/gui/QuitButtonSel")