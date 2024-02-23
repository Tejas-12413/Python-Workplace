import pyautogui as pg
from time import sleep

n = int(input("Number of entries  :"))
a = str(input("String : "))
for i in range(-5, 0):
	print(f"Starting in {abs(i)}"); sleep(1)
for i in range(1, n):
        pg.write(a)
        if i != n:
                pg.press('enter')
