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

walkingLoaded = 2

#walking_sprite = load_animation("1running", 8, 5, "src\main/assets/textures\entities\characters\character_1/animations/1Running", "png") 
idle_sprite = load_animation("1idle", 8, 6, "src\main/assets/textures\entities\characters\character_1/animations/1Idle", "png")
walking_sprite = load_animation("1running", 8, walkingLoaded, "src\main/assets/textures\entities\characters\character_1/animations/1Running", "png")
startButton = load_animation("playButtonSel", 9, 6, "src/main/assets/textures/elements/gui/PlayButtonSel")
optionsButton = load_animation("OptionButtonSel", 9, 6, "src/main/assets/textures/elements/gui/OptionsButtonSel")
quitButton = load_animation("quitButtonSel", 9, 8, "src/main/assets/textures/elements/gui/QuitButtonSel")
npcTalkingNormal = load_animation("N1Talking", 8, 6, "src\main/assets/textures\entities/npc\Animations\Talking/normal")
npcTalkingPoppy = load_animation("N1Talking(poppy)", 8, 6, "src\main/assets/textures\entities/npc\Animations\Talking\poppy")
npcIdle = load_animation("npc", 2, 1, "src\main/assets/textures\entities/npc")
jump_sprite = load_animation("1jump", 8, 5, "src\main/assets/textures\entities\characters\character_1/animations/1Jump")
water_top_sprite = load_animation("Water_topIdel", 8, 30, "src\main/assets/textures\elements\Environment/fluids\WaterAnimations\Water_topIdle")
water_sprite = load_animation("WaterIdle", 8, 50, "src\main/assets/textures\elements\Environment/fluids\WaterAnimations\WaterIdle")
explosion = load_animation("ExplosionAnimation", 8, 1, "src\main/assets/textures\elements\Environment\Explosion")
lever = load_animation("LeverActivate", 8, 7, "src\main/assets/textures\elements\Environment\decoration\Lever")