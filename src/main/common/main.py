import sys
import random
import pickle
from typing import Tuple
from os import path

import pygame

from registries.alerts import *
import registries.animations
from registries.colors import *
import registries.elements
import registries.gui
import registries.items
from registries.language import *

# pygame initialization
pygame.init()

class Player:
    # Initial Player attribute assignment
    def __init__(self):
        Player.defaultSpeed = 40
        Player.speed = Player.defaultSpeed
        Player.facingRight = True
        Player.facingLeft = False
        Player.standing = True
        Player.jumping = False
        Player.walking = False
        Player.collidingLeft = False
        Player.collidingRight = False
        Player.rect = pygame.Rect((1200, 870), (95, 186)) # Create the players hitbox
        Player.animationFrameUpdate = 1
        Player.debuggingMode = False
        Player.visible = True
        Player.locked = True
        Player.movementLocked = True
        Player.walkingLeftLocked = False
        Player.walkingRightLocked = False
        Player.jumpingLocked = True
        Player.debuggingMenu = False
        Player.flight = 0
        Player.collide = 0
        Player.showPos = 0
        Player.defaultHealth = 6 # most of the time it's 6
        Player.health = Player.defaultHealth
        Player.playedDeathSound = False
        Player.dead = False
        Player.chatOpen = False
        Player.world = None
        Player.langCounter = 0
        Player.languageList = ["en_us", "de_de"]
        Player.language = Player.languageList[Player.langCounter]
        Player.moving_right = False
        Player.moving_left = False
        Player.y_momentum = 0
        Player.air_timer = 0
        Player.holding = None
        Player.holdsItem = False
        Player.movement = [0, 0]
        Player.underWater = False
        Player.editMode = 0

    def keybinds(self, camera_pos):
        global player_x, player_y, key
        self.doorhandling = 0 # Door mechanics
        player_x = self.rect.x # Camera following the player
        player_y = self.rect.y

        jumpsound = pygame.mixer.Sound("src/main/assets/sounds/jump.wav")
        jumpsound.set_volume(0.09)    

        player_x, player_y = camera_pos # Assign variables to the camera position
        key = pygame.key.get_pressed()

        if Player.chatOpen == False:
            if key[pygame.K_UP] and Player.jumpingLocked == False and Player.locked == False and Player.movementLocked == False and Player.underWater == False:
                if Player.air_timer < 8:
                    Player.y_momentum = -30
                    pygame.mixer.Sound.play(jumpsound)
                    Player.jumping = True
                else: 
                    Player.jumping = False

            elif key[pygame.K_UP] and Player.jumpingLocked == False and Player.locked == False and Player.movementLocked == False and Player.underWater == True:
                Player.y_momentum = -5
                    
            if key[pygame.K_RIGHT] and Player.walkingRightLocked == False and Player.locked == False and Player.movementLocked == False:
                Player.facingLeft = False
                Player.facingRight = True
                Player.standing = False
                Player.moving_right = True
            else:
                Player.standing = True
                Player.walking = False
                Player.moving_right = False

            if key[pygame.K_LEFT] and Player.walkingLeftLocked == False and Player.locked == False and Player.movementLocked == False:
                Player.facingLeft = True
                Player.facingRight = False
                Player.standing = False
                Player.moving_left = True
            else:
                Player.standing = True
                Player.walking = False
                Player.moving_left = False

            #Debug mode to help developers
            if key[pygame.K_d] and Player.debuggingMode == False and Player.locked == False:
                pygame.time.wait(200)
                Player.debuggingMode = True
            elif key[pygame.K_d] and Player.debuggingMode == True and Player.debuggingMenu == False and Player.locked == False:
                pygame.time.wait(200)
                Player.debuggingMode = False

            if key[pygame.K_0] and Player.debuggingMode == True and Player.debuggingMenu == False and Player.locked == False:
                pygame.time.wait(200)
                Player.movementLocked = True
                Player.debuggingMenu = True
            elif key[pygame.K_0] or key[pygame.K_ESCAPE] and Player.debuggingMode == True and Player.locked == False:
                pygame.time.wait(200)
                Player.movementLocked = False
                Player.debuggingMenu = False

            if key[pygame.K_DOWN] and Player.visible == True and Player.debuggingMode == True and Player.movementLocked == False and Player.flight == 1 and Player.locked == False:
                Player.standing = False
                Player.facingLeft = False
                Player.facingRight = True
                self.rect.y += Player.speed 
            else:
                Player.standing = True
                Player.walking = False

            if key[pygame.K_u] and Player.visible == True and Player.debuggingMode == True and Player.movementLocked == False and Player.flight == 1 and Player.locked == False:
                Player.standing = False
                Player.facingLeft = False
                Player.facingRight = True
                self.rect.y -= Player.speed 
            else:
                Player.standing = True
                Player.walking = False

            #End of debugging mode functions

            if key[pygame.K_LEFT] and Player.walkingLeftLocked == False and Player.locked == False and Player.movementLocked == False or key[pygame.K_RIGHT] and Player.walkingRightLocked == False and Player.locked == False and Player.movementLocked == False: #Walking animations
                Player.walking = True
        
        #The chat
        if key[pygame.K_c] and Player.chatOpen == False and Player.debuggingMenu == False:
            pygame.time.wait(200)
            Player.chatOpen = True
            
        elif key[pygame.K_ESCAPE] and Player.chatOpen == True:
            pygame.time.wait(200)
            Player.chatOpen = False

        if Player.world == "tut1":
            return (-self.rect.x + 680, -self.rect.y + 550)# Return new player position
        else:
            return (-self.rect.x + 680, -self.rect.y + 400)
        
    def damage(damage):
        if Player.health > 0:
            Player.health -= damage
            if Player.health > 0.5:
                pygame.mixer.Sound.play(hurtSound)

    def heal(health):
        if Player.health + health <= Player.defaultHealth:
            Player.health += health

    def renderDebugMenu(self, language, map):
        global tut1_map
        toggleCollisionsText = registries.gui.registerFont(30, translatableComponent("text.debug_menu.collide", language), BLACK, 15, 30)
        toggleAdvMoveText = registries.gui.registerFont(30, translatableComponent("text.debug_menu.fly", language), BLACK, 15, 130)
        togglePosText = registries.gui.registerFont(25, translatableComponent("text.debug_menu.pos", language), BLACK, 15, 230)
        toggleEditModeText = registries.gui.registerFont(25, translatableComponent("text.debug_menu.editMode", language), BLACK, 15, 330)
        if Player.debuggingMenu == True:
            debugMenu.draw(screen, BLUISH_GRAY)
            toggleCollisionsText.drawFont(debugMenu.window)
            toggleAdvMoveText.drawFont(debugMenu.window)
            togglePosText.drawFont(debugMenu.window)
            toggleEditModeText.drawFont(debugMenu.window)
            if toggleCollisions.drawToggle(debugMenu.window, 320, 150, 75, 100):
                if Player.collide > 1:
                    Player.collide = 0
                Player.collide += 1
            if toggleAdvMove.drawToggle(debugMenu.window, 320, 250, 75, 100):
                if Player.flight > 1:
                    Player.flight = 0
                Player.flight += 1
            if togglePos.drawToggle(debugMenu.window, 320, 350, 75, 100):
                if Player.showPos > 1:
                    Player.showPos = 0
                Player.showPos += 1
            if toggleEditMode.drawToggle(debugMenu.window, 320, 450, 75, 100):
                if Player.editMode > 1:
                    Player.editMode = 0
                Player.editMode += 1
            if damageButton.draw(debugMenu.window, 225, 550, -35, -10, 75, 100, translatableComponent("button.debug_menu.damage", language), BLACK, "joystixmonospaceregular"):
                Player.damage(1)
            if healButton.draw(debugMenu.window, 225, 650, -60, -10, 75, 100, translatableComponent("button.debug_menu.heal", language), BLACK, "joystixmonospaceregular"):
                Player.heal(1)
            if saveButton.draw(debugMenu.window, 225, 750, -15, -10, 75, 100, translatableComponent("button.debug_menu.save", language), BLACK, "joystixmonospaceregular"):
                pickle_out = open(f'level1_data', 'wb')
                pickle.dump(map, pickle_out)
                pickle_out.close()
            if loadButton.draw(debugMenu.window, 225, 850, -15, -10, 75, 100, translatableComponent("button.debug_menu.load", language), BLACK, "joystixmonospaceregular"):
                if path.exists(f'level1_data'):
                    pickle_in = open(f'level1_data', 'rb')
                    tut1_map = pickle.load(pickle_in)
            #if loadButton.draw(debugMenu.window, 225, 850, )
        
    def render(self, surface):
            self.currentSprite = pygame.transform.scale(Player.currentSprite, (32 * 8, 32 * 8))
            # Drawing the player to the screen
            surface.blit(self.currentSprite,(self.rect.x - 75, self.rect.y - 70))
            if Player.debuggingMode == True:
                # Drawing the hitbox to the screen
                pygame.draw.rect(surface, (0, 255, 0), Player.rect, 4)
            Player.itemHandling(surface)

    dropped = False

    def editingMode(surface, map):
        if Player.editMode == 1:
            y = 0
            for row in map:
                x = 0
                for tile in row:
                    if tile == 0:
                        frame = pygame.Rect((96, 96), (x * 96, y * 96))
                        if frame.collidepoint(pygame.mouse.get_pos()):
                            pygame.draw.rect(surface, (255, 0, 255), frame, 3)
                        else:
                            pygame.draw.rect(surface, WHITE, frame, 3)
                    x += 1
                y += 1

    def itemHandling(world):
        if Player.holding != None:
            Player.holdsItem = True
        else:
            Player.holdsItem = False

        if poppy.pickedUp == True and Player.world == "tut2" and Player.visible == True:
            poppy.drawItem(world, Player, 0, 0)

    def giveItem(world, item):
        Player.holding = item
        item.drawItem(world, Player, 0, 200)
        if Player.visible == True:
            item.pickedUp = True

    def removeItem(item):
        try:
            item.pickedUp = False
            Player.holding = None
        except:
            pass

def TutorialRender(language):
    global Tut_welcome, Tut_walking_right, Tut_walking_left, Tut_jumping, Tut_item1, Tut_item2, Tut_item3, Tut_end
    key = pygame.key.get_pressed()
    if Tut_welcome == True:
        if key[pygame.K_SPACE]:
            Tut_welcome = False
        if key[pygame.K_RETURN]:
            Tut_welcome = False
            Tut_walking_right = True
    else:
        Player.locked = False

    if Tut_walking_right == True:
        Player.walkingRightLocked = False
        Player.walkingLeftLocked = True
        Player.jumpingLocked = True
        if Player.rect.x >= 1600:
            Tut_walking_right = False
            Tut_walking_left = True

    if Tut_walking_left == True:
        Player.walkingLeftLocked = False
        Player.jumpingLocked = True
        if Player.rect.x <= 1300:
            Tut_walking_left = False
            Tut_jumping = True

    if Tut_jumping == True:
        Player.jumpingLocked = False
        if Player.jumping == True:
            Tut_jumping = False
            Tut_item1 = True

    if Tut_item1 == True:
        if npcTalking == True:
            Tut_item1 = False
            Tut_item2 = True

    if Tut_item2 == True:
        if door0_open == True:
            Tut_item2 = False
            Tut_item3 = True

    if Tut_item3 == True:
        if poppyPlaced == True:
            Tut_item3 = False
            Tut_end = True

def TutorialPanelRenderer(language):
    if Tut_welcome:
        if language == 'de_de':
            tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', translatableComponent('text.tutorial.welcome', language), translatableComponent('text.tutorial.welcome1', language), translatableComponent('text.tutorial.welcome2', language), translatableComponent('text.tutorial.welcome3', language), translatableComponent('text.tutorial.welcome4', language), translatableComponent('text.tutorial.welcome5', language), translatableComponent('text.tutorial.welcome6', language), translatableComponent('text.tutorial.welcome7', language), translatableComponent('text.tutorial.welcome8', language), translatableComponent('text.tutorial.welcome9', language), translatableComponent('text.tutorial.welcome10', language), BLACK, -10, -10)
        if language == 'en_us':
            tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', '', translatableComponent('text.tutorial.welcome', language), translatableComponent('text.tutorial.welcome1', language), translatableComponent('text.tutorial.welcome2', language), translatableComponent('text.tutorial.welcome3', language), translatableComponent('text.tutorial.welcome4', language), translatableComponent('text.tutorial.welcome5', language), translatableComponent('text.tutorial.welcome6', language), translatableComponent('text.tutorial.welcome7', language), translatableComponent('text.tutorial.welcome8', language), '', BLACK, -10, -10)

    if Tut_walking_right == True:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', '', translatableComponent('text.tutorial.walking_right', language), translatableComponent('text.tutorial.walking_right1', language), '', '', '', '', '', '', '', '', BLACK, -10, -10)

    if Tut_walking_left == True:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', '', translatableComponent('text.tutorial.walking_right', language), translatableComponent('text.tutorial.walking_right1', language), translatableComponent('text.tutorial.walking_right2', language), '', translatableComponent('text.tutorial.walking_left', language), translatableComponent('text.tutorial.walking_left1', language), '', '', '', '', BLACK, -10, -10)

    if Tut_jumping == True:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', '', '', '', translatableComponent('text.tutorial.jump', language), translatableComponent('text.tutorial.jump1', language), translatableComponent('text.tutorial.jump2', language), '', '', '', '', '', BLACK, -10, -10)

    if Tut_item1 == True and npcTalking == False:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', translatableComponent('text.tutorial.item', language), translatableComponent('text.tutorial.item1', language), translatableComponent('text.tutorial.item2', language), '', '', '', '', '', '', '', '', BLACK, -10, -10)

    """if Tut_item2 == True:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', translatableComponent('text.tutorial.item', language), translatableComponent('text.tutorial.item1', language), translatableComponent('text.tutorial.item2', language), translatableComponent('text.tutorial.item3', language), translatableComponent('text.tutorial.item4', language), translatableComponent('text.tutorial.item5', language), translatableComponent('text.tutorial.item6', language), translatableComponent('text.tutorial.item7', language), '', '', '', BLACK, -10, -10)"""

    if Tut_item3 == True:
        tutWalking.render(screen, screen.get_width()//20, screen.get_width()//20, '', translatableComponent('text.tutorial.item', language), translatableComponent('text.tutorial.item1', language), translatableComponent('text.tutorial.item2', language), translatableComponent('text.tutorial.item3', language), translatableComponent('text.tutorial.item4', language), translatableComponent('text.tutorial.item5', language), translatableComponent('text.tutorial.item6', language), translatableComponent('text.tutorial.item7', language),translatableComponent('text.tutorial.item2.0', language), translatableComponent('text.tutorial.item2.1', language), '', BLACK, -10, -10)


def renderCoordinates():
    if Player.showPos == 1:
        coordinates = registries.gui.registerFont(35, str(str(Player.rect.x) + ", " + str(Player.rect.y)), WHITE, screen.get_width()//10 * 7, screen.get_height()//12)
        coordinates.drawFont(screen)

def resetDebugSettings():
    toggleAdvMove.test = 0
    toggleCollisions.test = 0
    togglePos.test = 0
    toggleEditMode.test = 0
    Player.collide = 0
    Player.flight = 0
    Player.showPos = 0
    Player.editMode = 0

Player()
#Loading element textures
grassElement = registries.elements.registerElement("elements/Environment/blocks/grass_dirt", 3)
dirtElement = registries.elements.registerElement("elements/Environment/blocks/Dirt", 3)
coarseDirtElement = registries.elements.registerElement("elements/Environment/blocks/Coarse_Dirt", 3)
coarseGrassElement = registries.elements.registerElement("elements/Environment/blocks/Coarse_Grass", 3)
cobbleElement = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
brickElement = registries.elements.registerElement("elements\Environment\Blocks/brick_wall", 3)
cobbleMossyElement = registries.elements.registerElement("elements/Environment/blocks/cobble_mossy", 3)
leverDeco = registries.elements.registerCallableAnimatedElement(3)
poppyDeco = registries.elements.registerElement("elements\Environment\decoration\Plants\poppy", 3)
grassDeco = registries.elements.registerElement("elements/Environment/decoration/Plants/grass", 3)
torchLeftDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/Torch(wall=left)", 3)
torchRightDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/Torch(wall=right)", 3)
torchTopDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/Torch(wall=top)", 3)
torchDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/Torch", 3)
specialTorchDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/special_torch", 3)
specialTorchHolderDeco = registries.elements.registerElement("elements/Environment/decoration/Torches/special_torch_holder", 3)
chainDeco = registries.elements.registerElement("elements/Environment/decoration/Chain/Chain", 3)
chainPartedDeco = registries.elements.registerElement("elements/Environment/decoration/Chain/Chain(parted)", 3) 
shieldDeco = registries.elements.registerElement("elements/Environment/decoration/Shields/Shield1", 3)
shieldDamagedDeco = registries.elements.registerElement("elements/Environment/decoration/Shields/Shield1(harmed)", 3)
bannerRedDeco = registries.elements.registerElement("elements/Environment/decoration/Banners/Banner1", 5)
bannerBlueDeco = registries.elements.registerElement("elements/Environment/decoration/Banners/Banner2", 5)
bannerYellowDeco = registries.elements.registerElement("elements/Environment/decoration/Banners/Banner3", 5)
door0OpenLargeElement = registries.elements.registerElement("elements/doors/door_0_open", 5)
door0ClosedLargeElement = registries.elements.registerElement("elements/doors/door_0_closed", 5)
door2OpenLargeElement = registries.elements.registerElement("elements/doors/door_2_open", 5)
door2ClosedLargeElement = registries.elements.registerElement("elements/doors/door_2_closed", 5)
darkCobble = registries.elements.registerElement("elements\Environment\Blocks\Cobble(Backround)", 3)
darkMossyCobble = registries.elements.registerElement("elements\Environment\Blocks\Mossy_cobble(Backround)", 3)
calcite = registries.elements.registerElement("elements\Environment\Blocks\Calcite", 3)
gravel = registries.elements.registerElement("elements\Environment\Blocks\Gravel", 3)
grass_end = registries.elements.registerElement("elements\Environment\Blocks\grass_side", 3)
sky = registries.elements.registerElement("elements\Environment\Sky\Sky", 6)
cloud = registries.elements.registerElement("elements\Environment\Sky\cloud", 1.5)
cobbleStairs = registries.elements.registerElement("elements\Environment\Blocks\Cobble_stairs", 3)
bush = registries.elements.registerElement("elements\Environment\decoration\Plants\Small_bush", 3)
explosion = registries.elements.registerAnimatedElement(16)
explosive = registries.elements.registerElement("elements\Environment\Blocks\TNT", 3)
light_dark_cobble = registries.elements.registerElement("elements\Environment\Blocks\light_dark_cobble", 3)
cobble_pedestal_inactive = registries.elements.registerElement("elements\Environment\Blocks\Pedestals\cobble_pedestal", 3)
wooden_plank = registries.elements.registerElement("elements/Environment/Blocks/wooden_plank", 3)
cobbleOffsetElement = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
cobbleY16Element = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
cobbleY32Element = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
cobbleY64Element = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
cobbleY80Element = registries.elements.registerElement("elements/Environment/blocks/cobble", 3)
towerWallBottom = registries.elements.registerElement("elements\Environment\Blocks/tower_wall", 3)
towerWall = registries.elements.registerElement("elements\Environment\Blocks/tower_wall2", 3)
towerWallTop= registries.elements.registerElement("elements\Environment\Blocks/tower_wall3", 3)
towerWallLong = registries.elements.registerElement("elements/Environment/Blocks/tower_wall4", 3)
towerWallWindow = registries.elements.registerElement("elements/Environment/Blocks/tower_window", 3)
towerWallWindow = registries.elements.registerElement("elements/Environment/Blocks/tower_window", 3)
hole = registries.elements.registerInvisibleElement()
hot_air = registries.elements.registerAnimatedElement(6)
npc = registries.elements.registerAnimatedElement(8) # 37/6
waterFluid = registries.elements.registerAnimatedElement(3)
waterWavingFluid = registries.elements.registerAnimatedElement(3)
door0Current = door0ClosedLargeElement
door2Current = door2ClosedLargeElement
poppy = registries.items.registerItem("elements\Environment\decoration\Plants\poppy")
torch = registries.items.registerItem("elements\Environment\decoration\Torches/Torch")

enemy_img = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png")
enemy_img_Scaled=pygame.transform.scale(enemy_img,(enemy_img.get_width( ) * 8, enemy_img.get_width() * 8))

creepy_sound = pygame.mixer.Sound("src/main/assets/sounds/scary.mp3")
creepy_sound.set_volume(0.2)

health = pygame.image.load("src\main/assets/textures\elements\gui\player\Heart(full).png")
healthScaled = pygame.transform.scale(health, (70, 70))

halfHealth = pygame.image.load("src\main/assets/textures\elements\gui\player\Heart(half).png")
halfHealthScaled = pygame.transform.scale(halfHealth, (70, 70))

emptyHealth = pygame.image.load("src\main/assets/textures/elements\gui\player\Heart(empty).png")
emptyHealthScaled = pygame.transform.scale(emptyHealth, (70, 70))
n = 0
npcCurrent = registries.animations.npcIdle
npcTalking = False

deathSound = pygame.mixer.Sound("src\main/assets\sounds\death.mp3")
deathSound.set_volume(0.25)
hurtSound = pygame.mixer.Sound("src\main/assets\sounds\hurt.mp3")
hurtSound.set_volume(0.25)

debugMenu = registries.gui.registerGui(70, 100, 300, 800, False)

font = pygame.font.Font('src\main/assets/fonts\joystixmonospaceregular.otf', 25)

def renderText(entry, language):
    debugMenuText = font.render(translatableComponent("text.debug_menu", language), True, DARK_ORANGE)
    debugModeText = font.render(translatableComponent("text.debug_mode", language), True, BLUE)
    texts = [debugMenuText, debugModeText]
    return texts[entry]

debug_menu = pygame.Rect((70, 70), (300, 400))

damageButton = registries.gui.registerButton("button", 4.0)
healButton = registries.gui.registerButton("button", 4.0)
saveButton = registries.gui.registerButton("button", 4.0)
loadButton = registries.gui.registerButton("button", 4.0)

toggleCollisions = registries.gui.registerButton("toggle", 12.0)
toggleAdvMove = registries.gui.registerButton("toggle", 12.0)
togglePos = registries.gui.registerButton("toggle", 12.0)
toggleEditMode = registries.gui.registerButton("toggle", 12.0)

screen_width = 1000
screen_height = 800

icon = pygame.image.load("src/main/assets/textures/elements/gui/icon/icon_32x.png")

chatBackground = registries.gui.registerGui(110, 100, 800, 600, False)
chat = registries.gui.registerChat(6, 30, BLACK, BLACK, BLACK, BLACK, 170, 110, 100, 800, 600, 140, 575, 735, 100)
chat.inputLocked = True
exitChat = registries.gui.registerExitButton(85, 80)
exitDebugMenu = registries.gui.registerExitButton(40, 75)
continueNpcTalk = registries.gui.registerExitButton(2950, 650, "gui\speech_bubble_button")

#tutorial working
Tut_welcome = True
Tut_walking_right = False
Tut_walking_left = False
Tut_jumping = False
Tut_item1 = False
Tut_item2 = False
Tut_item3 = False
Tut_end = False

door0_open = False
door2_open = False
doorsound = pygame.mixer.Sound('src/main/assets/sounds/Door_Closing.wav')
doorsound.set_volume(0.1)

leverOff = True
leverOn = False
leverTimer = 0
explosiveTimer = 0
leverPressed = 0
exploded = False
explosionCameraTimer = 0
cobble1X = cobbleElement.scaledTexture.get_width() * 31
cobble1Y = cobbleElement.scaledTexture.get_height() * 8
cobble2X = cobbleElement.scaledTexture.get_width() * 31
cobble2Y = cobbleElement.scaledTexture.get_height() * 9
cobbleModifier1 = 1
cobbleModifier10 = 1
cobbleModifier2 = 1
cobbleModifier20 = 1
element_rects = []

poppyPlaced = False
plankTimer = 0
plankCameraTimer = 0
yellowBannerDamaged = False
hasTorch = False
movesDown = False
posDone = False
bridgeTimer = 0
winTimer = 0

tic_tac_toe_board = pygame.image.load("src\main/assets/textures\elements\Environment\TicTacToe\TicTacToe.png")
tic_tac_toe_board = pygame.transform.scale(tic_tac_toe_board, (tic_tac_toe_board.get_width() * 3, tic_tac_toe_board.get_height() * 3))

def resetVars():
    global leverOn, leverOff, leverTimer, leverPressed
    leverOn = False
    leverOff = True
    leverTimer = 0
    leverPressed = 0

tutWalking = infoPanel("src\main/assets/textures\elements\gui/info_panel.png", 8, 15)

tut1_map = [[00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [ 2, 2, 2, 2, 2,21,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [ 1, 1, 1, 1, 1,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [ 1, 1, 1, 1, 1,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00],
            [ 1, 1, 1, 1, 1,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,22, 2, 2, 2, 2, 2, 2, 2, 2],
            [ 1, 1, 1, 1, 1,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1,00,00,00,00,11,00,11,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,44,39,39,39,45,00,00,00,00,00,00,00,00,00, 1, 1, 1, 6, 6, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 2,21,00,22, 7, 7, 2,21,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,46,39,48,39,47,00,00,00,00,00,11,11,12,11, 1,1 , 6, 6, 6, 6, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 6, 1,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,42,39,39,39,43,00,00,00,00,22, 7, 7, 7, 2, 1, 1, 6, 6, 6, 6, 6, 1],
            [ 1, 1, 1, 1, 6, 6, 6, 6, 1, 6, 6, 6,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,18,46, 9,39,39,47,00,00,00,00,11, 1, 6, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6],
            [ 1, 1, 1, 6, 6, 6, 6, 6, 1, 6, 6, 6,26,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,42,39,39,39,43,00,00,12,22, 7, 6, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6],
            [ 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 1, 7,21,26,00,11,11,11,11,11,11,00,26,11,11,11,11,11,11,00,12,00,11,00,00,00,40,39,39,39,41,26,22, 2, 2, 6, 6, 6, 6, 1, 1, 1, 6, 6, 6, 6, 6, 6],
            [ 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 7, 7, 2, 2, 2, 2, 2, 2, 2, 2, 2, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 6, 6, 6, 6, 6],
            [ 1, 1, 1, 1, 1, 6, 6, 1, 6, 6, 1, 1, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 6, 6, 6, 6, 6, 1, 1, 1, 1, 6, 6, 6, 1],
            [ 1, 1, 1, 1, 6, 6, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 6, 6, 6, 6, 1],
            [ 1, 1, 1, 1, 6, 1, 1, 1, 6, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 1, 6, 6, 6, 1, 1, 1, 6, 6, 6, 6, 1],
            [ 1, 1, 1, 6, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 1, 1, 1, 1, 6, 6, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 6, 6, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

tut2_map = [[ 3, 3, 3, 3, 3,16, 3,16, 3, 3,16, 3, 3,16, 3, 3,16, 3, 3, 3, 3,16, 3,16,16, 3, 3,16, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16, 3, 3, 3,16,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3, 3, 3,16,16, 3, 3, 3, 3, 3, 3,16,16, 3, 3,16, 3, 3,16, 3, 3,16, 3,16, 3, 3,16, 3,16, 3,16, 3, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16,16, 3, 3, 3,16,16, 3, 3, 3, 3, 3,16, 3, 3, 3, 3, 3, 3,16,16, 3,16, 3,16,16,16, 3, 3,16,16, 3, 3, 3,16, 3, 3, 3, 3,16, 3,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16, 3,16,16, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16,16,16, 3,16,16,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16, 3,16,16, 3,16, 3, 3, 3,16, 3,16, 3, 3, 3,16, 3, 3,16, 3,16, 3, 3,16, 3, 3,16,16,16, 3, 3,16, 3,16, 3, 3, 3,16, 3,16,16,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3,16, 3,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3,16,16,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3, 3,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,53,00, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3, 3,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00, 3,27,00,00,00,00,00,00,00,00,00,00,00,00, 3, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3, 3, 3,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16,27,27,00,00,00,00,00,00,00,00,00,00,00,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3,16, 3, 3,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00, 3,16, 3, 3,16,16, 3, 3, 3, 3, 3,16, 3,16,16, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,16,16, 3, 3,16, 3,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16,16, 3, 3,16,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3,16, 3,16, 3, 3,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,15, 3,16,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3,16,16,00,00,00,00,00,36,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,10, 3,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16, 3, 3, 3,00,00,00,00,16, 3,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3,16, 3,16, 3, 3,16, 3,16, 3, 3,00,00,00,00,16,16, 3, 3, 3, 3, 3,16, 3,16,16, 3, 3, 3,16, 3, 3,16, 3, 3, 3, 3, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3, 3, 3,16,16, 3, 3, 3,16, 3, 3,00,00,00,00, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3,16,16, 3, 3,16,16, 3, 3, 3, 3, 3, 3, 3, 3,16,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16, 3, 3,16, 3, 3,16, 3, 3, 3, 3, 3, 5, 5, 5, 5, 3, 3,16,16, 3,16,16, 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16, 3,16,16, 3, 3, 3, 3,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16, 3,16, 3, 3,16, 3, 3,16, 3, 3,16, 4, 4, 4, 4,16,16,16, 3,16, 3,16,16, 3, 3,16, 3, 3,16, 3, 3, 3,16,16, 3, 3,16, 3, 3, 3,16,16, 3, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3,16, 4, 4, 4, 4,16,16, 3, 3,16, 3,16, 3, 3,16, 3, 3, 3, 3,16,16, 3, 3, 3,16, 3, 3,16, 3,16, 3,16,16, 3,16,16, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16,16, 3, 3, 3,16, 3,16, 3, 3,16, 3, 3, 3,16, 3, 3, 3,16, 3, 3, 3,16, 3, 3, 3,16, 3, 3, 3,16, 3,16, 3, 3, 3, 3,16,16, 3, 3,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3,16, 3,16, 3, 3,16, 3, 3,16, 3, 3,16, 3, 3, 3, 3,16, 3,16,16, 3, 3,16, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16, 3, 3, 3,16,16,16, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3,16, 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16, 3,16,16, 3, 3, 3,16, 3, 3, 3,16, 3, 3,16,16,16, 3,16,16,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3,16, 3,16,16, 3, 3, 3, 3, 3,16, 3,16, 3, 3, 3,16, 3, 3,16, 3,16, 3, 3,16, 3, 3,16,16,16, 3, 3,16, 3,16, 3, 3, 3,16, 3,16,16,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,16,16, 3, 3, 3, 3, 3,16, 3, 3, 3,16,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3, 3,16, 3, 3,16, 3, 3, 3, 3, 3, 3, 3, 3]]

lvl1_map = [[ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,16,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,16,3 ,3 ,3 ,3 ,16,3 ,16,3 ,3 ,3 ,16,3 ,16,16,16,3 ,3 ,16,3 ,3 ,16,16,3 ],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,3 ,3 ,3 ,3 ,16,3 ,3 ,16,3 ,3 ,3 ,16,3 ,16,3 ,16,16,3 ,3 ,16,3 ,3 ,16,3 ,3 ,3 ,3 ,16,16,3 ,3 ,3 ,3 ,3 ,16,16,16,3 ,16,3 ,3 ,16,16],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3,16, 3,16, 3, 3,3 ,16,3 ,3 ,3 ,3 ,16,3 ,3 ,16,16,16,16,3 ,16,3 ,16,3 ,16,3 ,16,3 ,16,16,16,3 ,16,3 ,3 ,3 ,16,16,3 ,3 ,3 ,3 ,16,3 ,16,16,3 ,3 ,16],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,16,3 ,3 ,3 ,3 ,16,00,00,00,00,00,16,16,3 ,16,16,3 ,16,00,00,00,00,00,00,00,00,32,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16,3 ],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,16, 3,16,16,3 ,16,16,00,00,00,00,00,10,16,3 ,3 ,16,3 ,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,9 ,00,00,3 ,16],
            [ 3, 3,00,00,00,00,00,00,00,29,00,29,00,00,00,00,00,00,29,00,00,00,00,00,00,3 ,3 ,16,3 ,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16,3 ],
            [ 3, 3,14,00,00,00,30,00,00,29,00,29,00,00,00,00,00,00,00,00,00,23,3 ,16,3 ,3 ,16,3 ,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,16,3 ],
            [ 3,16,00,00,00,00,00,00,00,29,00,29,00,00,00,00,00,00,00,00,23,16,16,3 ,16,3 ,16,3 ,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,3 ,00,00,00,00,00,00,00,29,00,29,00,23,3 ,3 ,3 ,3 ,3 ,3 ,3 , 3, 3, 3,16,3 ,3 ,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,16, 3, 3, 3, 3,16, 3,37,37,37,3 , 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3,16,16,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,16, 3, 3, 3, 3,16, 3,00,00,00,3 , 3, 3, 3, 3, 3, 3, 3,16, 3, 3, 3,16,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,16,16, 3, 3, 3, 3,16,00,00,00, 3, 3, 3, 3, 3, 3, 3, 3, 3,16, 3, 3,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,16,16, 3, 3, 3, 3,16,00,00,00, 3,3 ,3 ,3 ,3 ,3 ,3 ,3 ,3 ,16, 3,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,16,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,00,19,19,19,00,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [ 3,3 ,00,00,00,00,00,00,00,00,00,00,00,33,00,00,00,00,19,19,19,00,00,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [16,3 ,50,00,00,00,00,00,00,00,00,00,00,00,51,00,00,00,19,19,19,00,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [16,16,00,00,00,00,00,00,00,00,00,00,00,00,51,00,00,00,19,19,19,00,00,00,23, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,3 ,16,16,3 ,16,3 ,16,3 , 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,16, 3, 3,16,3 ,16,3 ,3 ,3 ,16,16,3 ,3 ,00,16,3 ,3 , 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,16, 3, 3,16,3 ,16,3 ,3 ,16,3 ,3 ,3 ,16,00,16,3 , 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [16,3 ,3 ,16,3 ,3 ,3 ,16,16,16,16,16,16, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [16,3 , 3, 3,16,3 ,16,3 ,3 ,16,3 , 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,3 ,16,16,3 ,16,3 ,16, 3, 3,3 , 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,3 ,3 ,16,3 ,3 ,3 ,16,16,16,16,16,16, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [16,3 ,3 ,16,3 ,3 ,3 ,16,16, 3, 3,16, 3, 3,00, 3, 3,16, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [3 ,16,16,16,16,16,16, 3,16, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,16, 3],
            [ 3, 3, 3, 3, 3, 3, 3, 3, 3,3 ,3 , 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3,00, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
            [28, 3, 3,28,28,28, 3, 3,28,28,28, 3, 3, 3,00,28, 3, 3, 3, 3, 3,28,37, 3, 3,28,28,28, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3,28,28,28, 3, 3, 3,28,28, 3, 3,28,28,28,28,28, 3, 3,28,28],
            [28,28,28,28,28,28,28,28,28,28,28,28, 3,28,00,28,28,28,28,28,28,00,00,00,28,28,28,28,28,28,28, 3,28,28,28, 3, 3,28,28,00,00,28,28,28,28,28,28,28,28,28,28,00,28,28,28,28,28],
            [28,28,28,28,28,28,28,28,28,28,28,28,28,28,00,00,00,00,00,00,00,00,00,00,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,00,00,00,28,28,28,00,00,00,28,00,28,28],
            [28,28,28,28,28,28,28,28,28,28,28,28,28,28,00,00,00,00,00,00,00,00,00,00,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,00,00,00,28,28,28,00,00,00,28,00,28,28],
            [28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,00,00,00,28,28,28,00,00,00,28,00,28,28]]

ttt_map = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
# 33-21
inputLocked = True
input = 1
gameWon = False
gameLost = False
loseTimer = 0
selectedXPos = 0
selectedYPos = 0
allowTicTacToe = False
leaveTtt = False

def ticTacToe(screen, xPos, yPos):
    global input, inputLocked, gameLost, gameWon, loseTimer, ttt_map, selectedXPos, selectedYPos, frame_rects, lvl1_map, winTimer, leaveTtt, allowTicTacToe
    frameX, frameY = random.randint(0, 2), random.randint(0, 2)
    frame_rects = []
    not0 = []

    y = 0
    for row in ttt_map:
        x = 0
        for tile in row:
            frame = pygame.Rect((x * 100 + xPos, y * 100 + yPos), (100, 100))
            if ttt_map[selectedYPos][selectedXPos] == 0 and key[pygame.K_RETURN] and allowTicTacToe == True:
                ttt_map[selectedYPos][selectedXPos] = 1
                inputLocked = True
            if x == selectedXPos and y == selectedYPos:
                pygame.draw.rect(screen, (255, 0, 255), frame, 3)
            else:
                pygame.draw.rect(screen, (255, 255, 255), frame, 3)
            if not tile == 0:
                not0.append(tile)
            if tile == 1:
                pygame.draw.line(screen, (255, 0, 0), frame.bottomleft, frame.topright, 7)
                pygame.draw.line(screen, (255, 0, 0), frame.bottomright, frame.topleft, 7)
            if tile == 2:
                pygame.draw.circle(screen, (255, 0, 255), frame.center, frame.width//2, 7)
            screen.blit(tic_tac_toe_board, (2010, 2970))

            # Check lines
            if all(cell == 1 for cell in row):
                gameWon = True
                print(1)

            # Check columns
            for col in range(3):
                if all(ttt_map[row][col] == 1 for row in range(3)):
                    gameWon = True
                    print(2)

            # Check diagonals
            if all(ttt_map[i][i] == 1 for i in range(3)):
                    gameWon = True
                    print(3)

            if all(ttt_map[i][2 - i] == 1 for i in range(3)):
                    gameWon = True
                    print(4)

            # Bot winning
            # Check lines
            if all(cell == 2 for cell in row):
                    gameLost = True

            # Check columns
            for col in range(3):
                if all(ttt_map[row][col] == 2 for row in range(3)):
                    gameLost = True

            # Check diagonals
            if all(ttt_map[i][i] == 2 for i in range(3)):
                    gameLost = True
            
            if all(ttt_map[i][2 - i] == 2 for i in range(3)):
                    gameLost = True

            if inputLocked == True and gameWon == False:
                if ttt_map[frameX][frameY] == 0:
                    pygame.time.wait(200)
                    ttt_map[frameX][frameY] = 2
                    if Player.world == "lvl1":
                        inputLocked = False
    
            if gameWon == True:
                lvl1_map[30][22] = 0
                allowTicTacToe = False
                leaveTtt = True

            if leaveTtt == True:
                if Player.rect.x < 2100:
                    Player.rect.x += 10
                if Player.rect.x > 2100:
                    Player.rect.x -= 10
                for i in range(21, 33):
                    lvl1_map[i][22] = 49

            if gameLost == True:
                if loseTimer < 180:
                     loseTimer += 1
                else:
                    print("Bot wins!")
                    ttt_map = [[0, 0, 0],
                               [0, 0, 0],
                               [0, 0, 0]]

                gameLost = False

            if len(not0) == 9:
                print("Tie")
                ttt_map = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
                not0 = []

            frame_rects.append(frame)

            x += 1
        y += 1

def loadExplosion(map, world):
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == 25:
                explosion.drawAnimatedElement(world, x, y, deco_rects, registries.animations.explosion)
                explosion.yModifier = -600
                explosion.xModifier = -400
            x += 1
        y += 1

def genWorld(world, map):
    global door0Current, n, element_rects, deco_rects, npcCurrent, stair_rects, npcTalking, leverOff, leverOn, leverTimer, exploded, explosiveTimer, leverPressed, explosionCameraTimer, player_y, player_x, camera_pos, cobble1X, cobble1Y, cobble2X, cobble2Y, cobbleModifier1, cobbleModifier2, cobbleModifier10, cobbleModifier20, plankTimer, plankCameraTimer, poppyPlaced, yellowBannerDamaged, hasTorch, movesDown, bridgeTimer, poppyAlert, posDone, leverDeco
    element_rects = []
    deco_rects = []
    stair_rects = []
    y = 0
    
    for row in map:
        x = 0
        for tile in row:
            if tile == 1:
                dirtElement.drawElement(world, x, y, element_rects)
            if tile == 2:
                grassElement.drawElement(world, x, y, element_rects)
            if tile == 3:
                cobbleElement.drawElement(world, x, y, element_rects)
            if tile == 6:
                coarseDirtElement.drawElement(world, x, y, element_rects)
            if tile == 7:
                coarseGrassElement.drawElement(world, x, y, element_rects)
            #Don't use 9
            if tile == 10:
                leverDeco.drawCallableAnimatedElement(world, x, y, deco_rects, registries.animations.lever)
            if tile == 11:
                grassDeco.drawElement(world, x, y, deco_rects)
            if tile == 12:
                poppyDeco.drawElement(world, x, y, deco_rects)
            if tile == 14:
                torchLeftDeco.drawElement(world, x, y, deco_rects)
            if tile == 15:
                torchRightDeco.drawElement(world, x, y, deco_rects)
            if tile == 16:
                cobbleMossyElement.drawElement(world, x, y, element_rects)
            if tile == 17:
                torchDeco.drawElement(world, x, y, deco_rects)
            if tile == 19:
                gravel.drawElement(world, x, y, element_rects)
            if tile == 20:
                calcite.drawElement(world, x, y, element_rects)
            if tile == 20:
                calcite.drawElement(world, x, y, element_rects)
            if tile == 21:
                grass_end.drawRotatedElement(world, x, y, False, False)
            if tile == 22:
                grass_end.drawRotatedElement(world, x, y, True, False)
            if tile == 23:
                cobbleStairs.drawStairElement(world, x, y, False, False, element_rects)
            # Don't use tile 25. It is used in the loadExplosion method
            if tile == 26:
                bush.drawElement(world, x, y, deco_rects)
            if tile == 27:
                explosive.drawElement(world, x, y, element_rects)
            if tile == 28:
                light_dark_cobble.drawElement(world, x, y, element_rects)
            if tile == 29:
                chainDeco.drawElement(world, x, y, deco_rects)
            if tile == 30:
                bannerRedDeco.drawElement(world, x, y, deco_rects)
            if tile == 32:
                bannerBlueDeco.drawElement(world, x, y, deco_rects) 
            if tile == 33:
                bannerYellowDeco.drawElement(world, x, y, deco_rects)
                bannerYellowDeco.xModifier = 70
                bannerYellowDeco.xRectModifier = 70
            if tile == 34:
                shieldDamagedDeco.drawElement(world, x, y, deco_rects)
            # Don't use tile 35 it is used for background loading
            if tile == 36:
                cobble_pedestal_inactive.drawPedestalElement(world, x, y, element_rects)
            if tile == 37:
                wooden_plank.drawElement(world, x, y, element_rects)
                wooden_plank.heightModifier = -76
                print(x, y)
            if tile == 38:
                cobbleOffsetElement.drawElement(world, x, y, element_rects)
                cobbleOffsetElement.xModifier = -cobbleOffsetElement.rect.width // 2
                cobbleOffsetElement.xRectModifier = -cobbleOffsetElement.rect.width // 2
            if tile == 39:
                brickElement.drawElement(world, x, y, deco_rects)
            if Player.world == "tut1" and tile == 9:
                brickElement.drawElement(world, x, y, deco_rects)
            if tile == 40:
                towerWallBottom.drawStairElement(world, x, y, False, False, deco_rects)
            if tile == 41:
                towerWallBottom.drawStairElement(world, x, y, True, False, deco_rects)
            if tile == 42:
                towerWall.drawRotatedElement(world, x, y, False, False)
            if tile == 43:
                towerWall.drawRotatedElement(world, x, y, True, False)
            if tile == 44:
                towerWallTop.drawStairElement(world, x, y, True, False, deco_rects)
            if tile == 45:
                towerWallTop.drawStairElement(world, x, y, False, False, deco_rects)
            if tile == 46:
                towerWallLong.drawRotatedElement(world, x, y, False, False)
            if tile == 47:
                towerWallLong.drawRotatedElement(world, x, y, True, False)
            if tile == 48:
                towerWallWindow.drawElement(world, x, y, deco_rects)
            if tile == 49:
                hot_air.drawAnimatedElement(world, x, y, deco_rects, registries.animations.hot_air)
            if tile == 50:
                specialTorchDeco.drawElement(world, x, y, deco_rects)
            if tile == 51:
                hole.drawElement(x, y, deco_rects)
            if tile == 52:
                specialTorchHolderDeco.drawElement(world, x, y, deco_rects)
            x += 1
        y += 1

    for tiles in element_rects:
        if Player.debuggingMode == True:
            pygame.draw.rect(world, (255, 255, 255), tiles, 3)

    for tiles in deco_rects:
        if Player.debuggingMode == True:
            pygame.draw.rect(world, (255, 255, 255), tiles, 3)

    if Player.world == "tut2":
        if Player.rect.colliderect(cobble_pedestal_inactive.rect2) and poppy.pickedUp == True:
            poppyPlaced = True
        if poppyPlaced == True:
            poppy.pickedUp = False
            poppy.texture = pygame.transform.scale(poppy.texture, (32 * 3, 32 * 3))
            poppy.drawGhostItem(world, 1247, 1158)
            bridgeTimer += 1
        if bridgeTimer == 10:
            tut2_map[15][16] = 37
        if bridgeTimer == 20:
            tut2_map[15][17] = 37
        if bridgeTimer == 30:
            tut2_map[15][18] = 37
        if bridgeTimer == 40:
            tut2_map[15][19] = 37
        
        if leverOff == True and Player.rect.colliderect(leverDeco.rect) and key[pygame.K_e] and leverTimer >= 5:
            leverTimer = 0
            pygame.mixer.music.pause()
            leverOn = True
            leverOff = False
        if explosiveTimer >= 1:
            explosiveTimer += 1
        leverTimer += 1
        if leverOn == True:
            leverDeco.callAnimation()
            if leverDeco.frame == 34:
                leverPressed += 1
                explosionCameraTimer += 1
                exploded = True

        if explosionCameraTimer >= 1 and player_x <= -2533 and player_y <= -444:
            camera_pos = (player_x + 10, player_y + 5)
            Player.locked = True
            Player.facingLeft = True
        elif explosionCameraTimer >= 1 and explosiveTimer < 8:
            camera_pos = (-2533, -444)
            explosiveTimer += 1
            tut2_map[9][32] = 0
            tut2_map[9][33] = 25
            tut2_map[8][32] = 0
            tut2_map[8][31] = 0
            tut2_map[9][31] = 0
            world.blit(cobbleElement.scaledTexture, (cobble1X, cobble1Y))
            world.blit(cobbleElement.scaledTexture, (cobble2X, cobble2Y))
            pygame.mixer.music.unpause()
            cobble2Y -= 64 * cobbleModifier2 * cobbleModifier20
            cobble2X -= 208
            if cobble2X < 2720:
                cobbleModifier2 = -1
                cobbleModifier20 = 4
            if cobble2X <= 2250:
                cobble2X = 2250
                cobble2Y = 1350
            cobble1Y -= 64 * cobbleModifier1 * cobbleModifier10
            cobble1X -= 192
            if cobble1X < 2720:
                cobbleModifier1 = -1
                cobbleModifier10 = 4
            if cobble1X <= 2300:
                tut2_map[13][24] = 3
        if explosiveTimer >= 8 and explosiveTimer < 32:
            tut2_map[9][33] = 0
            camera_pos = (-2534, -445)
            world.blit(cobbleElement.scaledTexture, (cobble1X, cobble1Y))
            world.blit(cobbleElement.scaledTexture, (cobble2X, cobble2Y))
            cobble2Y -= 64 * cobbleModifier2 * cobbleModifier20
            cobble2X -= 208
            if cobble2X < 2720:
                cobbleModifier2 = -1
                cobbleModifier20 = 4
            if cobble2X <= 2250:
                cobble2X = 2250
                cobble2Y = 1350
            cobble1Y -= 64 * cobbleModifier1 * cobbleModifier10
            cobble1X -= 192
            if cobble1X < 2720:
                cobbleModifier1 = -1
                cobbleModifier10 = 4
            if cobble1X <= 2300:
                tut2_map[13][24] = 3
            Player.locked = False
        if explosionCameraTimer >= 1 and explosiveTimer >= 1 and explosiveTimer < 5:
            explosion_sound = pygame.mixer.Sound('src/main/assets/sounds/explosion.mp3')
            explosion_sound.set_volume(0.1)
            pygame.mixer.Sound.play(explosion_sound)
        elif explosiveTimer >= 32:
            camera_pos = (-Player.rect.x + 680, -Player.rect.y + 400)
            world.blit(cobbleElement.scaledTexture, (cobble1X, cobble1Y))
            world.blit(cobbleElement.scaledTexture, (cobble2X, cobble2Y))
            cobble2Y -= 64 * cobbleModifier2 * cobbleModifier20
            cobble2X -= 208
            if cobble2X < 2720:
                cobbleModifier2 = -1
                cobbleModifier20 = 4
            if cobble2X <= 2250:
                tut2_map[14][24] = 38
            cobble1Y -= 64 * cobbleModifier1 * cobbleModifier10
            cobble1X -= 192
            if cobble1X < 2720:
                cobbleModifier1 = -1
                cobbleModifier10 = 4
            if cobble1X <= 2300:
                tut2_map[13][24] = 3
            Player.locked = False

    elif Player.world == "lvl1":
        if leverOff == True and Player.rect.colliderect(leverDeco.rect) and key[pygame.K_e] and leverTimer >= 5:
            leverTimer = 0
            pygame.mixer.music.pause()
            leverOn = True
            leverOff = False
            Player.locked = True
        if leverOn == True:
            leverDeco.callAnimation()
            if leverDeco.frame == 34:
                leverPressed += 1
                plankCameraTimer += 1
        if plankCameraTimer >= 1 and player_x <= -400:
            camera_pos = (player_x + 10, player_y - 3)
        if plankCameraTimer >= 1 and player_x >= -400:
            camera_pos = (-400, player_y)
            plankCameraTimer += 1
        if plankCameraTimer >= 32:
            camera_pos = (-Player.rect.x + 680, -Player.rect.y + 400)
        if Player.rect.x >= 864 and Player.rect.x <= 1057 and Player.rect.y == 966 and leverOn == True:
            plankTimer += 1
        if plankTimer >= 1:
            plankTimer += 1
        if plankTimer == 30:
            lvl1_map[12][11] = 29
            lvl1_map[12][10] = 0
            lvl1_map[12][9] = 29
            lvl1_map[13][11] = 37
            lvl1_map[13][10] = 37
            lvl1_map[13][9] = 37
        if plankTimer == 60:
            lvl1_map[13][11] = 29
            lvl1_map[13][10] = 0
            lvl1_map[13][9] = 29
            lvl1_map[14][11] = 37
            lvl1_map[14][10] = 37
            lvl1_map[14][9] = 37
        if plankTimer == 90:
            lvl1_map[14][11] = 29
            lvl1_map[14][10] = 0
            lvl1_map[14][9] = 29
            lvl1_map[15][11] = 37
            lvl1_map[15][10] = 37
            lvl1_map[15][9] = 37
        if plankTimer == 120:
            lvl1_map[15][11] = 29
            lvl1_map[15][10] = 0
            lvl1_map[15][9] = 29
            lvl1_map[16][11] = 37
            lvl1_map[16][10] = 37
            lvl1_map[16][9] = 37
        if plankTimer == 150:
            lvl1_map[16][11] = 29
            lvl1_map[16][10] = 0
            lvl1_map[16][9] = 29
            lvl1_map[17][11] = 37
            lvl1_map[17][10] = 37
            lvl1_map[17][9] = 37
        if plankTimer == 180:
            lvl1_map[17][11] = 29
            lvl1_map[17][10] = 0
            lvl1_map[17][9] = 29
            lvl1_map[18][11] = 37
            lvl1_map[18][10] = 37
            lvl1_map[18][9] = 37
        if plankTimer == 210:
            lvl1_map[18][11] = 29
            lvl1_map[18][10] = 0
            lvl1_map[18][9] = 29
            lvl1_map[19][11] = 37
            lvl1_map[19][10] = 37
            lvl1_map[19][9] = 37

        if Player.rect.colliderect(bannerYellowDeco.rect) and key[pygame.K_e] and yellowBannerDamaged == False and hasTorch == True:
            lvl1_map[17][13] = 0
            yellowBannerDamaged = True

        if yellowBannerDamaged == True and Player.rect.colliderect(hole) and key[pygame.K_e]:
            movesDown = True
            hasTorch = False

        if Player.rect.colliderect(specialTorchDeco.rect) and key[pygame.K_e] and hasTorch == False:
            lvl1_map[18][2] = 52
            hasTorch = True

        """if Player.rect.colliderect(cobbleStairs.rect1) and Player.jumping == False:
            Player.rect.bottom = cobbleStairs.rect1.top
            pygame.draw.rect(world, WHITE, Player.rect, 3)"""
        
        if movesDown == True and Player.rect.y < 3078:
            Player.collide = 1
        elif movesDown == True:
            Player.collide = 0
            movesDown = False

        if movesDown == True and Player.rect.x < 1344:
            Player.rect.x += 20
            Player.facingRight = True
            Player.locked = True

        if movesDown == True and Player.rect.x > 1344:
            Player.rect.x -= 20
            Player.facingRight = True
            Player.locked = True

        if movesDown == False:
            Player.locked = False
            
        leverTimer += 1

drownTime = 0
def loadFluids(map, surface): 
    global fluid_rects, drownTime
    fluid_rects = []
    fluids_collding = []
    y = 0
    
    for row in map:
        x = 0
        for tile in row:
            if tile == 4:
                waterFluid.drawAnimatedElement(surface, x, y, fluid_rects, registries.animations.water_sprite)
            if tile == 5:
                waterWavingFluid.drawAnimatedElement(surface, x, y, fluid_rects, registries.animations.water_top_sprite)
            x += 1
        y += 1

    if Player.world == "tut2":

        for fluid in fluid_rects:
            if Player.rect.colliderect(fluid):
                fluids_collding.append(fluid)
                Player.underWater = True
            if not Player.rect.colliderect(fluid):
                Player.underWater = False

        for collidingFluids in fluids_collding:
            pygame.draw.rect(surface, (255, 255, 255), collidingFluids, 3)
            drownTime += 4
            pygame.draw.rect(surface, WHITE, Player.rect, 3)
            if drownTime > 0:
                drownTime -= 1
        
            if drownTime >= 120 or Player.dead == True:
                Player.damage(1)
                drownTime = 0

def loadBackground(map, surface):
    global background_rects, element_rects
    background_rects = []
    element_rects = []
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if Player.world == "tut1" and tile != 39:
                sky.drawElement(surface, x * 4, y * 4, background_rects)
            if Player.world == "tut2" and tile != 35:
                darkCobble.drawElement(surface, x, y, background_rects)
            if Player.world == "lvl1" and tile != 35 and tile != 51:
                darkCobble.drawElement(surface, x, y, background_rects)
            if tile == 35:
                darkMossyCobble.drawElement(surface, x, y, deco_rects)
            x += 1
        y += 1

def loadForeGround(map, surface, language):
    global foreground_rects, npcTalking, door0Current, n, npcCurrent, npcTalking, door0_open, door2Current, door2_open
    foreground_rects = []

    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == 9:
                door0Current.drawElement(surface, x, y, deco_rects)
                door0Current.yModifier = -22
                door0Current.widthModifier = -75
                door0Current.xRectModifier = 50
                door0Current.yRectModifier = -22
            if tile == 18:
                npc.drawAnimatedElement(surface, x, y, foreground_rects, npcCurrent)
                npc.yModifier = 32
                npc.widthModifier = -160
                npc.heightModifier = -100
                npc.xRectModifier = 80
                npc.yRectModifier = 120
            if tile == 53:
                door2Current.drawElement(world, x, y, deco_rects)
                door2Current.yModifier = -22
                door2Current.widthModifier = -75
                door2Current.xRectModifier = 50
                door2Current.yRectModifier = -22
            x += 1
        y += 1
    if Player.rect.colliderect(door0ClosedLargeElement.rect) and Player.visible == True and key[pygame.K_e]:
        if Player.world != "tut1":
            door0_open = True
            door0Current = door0OpenLargeElement
            door0Current.yModifier = -22
            door0Current.widthModifier = -75
            door0Current.xRectModifier = 50
            door0Current.yRectModifier = -22
            n += 1
        elif not Player.rect.colliderect(npc.rect) and Player.holding == poppy.id:
            door0Current = door0OpenLargeElement
            door0Current.yModifier = -22
            door0Current.widthModifier = -75
            door0Current.xRectModifier = 50
            door0Current.yRectModifier = -22
            n += 1

    if Player.world == "tut2":
        if Player.rect.colliderect(door2ClosedLargeElement.rect) and Player.visible == True and key[pygame.K_e]:
            door2_open = True
            door2Current = door2OpenLargeElement
            door2Current.yModifier = -22
            door2Current.widthModifier = -75
            door2Current.xRectModifier = 50
            door2Current.yRectModifier = -22
            n += 1

    if n == 30 and door0_open == True:
        Player.visible = False
        door0_open = False
        door0Current = door0ClosedLargeElement
        door0Current.yModifier = -22
        door0Current.widthModifier = -75
        door0Current.xRectModifier = 50
        door0Current.yRectModifier = -22
        pygame.mixer.Sound.play(doorsound)

    if n == 30 and door2_open == True:
        Player.visible = False
        door2_open = False
        door2Current = door2ClosedLargeElement
        door2Current.yModifier = -22
        door2Current.widthModifier = -75
        door2Current.xRectModifier = 50
        door2Current.yRectModifier = -22
        pygame.mixer.Sound.play(doorsound)

    if n == 40:
        n = 0
        if Player.world == "tut1":
            Tut2(language)
        elif Player.world == "tut2":
            Lvl1(language)
    if n >= 1 and n <= 50:
        n += 1

    if Player.world == "tut1":
        if Player.rect.colliderect(npc.rect) and key[pygame.K_e]:
            npcCurrent = registries.animations.npcTalkingNormal
            npcTalking = True

"""def loadLights(surface, map):
    y = 0
    for row in map:
        x = 0
        for tile in row:
            if tile == 53:
                surface.blit(light, (x * 32 - 320, y * 32 - 224))
            x += 1
        y += 1"""
        
def health():
        for i in range(Player.defaultHealth):
            if (i % 2) == 0:
                screen.blit(emptyHealthScaled, (10 + i * emptyHealthScaled.get_width()//2, 0))

        for i in range(Player.health):
            if (i % 2) == 0:
                screen.blit(halfHealthScaled, (10 + i * halfHealthScaled.get_width()//2, 0))
            else:
                screen.blit(healthScaled, (10 + i * healthScaled.get_width()//2 - halfHealthScaled.get_width()//2, 0))

def collisionTest(player, rectArray):
    hit_list = []
    for tile in rectArray:
        if player.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(player, movement, rectArray):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    player.x += movement[0]
    hit_list = collisionTest(player, rectArray)
    for tile in hit_list:
        if movement[0] > 0 and Player.collide != 1:
            player.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0 and Player.collide != 1:
            player.left = tile.right
            collision_types['left'] = True
    player.y += movement[1]
    hit_list = collisionTest(player, rectArray)
    for tile in hit_list:
        if movement[1] > 0 and Player.collide != 1:
            player.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0 and Player.collide != 1:
            player.top = tile.bottom
            collision_types['top'] = True
    return player, collision_types

def movementControl(self):
    Player.movement = [0, 0]

    if self.moving_right == True and Player.underWater == False:
        Player.movement[0] += 20
    elif self.moving_right == True and Player.underWater == True:
        Player.movement[0] += 5
    if self.moving_left == True and Player.underWater == False:
        Player.movement[0] -= 20
    elif self.moving_left == True and Player.underWater == True:
        Player.movement[0] -= 5

    Player.movement[1] += self.y_momentum
    self.y_momentum += 1
    if self.y_momentum > 20:
        self.y_momentum = 20

    self.rect, collisions = move(self.rect, Player.movement, element_rects)

    if collisions['bottom']:
        self.y_momentum = 0
        self.air_timer = 0
    else:
        self.air_timer += 10

    if Player.visible == False:
        Player.locked = True
    else:
        Player.locked = False

    if Player.locked == True:
        Player.movementLocked = True
    else:
        Player.movementLocked = False

    if Player.movementLocked == True:
        Player.walkingLeftLocked = True
        Player.walkingRightLocked = True
        Player.jumpingLocked = True
    else:
        Player.walkingLeftLocked = False
        Player.walkingRightLocked = False
        Player.jumpingLocked = False
    
def Start(language):
    Player()
    resetDebugSettings()
    i = 0
    Player.world = None
    startButton = registries.gui.registerButton("button", 6.0)
    optionsButton = registries.gui.registerButton("button", 6.0)
    quitButton = registries.gui.registerButton("button", 6.0)
    clock = pygame.time.Clock()
    resetVars()
    while True:
        key = pygame.key.get_pressed()
        pygame.mixer.music.stop()
        language = Player.languageList[i]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and Player.world == None:
                pygame.quit()
                sys.exit()

        startFont = registries.gui.registerFont(40, "YET-BE-NAMED-GAME", DARKER_GRAY, screen.get_width()//2 - 250, screen.get_height()//9)
        screen.fill(BLUISH_GRAY)
        if startButton.drawAnimated(screen, screen.get_width()//2, screen.get_height()//8 * 2.75, registries.animations.startButton, 48, 48, 6, -125, -25, translatableComponent("button.start", language), BLACK, "joystixmonospaceregular"):
            Tut1(language)
        if optionsButton.drawAnimated(screen, screen.get_width()//2, screen.get_height()//2, registries.animations.optionsButton, 48, 48, 6, -125, -25, translatableComponent("button.options", language), BLACK, "joystixmonospaceregular"):
            if i < len(Player.languageList) -1:
                i += 1
            else:
                i = 0
        if quitButton.drawAnimated(screen, screen.get_width()//2, screen.get_height()//8 * 5.25, registries.animations.quitButton, 48, 48, 6, -125, -25, translatableComponent("button.quit", language), BLACK, "joystixmonospaceregular"):
            pygame.quit()
            sys.exit()
            
        if key[pygame.K_RETURN] and Player.world == None:
            pygame.quit()
            sys.exit()

        startFont.drawFont(screen)
        pygame.display.flip()
        clock.tick(1000)
        
def commandEvent(event, language):
    if chat.userInput.lower() == "/world tut2" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not Player.world == "tut2" and Player.debuggingMode == True:
        chat.userInput = ""
        chat.linesLoaded[0] = translatableComponent("command.teleport.tut2", language)
        chat.x = chat.markerDefaultPos
        Tut2(language)
                
    if chat.userInput.lower() == "/world tut1" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not Player.world == "tut1" and Player.debuggingMode == True:
        chat.userInput = ""
        chat.linesLoaded[0] = translatableComponent("command.teleport.tut1", language)
        chat.x = chat.markerDefaultPos
        Tut1(language)
                
    if chat.userInput.lower() == "/world lvl1" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and not Player.world == "lvl1" and Player.debuggingMode == True:
        chat.userInput = ""
        chat.linesLoaded[0] = translatableComponent("command.teleport.lvl1", language)
        chat.x = chat.markerDefaultPos
        Lvl1(language)

def deathEvent(language):
    if Player.rect.y >= 4000:
        Start(language)
        Player.dead = True

def parse_input(input_str: str) -> Tuple[str, int, int]:
    test_str = input_str.lower()
    components = test_str.split(" ")
    command = " ".join(components[0:-2])
    x, y = (int(components[-2]), int(components[-1]))
    return command, x, y
    
def Tut1(language):
    global command, x, y, camera_pos, poppy, npcTalking, npcCurrent
    enemy_x = 3000
    enemy_y = 1170
    world = pygame.Surface((6000,6000), pygame.SRCALPHA) # Create Map
    player = Player() # Initialize Player Class
    resetDebugSettings()
    camera_pos = (0, 0) #camera starting position
    # values for animation calculation
    idleValue = 0
    walkingValue = 0
    pickUpValue = 0
    
    pygame.mixer.music.load("src\main/assets\sounds\GameMusic.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.1)
    Player.world = "tut1"
    resetVars()
    while True:
        key = pygame.key.get_pressed()
        # Fill the background outside of the map
        screen.fill(AQUA)

        loadBackground(tut1_map, world)

        genWorld(world, tut1_map)

        loadForeGround(tut1_map, world, language)

        movementControl(Player)

        try:
            command, x, y = parse_input(chat.userInput.lower())
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if chat.userInput.lower() == "/lang de_de" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[1]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            
            if chat.userInput.lower() == "/lang en_us" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[0]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            try:
                if parse_input(str(chat.userInput.lower())) and command == "/place block" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    chat.userInput = ""
                    chat.x = chat.markerDefaultPos
                    chat.linesLoaded[0] = translatableComponent("command.place", language)
                    tut1_map[y][x] = 17
            except:
                pass

            commandEvent(event, language)
            chat.event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and Player.chatOpen == False and Player.debuggingMenu == False:
                Start(language)
        
        # idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        # loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0
        if registries.items.pickingUp == True:
            if pickUpValue > len(registries.animations.pickup_sprite) - 3:
                registries.items.pickingUp = False
            else:
                pickUpValue += 1

            if pickUpValue >= len(registries.animations.pickup_sprite) // 2:
                registries.items.finishedPickup = True
        
        # Movement animation rendering
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_sprite[walkingValue]
        
        if registries.items.pickingUp == True:
            Player.currentSprite = registries.animations.pickup_sprite[pickUpValue]

        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        # bliting to the world

        if Player.visible == True:
            player.render(world)

        if key[pygame.K_4]:
            Player.giveItem(world, poppy)

        if npcTalking == True:
            Player.giveItem(world, poppy)

        loadFluids(tut1_map, world)

        loadExplosion(tut1_map, world)

        cloud.drawElement(world, 10, 2, background_rects)

        # Enemy Import
        enemy_img = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png")
        enemy_img_Scaled = pygame.transform.scale(enemy_img,(enemy_img.get_width() * 8, enemy_img.get_width() * 8))
        image_rect = enemy_img_Scaled.get_rect()
        enemy_speed = 5
        if enemy_x <= 3000:
           enemy_x -= enemy_speed
        if enemy_x <= 2500:
           enemy_x += 5
        world.blit(enemy_img_Scaled,(enemy_x, enemy_y))

        if Tut_welcome == True:
            Player.locked = True

        TutorialRender(language)

        camera_pos = player.keybinds(camera_pos)

        if key[pygame.K_3]:
            Player.removeItem(poppy)
        """if npcTalking == True:
            if continueNpcTalk.draw(world):
                npcCurrent = registries.animations.npcIdle
                npcTalking = False"""
        
        Player.editingMode(world, tut1_map)

        # Render the map to the screen
        speech_bubble = infoPanel("src\main/assets/textures\elements\gui\speech_bubble.png", 4, 25)
        if npcTalking == True:
            speech_bubble.render(world, 3050, 1200, translatableComponent('text.tutorial.item3', language), translatableComponent('text.tutorial.item4', language), translatableComponent('text.tutorial.item5', language), translatableComponent('text.tutorial.item6', language), translatableComponent('text.tutorial.item7', language), "", "", "", "", "", "", "", BLACK, -25, -25)

        poppy.drawItem(world, Player, 1000, 1000)
        
        screen.blit(world, (player_x, player_y))

        if Player.debuggingMode == True:
            screen.blit(renderText(0, language), (440, 90))

        screen.blit(renderText(1, language), (440, 30))

        # Rendering the debug menu
        player.renderDebugMenu(language, tut1_map)

        health()
        
        if Player.health > Player.defaultHealth:
            Player.health = Player.defaultHealth
            
        if Player.health <= 0 and Player.defaultHealth != 0:
            Player.dead = True
        else:
            Player.dead = False
            
        if Player.dead == True:
            Player.movementLocked = True
        else:
            Player.movementLocked = False
            
        if Player.dead == True and Player.playedDeathSound == False:
            pygame.mixer.Sound.play(deathSound)
            Player.playedDeathSound = True

        elif Player.dead == False:
            Player.playedDeathSound = False

        # Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate
        
        if Player.chatOpen == True:
            chatBackground.draw(screen, "default")
            chat.drawChat(screen)
            chat.inputLocked = False
            Player.locked = True
            if exitChat.draw(screen):
                Player.chatOpen = False
        else:
            chat.inputLocked = True
            Player.locked = False

        if Player.debuggingMenu == True:
            if exitDebugMenu.draw(screen):
                Player.debuggingMenu = False
        deathEvent(language)
        
        TutorialPanelRenderer(language)
        
        renderCoordinates()

        clock.tick(1600)
        pygame.display.flip()

def Tut2(language):
    global camera_pos, world, poppyAlert
    world = pygame.Surface((6000,3000), pygame.SRCALPHA) # Create Map
    player = Player() # Initialize Player Class
    resetDebugSettings()
    camera_pos = (0, 0) #camera starting position

    # values for animation calculation
    idleValue = 0
    walkingValue = 0
    Player.rect.x, Player.rect.y = 900, 750

    pygame.mixer.music.load("src\main/assets\sounds\MysteriousGameMusic.mp3")
    pygame.mixer.music.play(1000)
    pygame.mixer.music.set_volume(0.1)
    
    Player.world = "tut2"
    poppyAlert = notification("src\main/assets/textures\elements\gui/notification_bar.png", "src\main/assets/textures\elements\Environment\decoration\Plants\poppy.png", 3, screen.get_width(), 200, 100)
    resetVars()
    while True: # Render background
        world.fill(DARK_GRAY)

        # Fill the background outside of the map
        screen.fill(DARK_GRAY)

        loadBackground(tut2_map, world)
        
        genWorld(world, tut2_map)

        loadForeGround(tut2_map, world, language)

        movementControl(Player)

        try:
            command, x, y = parse_input(chat.userInput.lower())
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if chat.userInput.lower() == "/lang de_de" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[1]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            
            if chat.userInput.lower() == "/lang en_us" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[0]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            try:
                if parse_input(str(chat.userInput.lower())) and command == "/place block" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    chat.userInput = ""
                    chat.x = chat.markerDefaultPos
                    chat.linesLoaded[0] = translatableComponent("command.place", language)
                    tut2_map[y][x] = 17
            except:
                pass
            commandEvent(event, language)
            chat.event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and Player.chatOpen == False and Player.debuggingMenu == False:
                Start(language)
        
        # idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        # loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0
        
        TutorialRender(language)

        # Player movement
        camera_pos = player.keybinds(camera_pos) 

        # Movement animation rendering
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_sprite[walkingValue]
        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        if Player.visible == True:
            player.render(world)

        loadFluids(tut2_map, world)

        loadExplosion(tut2_map, world)
        
        # Render the map to the screen
        screen.blit(world, (player_x, player_y))

        renderCoordinates()

        if Player.debuggingMode == True:
            screen.blit(renderText(0, language), (440, 90))
            
        screen.blit(renderText(1, language), (440, 30))

        # Rendering the debug menu
        player.renderDebugMenu(language, tut2_map)	
        
        health()
        if Player.health > Player.defaultHealth:
            Player.health = Player.defaultHealth
            
        if Player.health <= 0 and Player.defaultHealth != 0:
            Player.dead = True
        else:
            Player.dead = False
            
        if Player.dead == True:
            Player.movementLocked = True
        else:
            Player.movementLocked = False
            
        if Player.dead == True and Player.playedDeathSound == False:
            pygame.mixer.Sound.play(deathSound)
            Player.playedDeathSound = True

        elif Player.dead == False:
            Player.playedDeathSound = False

        # Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate
        if Player.chatOpen == True:
            chatBackground.draw(screen, "default")
            chat.drawChat(screen)
            chat.inputLocked = False
            Player.locked = True
            if exitChat.draw(screen):
                Player.chatOpen = False
        else:
            chat.inputLocked = True
            Player.locked = False

        if Player.debuggingMenu == True:
            if exitDebugMenu.draw(screen):
                Player.debuggingMenu = False

        """filter = pygame.surface.Surface((world.get_width(), world.get_height()))
        filter.fill((204,204,204))
        loadLights(filter, tut2_map)
        screen.blit(filter, (player_x, player_y), special_flags=pygame.BLEND_RGBA_SUB)"""

        deathEvent(language)

        TutorialPanelRenderer(language)

        if bridgeTimer >= 40:
            poppyAlert.render(screen, "Freundliche", "Geste", BLACK)

        clock.tick(1600)
        pygame.display.flip()

def Lvl1(language):
    global command, x, y, camera_pos, world, selectedYPos, selectedXPos, allowTicTacToe, frame_rects
    enemy_x = 1000
    enemy_y = 1170
    world = pygame.Surface((6000,6000), pygame.SRCALPHA) # Create Map
    player = Player() # Initialize Player Class
    resetDebugSettings()
    camera_pos = (0, 0) #camera starting position
    # values for animation calculation
    idleValue = 0
    walkingValue = 0
    Player.rect.x, Player.rect.y = 350, 1050

    pygame.mixer.music.pause()

    pygame.mixer.Sound.play(creepy_sound)
    
    Player.world = "lvl1"
    resetVars()
    while True:
        # Fill the background outside of the map
        world.fill(DARK_GRAY)

        # Fill the background outside of the map
        screen.fill(DARK_GRAY)

        movementControl(Player)

        try:
            command, x, y = parse_input(chat.userInput.lower())
        except:
            pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if chat.userInput.lower() == "/lang de_de" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[1]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            
            if chat.userInput.lower() == "/lang en_us" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                chat.userInput = ""
                chat.x = chat.markerDefaultPos
                language = Player.languageList[0]
                chat.linesLoaded[0] = translatableComponent("command.lang", language) + language
            try:
                if parse_input(str(chat.userInput.lower())) and command == "/place block" and event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    chat.userInput = ""
                    chat.x = chat.markerDefaultPos
                    chat.linesLoaded[0] = translatableComponent("command.place", language)
                    lvl1_map[y][x] = 17
            except:
                pass
            
            for frame in frame_rects:
                if key[pygame.K_e] and Player.rect.colliderect(frame):
                    allowTicTacToe = True

            if allowTicTacToe == True:
                if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
                    if selectedXPos >= 2:
                        selectedXPos = 0
                        if selectedYPos != 2:
                            selectedYPos += 1
                        else:
                            selectedYPos = 0
                    else:
                        selectedXPos += 1
                if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
                    if selectedXPos <= 0 and not selectedYPos <= 0:
                        selectedXPos = 2
                        selectedYPos -= 1
                    elif selectedXPos == 0 and selectedYPos == 0:
                         selectedYPos = 2
                         selectedXPos = 2
                    elif selectedXPos != 0:
                        selectedXPos -= 1
                if event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
                    selectedYPos += 1
                if event.type == pygame.KEYUP and event.key == pygame.K_UP:
                    selectedYPos -= 1

            commandEvent(event, language)
            chat.event(event)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and Player.chatOpen == False and Player.debuggingMenu == False:
                Start(language)
        
        # idle animation calculation
        if idleValue >= len(registries.animations.idle_sprite):
            idleValue = 0

        # loading the idle animation
        Player.currentSprite = registries.animations.idle_sprite[idleValue]
        
        if walkingValue >= len(registries.animations.walking_sprite):
            walkingValue = 0

        loadBackground(lvl1_map, world)

        genWorld(world, lvl1_map)

        loadForeGround(tut1_map, world, language)

        if allowTicTacToe == True:
            Player.locked = True

        if leaveTtt == True:
            Player.locked = True
        
        # Player movement
        camera_pos = player.keybinds(camera_pos) 

        # Movement animation rendering
        if Player.walking == True:
            Player.currentSprite = registries.animations.walking_sprite[walkingValue]
        if Player.facingLeft == True:
            Player.currentSprite = pygame.transform.flip(Player.currentSprite, True, False)

        if Player.visible == True:
            player.render(world)

        if hasTorch == True:
            Player.giveItem(world, torch)

        loadFluids(lvl1_map, world)

        loadExplosion(lvl1_map, world)

        # Enemy
        enemy_img = pygame.image.load("src\main/assets/textures\entities\enemies\placeholder_enemy.png")
        enemy_img_Scaled = pygame.transform.scale(enemy_img,(enemy_img.get_width() * 8, enemy_img.get_width() * 8))
        enemy_rect = enemy_img_Scaled.get_rect()
        enemy_speed = 5
        enemy_facing_left = True
        enemy_x -= enemy_speed
        world.blit(enemy_img_Scaled,(enemy_x, enemy_y))

        ticTacToe(world, 2010, 2970)

        screen.blit(world, (player_x, player_y))
        renderCoordinates()

        if Player.debuggingMode == True:
            screen.blit(renderText(0, language), (440, 90))
            
        screen.blit(renderText(1, language), (440, 30))

        # Rendering the debug menu
        player.renderDebugMenu(language, lvl1_map)
        
        health()
        
        if Player.health > Player.defaultHealth:
            Player.health = Player.defaultHealth
            
        if Player.health <= 0 and Player.defaultHealth != 0:
            Player.dead = True
        else:
            Player.dead = False
            
        if Player.dead == True:
            Player.movementLocked = True
        else:
            Player.movementLocked = False
            
        if Player.dead == True and Player.playedDeathSound == False:
            pygame.mixer.Sound.play(deathSound)
            Player.playedDeathSound = True

        elif Player.dead == False:
            Player.playedDeathSound = False

        # Idle animations
        if Player.standing == True:
            idleValue += 1
        if Player.walking == True:
            walkingValue += Player.animationFrameUpdate
        
        if Player.chatOpen == True:
            chatBackground.draw(screen, "default")
            chat.drawChat(screen)
            chat.inputLocked = False
            Player.locked = True
            if exitChat.draw(screen):
                Player.chatOpen = False
        else:
            chat.inputLocked = True
            Player.locked = False

        if Player.debuggingMenu == True:
            if exitDebugMenu.draw(screen):
                Player.debuggingMenu = False
                
        deathEvent(language)

        clock.tick(1600)
        pygame.display.flip()

if __name__ in "__main__":
    Player()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("yet-to-be-named-game")
    pygame.display.set_icon(icon)
    clock = pygame.time.Clock()
    Start(Player.language)