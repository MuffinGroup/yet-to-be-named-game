from os import error
import sys


try:
    import cv2
except ImportError:
    error("Install cv2 before running / install requirments.txt if present.")
    sys.exit(4)

# Load the two images
image1 = cv2.imread(
    "src\main/assets/textures\entities\characters\character_1/animations\character_1.png"
)
image2 = cv2.imread("src\main/assets/textures\entities\enemies\placeholder_enemy.png")

# Create a mask for the first image
gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray1, 10, 255, cv2.THRESH_BINARY)

# Set up the initial position of the second image
pos_x = 0
pos_y = 0


# Define a function to handle mouse events
def mouse_callback(event, x, y, flags, param):
    global pos_x, pos_y
    if event == cv2.EVENT_MOUSEMOVE:
        pos_x = x
        pos_y = y


# Create a window and set the mouse callback function
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)

while True:
    # Create a copy of the second image
    overlay = image2.copy()

    # Calculate the new position of the second image
    new_x = pos_x - image1.shape[1] // 2
    new_y = pos_y - image1.shape[0] // 2

    # Apply the mask to the first image
    masked_image = cv2.bitwise_and(image1, image1, mask=mask)

    # Overlay the masked image onto the second image
    overlay[
        new_y : new_y + masked_image.shape[0], new_x : new_x + masked_image.shape[1]
    ] = masked_image

    # Display the result
    cv2.imshow("Image", overlay)

    # Check for key presses
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Clean up
cv2.destroyAllWindows()
