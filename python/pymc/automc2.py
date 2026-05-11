import pyautogui
import keyboard
import time

# Nastavení pauzy mezi příkazy (ponecháno tvých 0.5s)
pyautogui.PAUSE = 0.5

def spustit_obchodování():
    print("Spouštím sekvenci...")
    
    # --- TVŮJ KÓD ZAČÍNÁ ZDE ---
    pyautogui.PAUSE = 0.25
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    pyautogui.moveTo(797, 365)
    pyautogui.click(797, 365)

    pyautogui.moveTo(1123, 286)
    pyautogui.click(1123, 286)

    pyautogui.moveTo(955, 552)
    pyautogui.click(955, 552)

    pyautogui.moveTo(1121, 399)
    pyautogui.click(1121, 399)

    pyautogui.moveTo(1119, 288)
    pyautogui.click(1119, 288)

    pyautogui.moveTo(962, 556)
    pyautogui.click(962, 556)

    pyautogui.moveTo(1124, 388)
    pyautogui.click(1124, 388)

    pyautogui.moveTo(959, 554)
    pyautogui.click(959, 554)

    pyautogui.moveTo(1016, 472)
    pyautogui.click(1016, 472)

    pyautogui.moveTo(846, 338)
    pyautogui.click(846, 338)

    pyautogui.moveTo(952, 544)
    pyautogui.click(952, 544)

    pyautogui.moveTo(1125, 390)
    pyautogui.click(1125, 390)

    pyautogui.moveTo(855, 342)
    pyautogui.click(855, 342)

    pyautogui.moveTo(955, 561)
    pyautogui.click(955, 561)

    pyautogui.moveTo(1064, 395)
    pyautogui.click(1064, 395)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')

    # Shift-click sekvence 1
    for x, y in [(634, 416), (1320, 427), (625, 425), (1315, 421), (619, 417), (1310, 442)]:
        pyautogui.moveTo(x, y)
        pyautogui.keyDown('shift')
        pyautogui.click(x, y, button='left')
        pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    pyautogui.moveTo(798, 370)
    pyautogui.click(798, 370)

    pyautogui.moveTo(1121, 281)
    pyautogui.click(1121, 281)

    pyautogui.moveTo(957, 555)
    pyautogui.click(957, 555)

    pyautogui.moveTo(1124, 393)
    pyautogui.click(1124, 393)

    pyautogui.moveTo(955, 552)
    pyautogui.click(955, 552)

    pyautogui.moveTo(1016, 472)
    pyautogui.click(1016, 472)

    pyautogui.moveTo(848, 338)
    pyautogui.click(848, 338)

    pyautogui.moveTo(958, 557)
    pyautogui.click(958, 557)

    pyautogui.moveTo(1122, 395)
    pyautogui.click(1122, 395)

    pyautogui.moveTo(849, 339)
    pyautogui.click(849, 339)

    pyautogui.moveTo(957, 554)
    pyautogui.click(957, 554)

    pyautogui.moveTo(1066, 390)
    pyautogui.click(1066, 390)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')

    # Shift-click sekvence 2
    for x, y in [(634, 416), (1320, 427), (625, 425), (1315, 421), (619, 417), (1310, 442)]:
        pyautogui.moveTo(x, y)
        pyautogui.keyDown('shift')
        pyautogui.click(x, y, button='left')
        pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.rightClick()

    # Závěrečná Shift-click sekvence
    for x, y in [(1120, 738), (1071, 739), (1017, 738), (971, 735), (913, 735), (844, 730)]:
        pyautogui.moveTo(x, y)
        pyautogui.keyDown('shift')
        pyautogui.click(x, y, button='left')
        pyautogui.keyUp('shift')
    
    # --- TVŮJ KÓD KONČÍ ZDE ---
    print("Hotovo! Čekám na další zmáčknutí Numpad 1...")

# Hlavní smyčka programu
# Nahraď úplný konec skriptu tímto:
print("Program připraven. Zmáčkni '1' pro start.")
while True:
    # Čeká na jakoukoli klávesu 1
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == '1':
        spustit_obchodování()
    time.sleep(0.1)