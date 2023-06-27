import time
import pyautogui as pag
import getch
import os
from datetime import datetime

#Directry change
current_file_path = os.path.realpath(__file__)
script_directory = os.path.dirname(current_file_path)
os.chdir(script_directory)

#Today
today = datetime.now()
str_today_date = today.strftime('%d-%m-%Y')

def screenshotter(w, h):
    print()
    print('Starting program...\nPress "q" for screenshot or "k" to exit program.')
    print()
    num = -1
    while True:
        key = getch.getch()
        if key == 'q':
            num += 1
            x, y = pag.position()
            pag.screenshot(f'screens/img_{str(num)}_{str_today_date}.png', (x, y, w, h))
            print(f"Click! Screenshot saved to defined path!")
        elif key == 'k':
            print("Exiting program...")
            break
        else:
            time.sleep(0.01)


if __name__ == "__main__":
    w = int(input("Enter width[px]: "))
    h = int(input("Enter height[px]: "))
    screenshotter(w, h)
