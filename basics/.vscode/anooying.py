import random
import pyautogui as pg
import time
animal=('HUccha','kunni','GAY')
time.sleep(8)
for i in range(100):
    a=random.choice(animal)
    pg.write("you are a "+a)
    pg.press('ENter')