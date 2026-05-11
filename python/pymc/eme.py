import pyautogui
import keyboard

def proved_akci():
    print("Provádím sekvenci...")
    pyautogui.keyUp('shift')
    pyautogui.moveTo(547, 424) 
    pyautogui.moveTo(1318, 423)  
    pyautogui.keyDown('shift')
    print("Hotovo. Čekám na další stisk...")

print("Program běží.")
print("Zkus stisknout 5 na numerické klávesnici.")
print("Pro ukončení stiskni 'Esc'.")

# Zkusíme nejčastější varianty názvu pro numerickou pětku
try:
    keyboard.add_hotkey('numpad5', proved_akci)
except ValueError:
    # Pokud by numpad5 nefungoval, zkusíme obyčejnou pětku
    keyboard.add_hotkey('5', proved_akci)

# Drží program při životě
keyboard.wait('esc')