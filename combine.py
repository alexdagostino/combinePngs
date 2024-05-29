import cv2
import numpy as np

# Read the images
imgTop = cv2.imread('top.png')
qrcodeImage = cv2.imread('qr.png')
imgBottom = cv2.imread('bottom.png')

def createSquare():
    height = 640
    width = 190
    background_color = (229, 239, 231)

    # Create an image with all pixel values set to the background color
    image = np.full((height, width, 3), background_color, dtype=np.uint8)

    # Step 2: Define the rectangle properties
    top_left = (100, 100)  # Top-left corner of the rectangle (x, y)
    bottom_right = (400, 400)  # Bottom-right corner of the rectangle (x, y)
    color = (229, 239, 231)  # Rectangle color in BGR (Green)
    thickness = 0  # Thickness of the rectangle border. Use -1 for filled r

    cv2.rectangle(image, top_left, bottom_right, color, thickness)

    # # Step 4: Display the image
    # cv2.imshow('Rectangle Image', image)

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return image
    



squareLeft = createSquare()
squareRight = createSquare()


# create middle section of imagle
imageMiddle = cv2.hconcat([squareLeft, qrcodeImage, squareRight])

# Vertically concatenate images
image_final = cv2.vconcat([imgTop, imageMiddle, imgBottom])

# Display the concatenated image
cv2.imshow('Concatenated Image', image_final)
cv2.imwrite("newImage.PNG", image_final) 
    # Wait until a key is pressed and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()


