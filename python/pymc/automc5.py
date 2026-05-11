import pyautogui, keyboard, time, sys
from screeninfo import get_monitors

# --- NASTAVENÍ MONITORU ---
def vyber_monitor():
    monitory = get_monitors()
    print("Nalezené monitory:")
    for i, m in enumerate(monitory):
        print(f"{i}: {m.name} ({m.width}x{m.height}) na pozici [x={m.x}, y={m.y}]")
    
    volba = input("Zadej číslo monitoru, na kterém běží Minecraft: ")
    try:
        vybrany = monitory[int(volba)]
        return vybrany.x, vybrany.y
    except:
        print("Neplatná volba, končím.")
        sys.exit()

offX, offY = vyber_monitor()
# -------------------------

def generate_warps():
    warps = []
    for c1 in 'defghijklmnopqrstuvwxyz': 
        warps.append(f'aa{c1}')
    for c1 in 'abcdefghijklmnopqrstuvw': 
        warps.append(f'ab{c1}')
    return warps

def PNP(check_x, check_y, retry_x=None, retry_y=None):
    # Přidání offsetu monitoru
    real_x = check_x + offX
    real_y = check_y + offY
    
    start_time = time.time()
    druhy_pokus = False 
    
    while True:
        if (pyautogui.pixelMatchesColor(real_x, real_y, (198, 198, 198)) or 
            pyautogui.pixelMatchesColor(real_x, real_y, (170, 0, 0)) or 
            pyautogui.pixelMatchesColor(real_x, real_y, (142, 30, 17))):
            return 
            
        if time.time() - start_time > 5:
            if not druhy_pokus and retry_x is not None:
                print(f"Varování: Bod nenalezen do 5s. Zkouším retry.")
                pyautogui.click(retry_x + offX, retry_y + offY)
                start_time = time.time() 
                druhy_pokus = True      
            else:
                print("chyba: nenašel se bod s uvedenou barvou ani po opakovaném pokusu")
                sys.exit()
                
        time.sleep(0.05)

warps = generate_warps()

print("Čekám na stisk klávesy 4...")
keyboard.wait('4')
print("Spouštím program!")
time.sleep(0.5)

for warp in warps:
    pyautogui.PAUSE = 0.15
    pyautogui.press('t')
    pyautogui.write(f'/warp {warp}')
    pyautogui.press('enter')
    
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    PNP(956, 257) 
    pyautogui.click(797 + offX, 365 + offY)
    PNP(1111, 220, 797, 365)
    pyautogui.click(1123 + offX, 286 + offY)
    PNP(886, 235, 1123, 286)
    pyautogui.click(955 + offX, 552 + offY)
    PNP(900, 359, 955, 552)
    pyautogui.click(1121 + offX, 399 + offY)
    PNP(1111, 220, 1121, 399)
    pyautogui.click(1119 + offX, 288 + offY)
    PNP(886, 235, 1119, 288)
    pyautogui.click(962 + offX, 556 + offY)
    PNP(900, 359, 962, 556)
    pyautogui.click(1124 + offX, 388 + offY)
    PNP(1111, 220, 1124, 388)
    pyautogui.click(959 + offX, 554 + offY)
    PNP(956, 257, 959, 554)
    pyautogui.click(1016 + offX, 472 + offY)
    PNP(955, 297, 1016, 472)
    pyautogui.click(846 + offX, 338 + offY)
    PNP(886, 235, 846, 338)
    pyautogui.click(952 + offX, 544 + offY)
    PNP(900, 359, 952, 544)
    pyautogui.click(1125 + offX, 390 + offY)
    PNP(955, 297, 1125, 390)
    pyautogui.click(855 + offX, 342 + offY)
    PNP(886, 235, 855, 342)
    pyautogui.click(955 + offX, 561 + offY)
    PNP(900, 359, 955, 561)
    pyautogui.click(1064 + offX, 395 + offY)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')

    PNP(1189, 317)
    pyautogui.keyDown('shift')
    pyautogui.click(634 + offX, 416 + offY)
    PNP(1319, 418, 634, 416)
    pyautogui.click(1320 + offX, 427 + offY)
    pyautogui.click(625 + offX, 425 + offY)
    PNP(1319, 418, 625, 425)
    pyautogui.click(1315 + offX, 421 + offY)
    pyautogui.click(619 + offX, 417 + offY)
    PNP(1319, 418, 619, 417)
    pyautogui.click(1310 + offX, 442 + offY)
    pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    PNP(956, 257)
    pyautogui.click(798 + offX, 370 + offY)
    PNP(1111, 220, 798, 370)
    pyautogui.click(1121 + offX, 281 + offY)
    PNP(886, 235, 1121, 281)
    pyautogui.click(957 + offX, 555 + offY)
    PNP(900, 359, 957, 555)
    pyautogui.click(1124 + offX, 393 + offY)
    PNP(1111, 220, 1124, 393)
    pyautogui.click(955 + offX, 552 + offY)
    PNP(956, 257, 955, 552)
    pyautogui.click(1016 + offX, 472 + offY)
    PNP(955, 297, 1016, 472)
    pyautogui.click(848 + offX, 338 + offY)
    PNP(886, 235, 848, 338)
    pyautogui.click(958 + offX, 557 + offY)
    PNP(900, 359, 958, 557)
    pyautogui.click(1122 + offX, 395 + offY)
    PNP(955, 297, 1122, 395)
    pyautogui.click(849 + offX, 339 + offY)
    PNP(886, 235, 849, 339)
    pyautogui.click(957 + offX, 554 + offY)
    PNP(900, 359, 957, 554)
    pyautogui.click(1066 + offX, 390 + offY)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')
    PNP(1189, 317)
    pyautogui.keyDown('shift')
    pyautogui.click(634 + offX, 416 + offY)
    PNP(1319, 418, 634, 416)
    pyautogui.click(1320 + offX, 427 + offY)
    pyautogui.click(625 + offX, 425 + offY)
    PNP(1319, 418, 625, 425)
    pyautogui.click(1315 + offX, 421 + offY)
    pyautogui.click(619 + offX, 417 + offY)
    PNP(1319, 418, 619, 417)
    pyautogui.click(1310 + offX, 442 + offY)
    pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.rightClick()

    PNP(978, 239)
    pyautogui.PAUSE = 0.2
    pyautogui.keyDown('shift')
    pyautogui.click(1128 + offX, 829 + offY)
    pyautogui.click(1063 + offX, 828 + offY)
    pyautogui.click(1018 + offX, 822 + offY)
    pyautogui.click(972 + offX, 824 + offY)
    pyautogui.click(895 + offX, 828 + offY)
    pyautogui.click(852 + offX, 820 + offY)
    pyautogui.keyUp('shift')
    pyautogui.press('esc')
    
    print(f'Hotovo: /warp {warp}')

print("Všechny warpy dokončeny!")