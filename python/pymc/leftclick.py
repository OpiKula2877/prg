import pyautogui
import keyboard
import time

print(f"Program běží. Čekám na stisknutí klávesy '3' na numerice...")

    # Čekání na stisknutí klávesy
keyboard.wait('3')

while True:
    # Stisknutí levého tlačítka
    pyautogui.mouseDown(button='left')

print("Tlačítko uvolněno. Program končí.")