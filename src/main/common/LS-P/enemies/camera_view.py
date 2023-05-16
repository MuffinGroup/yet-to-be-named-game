import pygame

pygame.init()


#
###
class Player:
    def __init__(image):
        """Player constructor is called when player is instanced / declared.

        :param image: Player image to load from (not as a surface)
        :type image: str

        No self argument is present, as one is not needed.

        Player.image is not defined previously, as that would load image files when this file
        is imported, which could potentially cause problems if a display hasn't already been declared

        """

        Player.image = pygame.image.load(
            "src\main/assets/textures\entities\characters\character_1/animations\character_1.png"
        )  # Create Player Image
        Player.image = pygame.transform.scale(Player.image, (250, 250))
        Player.image_speed = 5
        Player.rect = pygame.Rect((50, 50), (30, 30))  # Create Player Rect

    def move(self, camera_pos):
        """Controls player movement

        This function reads player movement and modifies the player rect as needed.

        :param camera_pos: Camera position relative to player
        :type camera_pos: list[int, int]
        """

        pos_x, pos_y = camera_pos  # Split camara_pos
        #
        key = pygame.key.get_pressed()  # Get Keyboard Input
        if key[pygame.K_UP]:  # Check Key
            self.rect.y -= Player.image_speed  # Move Player Rect Coord
            pos_y += Player.image_speed  # Move Camara Coord Against Player Rect
        if key[pygame.K_LEFT]:
            self.rect.x -= Player.image_speed
            pos_x += Player.image_speed
        if key[pygame.K_DOWN]:
            self.rect.y += Player.image_speed
            pos_y -= Player.image_speed
        if key[pygame.K_RIGHT]:
            self.rect.x += Player.image_speed
            pos_x -= Player.image_speed
        #
        if self.rect.x < 0:  # Simple Sides Collision
            self.rect.x = 0  # Reset Player Rect Coord
            pos_x = camera_pos[0]  # Reset Camera Pos Coord
        elif self.rect.x > 1980:  # Set the Player`s moving range
            self.rect.x = 1980
            pos_x = camera_pos[0]
        if (
            self.rect.y < 0
            ):  # NOTE: https://www.youtube.com/watch?v=dQw4w9WgXcQ <- the beauty of open-source
            self.rect.y = 0
            pos_y = camera_pos[1]
        elif self.rect.y > 1980:
            self.rect.y = 1980
            pos_y = camera_pos[1]
        #
        return (pos_x, pos_y)  # Returns new, modified camera pos

    def render(self, display):
        display.blit(self.image, (self.rect.x, self.rect.y))


###
#
#
###
background = pygame.image.load(
    "src\main/assets/textures\elements/background\placeholder_background_0.jpg"
)
background = pygame.transform.scale(background, (2000, 2000)) # Creates 2k x 2k surface


# TODO: refactor Main function to main to match lower case linting standards
def Main(display, clock):
    world = pygame.Surface((2000, 2000))  # Creates map surface

    #
    player = Player()  # Instantiate player class, runs player initalizer
    camera_pos = (192, 192)  # Define camera starting position in pixels
    #
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                return
        #
        camera_pos = player.move(
            camera_pos # Run Player Move Function And Return New Camera Pos
        )
        #
        display.fill(colors["WHITE"])  # Fills the background with white to avoid ghosting
        player.render(world)  # Renders the player to the display
        display.blit(world, camera_pos)  # Renders map to the display
        world.blit(background, (0, 0))
        #
        pygame.display.flip()


###
#
if __name__ in "__main__":
    display = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("CameraView")
    clock = pygame.time.Clock()
    #
    global colors  # Define Colors
    colors = {
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "GREEN": (0, 255, 0),
        "BLUE": (0, 0, 255),
        "BLACK": (0, 0, 0),
    }
    Main(display, clock)  # Run Main Loop
