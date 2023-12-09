import pyautogui
from PIL import ImageDraw

import random

def locate_image_and_draw_box(image_path, confidence = 0.8, radius = 5):
    location = pyautogui.locateOnScreen(image_path, confidence)

    if location:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert Box object to a tuple (left, top, right, bottom)
        left, top, width, height = location
        right = left + width
        bottom = top + height
        rect_coords = (left, top, right, bottom)

        # Draw a red outline around the located image
        draw = ImageDraw.Draw(screenshot)
        draw.rectangle(rect_coords, outline='red', width=5)

        if (rect_coords[2] <= rect_coords[0] or rect_coords[3] <= rect_coords[1]):
            print("Invalid box dimensions")
            
        # Calculate valid range for the center of the circle
        valid_x_range = (rect_coords[0] + radius, rect_coords[2] - radius)
        valid_y_range = (rect_coords[1] + radius, rect_coords[3] - radius)
        
        # Generate random center within the valid range
        center_x = random.randint(*valid_x_range)
        center_y = random.randint(*valid_y_range)
        
        # Draw the circle
        bounding_box = [center_x - radius, center_y - radius, center_x + radius, center_y + radius]
        draw.ellipse(bounding_box, fill='blue', outline='black')  # Blue circle with a black outline

        # Save or display the result
        screenshot.show()  # This will display the image
        # screenshot.save('outlined_screenshot.png')  # Or save the image
    else:
        print("Image not found on the screen.")

# Uncomment the following line to test the function
# locate_image_and_draw_box("./imgs/QHD/refresh_button.png")