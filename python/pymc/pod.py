import pyautogui
import keyboard
import time

# Nastavení klávesové zkratky a souřadnic
HOTKEY = 'ctrl+8' 
POZICE_DOLU = (928, 1016)
POZICE_NAHORU = (942, 134)

print(f"Program běží! Zmáčkni '{HOTKEY}' pro akci.")
print("Pro úplné ukončení skriptu zmáčkni Esc.")

def proved_akci():
    # 1. Plynule DOLŮ (0.5 sekundy)
    pyautogui.moveTo(POZICE_DOLU[0], POZICE_DOLU[1], duration=0.5)
    
    # 2. Pauza 0.5 sekundy (podle tvého zadání)
    time.sleep(0.5)
    
    # 3. Hodně RYCHLE plynule NAHORU (0.1 sekundy)
    pyautogui.moveTo(POZICE_NAHORU[0], POZICE_NAHORU[1], duration=0.1)

# Registrace kombinace kláves
keyboard.add_hotkey(HOTKEY, proved_akci)

# Drží program v paměti
keyboard.wait('esc')