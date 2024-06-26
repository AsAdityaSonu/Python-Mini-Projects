# Auto Click on the screen at regular intervals

import pyautogui
import time

def auto_click(inter, dur):
    end = time.time() + dur

    while time.time() < end:
        pyautogui.click()
        time.sleep(inter)

def main():
    print("Shuru hoja..")
    auto_click(inter=5, dur=10000000000000)
    print("Aapna safar bas yahi tak tha...")

if __name__ == "__main__":
    main()
