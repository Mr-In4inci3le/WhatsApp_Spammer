import pyautogui
import time
time.sleep(6)
text = "Stupid , This Is A test for my new reel" #YOUR MESSAGE HERE
for _ in range(0,200):
    pyautogui.typewrite(text)
    pyautogui.press('enter') # AFTER RUNNING THE SCRIPT OPEN YOUR WEB AND HIT ENTER ON WHOM YOU WANT TO SEND
