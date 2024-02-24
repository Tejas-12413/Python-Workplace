from pyautogui import *
import pyautogui, time, keyboard, random, win32api, win32con


#Tile 1 x:1300, y:630
#Tile 2 x:1400, y:630
#Tile 3 x:1500, y:630
#Tile 4 x:1600, y:630

for i in range(1, 6):
    print(f'Starting in {i}')
    time.sleep(1)


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(1300, 430)[0] == 0:
        click(1300, 430)
    if pyautogui.pixel(1400, 430)[0] == 0:
        click(1400, 430)
    if pyautogui.pixel(1500, 430)[0] == 0:
        click(1500, 430)
    if pyautogui.pixel(1600, 430)[0] == 0:
        click(1600, 430)
