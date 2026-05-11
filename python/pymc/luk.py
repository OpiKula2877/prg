import pyautogui
import keyboard
import time

print("Skript je aktivní a začne hned pracovat.")
print("Pro OKAMŽITÉ UKONČENÍ stiskni 'Numpad 5'.")

try:
    while True:
        # Kontrola stisku klávesy na začátku cyklu
        if keyboard.is_pressed('num 5'):
            break

        # Stiskne a drží pravé tlačítko
        pyautogui.mouseDown(button='right')
        
        # Místo jednoho dlouhého sleepu budeme kontrolovat klávesu po malých kouscích
        # aby byla reakce na vypnutí okamžitá
        for _ in range(10): 
            time.sleep(0.01)
            if keyboard.is_pressed('num 5'):
                pyautogui.mouseUp(button='right') # Pustit tlačítko před ukončením
                print("Ukončeno uživatelem.")
                exit()

        # Pustí pravé tlačítko
        pyautogui.mouseUp(button='right')
        
        # Malá pauza před dalším držením (opět s kontrolou klávesy)
        if keyboard.is_pressed('num 5'):
            break

except KeyboardInterrupt:
    pass

print("Program byl ukončen.")