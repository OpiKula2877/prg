import pyautogui
import keyboard

print("Stiskni klávesu 'S' pro zobrazení souřadnic myši.")
print("Stiskni ESC pro ukončení programu.")

while True:
    if keyboard.is_pressed('s'):
        x, y = pyautogui.position()
        print(f"Souřadnice myši: X={x}, Y={y}")
        keyboard.wait('s')  # zabrání vícenásobnému výpisu

    if keyboard.is_pressed('esc'):
        print("Ukončuji program.")
        break
