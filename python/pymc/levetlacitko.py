import pyautogui
import keyboard as kb
import time

# Čeká 5 sekund, abys měl čas se přepnout do okna, kde chceš klikat
time.sleep(5) 

while True:
    # Přidány závorky (), aby se kliknutí provedlo
    pyautogui.rightClick()
    time.sleep(0.05)
    pyautogui.leftClick() 
    time.sleep(0.005)
    # Krátká pauza mezi kliknutími
    
    # Bonus: Tip jak to bezpečně vypnout
    if kb.is_pressed('q'): # Podrž 'q' pro ukončení
        break