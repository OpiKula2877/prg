import pyautogui
import keyboard
import time
import sys

# Nastavení kláves
START_KEY = '4'  # Klávesa pro spuštění
STOP_KEY = '5'   # Klávesa pro ukončení

print(f"Program je připraven.")
print(f"1. Zmáčkni {START_KEY} pro SPUŠTĚNÍ")
print(f"2. Zmáčkni {STOP_KEY} pro UKONČENÍ")

# Čekání na startovní klávesu
keyboard.wait(START_KEY)
print("--- PROGRAM SPUŠTĚN (běží smyčka) ---")

try:
    while True:
        # Okamžitá kontrola ukončení na začátku cyklu
        if keyboard.is_pressed(STOP_KEY):
            break

        # Stiskni pravé tlačítko
        pyautogui.mouseDown(button='right')
        
        # Držení po dobu 1 sekundy s průběžnou kontrolou klávesy STOP
        for _ in range(10):
            time.sleep(0.1)
            if keyboard.is_pressed(STOP_KEY):
                pyautogui.mouseUp(button='right')
                print("Program ukončen (přes klávesu 5).")
                sys.exit()

        # Pusť pravé tlačítko
        pyautogui.mouseUp(button='right')
        
        # Krátká pauza před dalším stisknutím
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram přerušen.")
finally:
    pyautogui.mouseUp(button='right')
    print("Všechna tlačítka uvolněna. Nashledanou!")