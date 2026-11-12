import pyautogui
import time
from datetime import datetime
from pathlib import Path

# Screenshot interval in seconds
INTERVAL = 10

# Folder where screenshots will be saved
SAVE_DIR = Path("screenshots")
SAVE_DIR.mkdir(exist_ok=True)

print("Screenshot capture started...")
print("Press Ctrl+C to stop.")

try:
    while True:
        # Capture screen
        screenshot = pyautogui.screenshot()

        # Create timestamped filename
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = SAVE_DIR / f"screenshot_{timestamp}.png"

        # Save screenshot
        screenshot.save(filename)

        print(f"Saved: {filename}")

        # Wait before next screenshot
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("\nScreenshot capture stopped.")