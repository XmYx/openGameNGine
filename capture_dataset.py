import os
import time
import subprocess
import pyautogui
from PIL import Image
from datetime import datetime

# Path to DOSBox executable and game
DOSBOX_PATH = "/usr/bin/dosbox"  # Default location; adjust if necessary
GAME_PATH = "/path/to/game/game.exe"
CONFIG_PATH = "/path/to/dosbox.conf"
CAPTURE_DIR = "/path/to/captures"

# Create capture directory if it doesn't exist
if not os.path.exists(CAPTURE_DIR):
    os.makedirs(CAPTURE_DIR)

# Define the action set in a clear, expandable manner
ACTIONS = {
    "move_forward": ['up'],
    "move_left": ['left'],
    "move_right": ['right'],
    "move_backward": ['down'],
    "shoot": ['space'],
    "open_door": ['ctrl'],  # Example action, adjust as per game controls
    # Add more actions as needed
}

def run_game():
    """Launch the game via DOSBox."""
    subprocess.Popen([DOSBOX_PATH, GAME_PATH, "-conf", CONFIG_PATH])
    time.sleep(5)  # Wait for the game to load

def capture_frame(action_name, frame_number):
    """Capture a screenshot of the game and save it."""
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = os.path.join(CAPTURE_DIR, f"{action_name}_frame_{frame_number}_{timestamp}.png")
    screenshot.save(image_path)
    print(f"Captured {image_path}")

def perform_action_and_capture(action_name, frame_number):
    """Perform an action in the game and capture the resulting frame."""
    keys = ACTIONS[action_name]
    for key in keys:
        pyautogui.press(key)
    
    time.sleep(1)  # Allow the game to react to the input
    capture_frame(action_name, frame_number)

def main():
    run_game()
    
    frame_number = 0

    # Loop through actions to perform them sequentially and capture frames
    for action_name in ACTIONS:
        perform_action_and_capture(action_name, frame_number)
        frame_number += 1

    # After capturing, close DOSBox
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')  # Send a command to close DOSBox

if __name__ == "__main__":
    main()
