
import pyautogui
from io import BytesIO


def capture_screenshot():

    # Capture the current screen
    screenshot = pyautogui.screenshot()

    # Get screenshot dimensions
    width, height = screenshot.size

    # Convert image into bytes in memory
    image_buffer = BytesIO()
    screenshot.save(image_buffer, format="PNG")

    image_bytes = image_buffer.getvalue()

    # Close the image and temporary buffer
    screenshot.close()
    image_buffer.close()

    return image_bytes, width, height
