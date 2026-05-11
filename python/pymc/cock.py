import pyautogui
import keyboard
import sys

def ziskej_barvu_pixelu():
    try:
        # Vstup od uživatele
        vstup = input("Zadej souřadnice x, y (např. 886, 235): ")
        x_str, y_str = vstup.split(',')
        x, y = int(x_str.strip()), int(y_str.strip())
        
        print(f"\nNastaven bod: [{x}, {y}]")
        print("Nyní čekám, až stiskneš '2' na numerické klávesnici...")

        # Čekání na stisk klávesy '2' na numpadu
        # '98' je scan kód pro numpad 2, '2' funguje obecně
        keyboard.wait('2')

        # Získání barvy pixelu
        # screenshot() vytvoří snapshot a getpixel() vytáhne barvu
        barva = pyautogui.screenshot().getpixel((x, y))

        print("-" * 30)
        print(f"Výsledek pro bod [{x}, {y}]:")
        print(f"RGB: {barva}")
        print("-" * 30)

    except ValueError:
        print("Chyba: Zadej souřadnice ve správném formátu (např. 800, 600).")
    except Exception as e:
        print(f"Nastala chyba: {e}")

if __name__ == "__main__":
    ziskej_barvu_pixelu()