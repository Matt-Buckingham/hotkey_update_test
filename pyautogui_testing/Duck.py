import pyautogui
import time
import datetime
import csv

# formattednow = now.strftime("%Y/%m/%d %H:%M:%s")
now = datetime.datetime.now()

i = 1

f = open('ducklog.csv', 'a', newline='')
writer = csv.writer(f)

while i == 1:
    Got_him = pyautogui.locateCenterOnScreen("Success.png", grayscale=False, confidence=0.7)
    if Got_him is None:
        print(Got_him)
        continue

    else:
        now = datetime.datetime.now()
        print(Got_him)
        print("OH GOD THERE HE IS")
        print(now)
        writer.writerow(('Success', datetime.datetime.now()))
        time.sleep(5)
        continue

    # i=i+1

# Got_him = pyautogui.locateCenterOnScreen("That Duck.png")
# print(Got_him)
