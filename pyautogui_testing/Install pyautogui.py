



import pyautogui

res = pyautogui.locateOnScreen("Test Image.png")
print(res)

centerpoint = pyautogui.locateCenterOnScreen("Test Image.png")
print(centerpoint)

