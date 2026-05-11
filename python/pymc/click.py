import keyboard
import pyautogui
import sys
from PIL import Image

KLAVESA_1 = '1' 
KLAVESA_2 = '2'
KLAVESA_3 = '3'

def vypis_souradnice_a_barvu():
    x, y = pyautogui.position()
    barva = pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))
    print(f"Souřadnice: x={x}, y={y} | Kód: pyautogui.moveTo({x}, {y}) | Barva (RGB): {barva}")

def napis_xxx():
    pyautogui.write("XXX")
    print("Napsáno: XXX")

print(f"Program běží! (Použij klávesy {KLAVESA_1}, {KLAVESA_2} na Numpadu)")
print(f"Klávesa {KLAVESA_3} program ukončí.")

try:
    keyboard.add_hotkey(KLAVESA_1, vypis_souradnice_a_barvu)
    keyboard.add_hotkey(KLAVESA_2, napis_xxx)
    keyboard.wait(KLAVESA_3)
except ValueError as e:
    print(f"\nCHYBA: Klávesa nebyla rozpoznána. Zkus ji v kódu přejmenovat.")
    print(f"Detaily chyby: {e}")

print("Program ukončen.")
sys.exit()
