# with open ("Prueba_exe.txt", mode='+w') as file:
#     file.write("Test file save")

import pyautogui
from random import randint
import time


program = True


answer = input("Please type Password: ")

if answer != 'KeyCode2023&':
    program = False


while program:

    time.sleep(randint(1, 8))

    pyautogui.moveTo(randint(100, 500), randint(100, 500))


    if randint(1, 15) == 1:
        pyautogui.drag(30, 0, 2, button='right')
        continue


    if randint(1, 11) == 1:
        pyautogui.click()
        continue
    

    if randint(1, 10) == 1:
        pyautogui.press('shift')
        continue
    

    if randint(1, 10) == 1:
        pyautogui.press('ctrl')
        continue


    if randint(1, 10) == 1:
        pyautogui.press('esc')
        continue

    
       







