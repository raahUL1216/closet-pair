import cv2
import numpy as np

def identify_skin_color(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of skin color in HSV color space
    lower_skin = np.array([0, 48, 80], dtype=np.uint8)
    upper_skin = np.array([20, 255, 255], dtype=np.uint8)

    # Create a mask to detect skin color
    skin_mask = cv2.inRange(hsv_image, lower_skin, upper_skin)

    # Apply the mask to the original image
    skin_image = cv2.bitwise_and(image, image, mask=skin_mask)

    # Calculate the average color of the skin region
    average_color = cv2.mean(skin_image, skin_mask)[:3]

    # Convert the average color to RGB format
    average_color_rgb = np.array(average_color[::-1], dtype=np.uint8)

    # Convert the average color to hexadecimal format
    average_color_hex = '#{:02X}{:02X}{:02X}'.format(*average_color_rgb)

    return average_color_hex
