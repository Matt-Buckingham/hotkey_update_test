__version__ = "1.1"

import keyboard
import threading
import time
import pyautogui

def handle_hotkey():
    print("Hotkey triggered!")
    # Simulate moving the mouse cursor to a specific position
    pyautogui.moveTo(1500, 1500, duration=1)

# Termination thread function
def monitor_termination():
    while True:
        if keyboard.is_pressed('ctrl+esc'):
            print("Terminating script.")
            break
        time.sleep(0.1)

# Register the 'Alt+1' hotkey
keyboard.add_hotkey('alt+1', handle_hotkey)

# Start the termination monitor in a separate thread
termination_thread = threading.Thread(target=monitor_termination)
termination_thread.start()

# Main loop
try:
    while True:
        # Check for termination condition
        if termination_thread.is_alive():
            time.sleep(0.1)
        else:
            break

except KeyboardInterrupt:
    print("Script terminated.")
