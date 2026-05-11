import pyautogui, keyboard, time, sys

def PNP(check_x, check_y, retry_x=None, retry_y=None):
    pokusy = 1
    max_pokusu = 3
    
    while pokusy <= max_pokusu:
        start_time = time.time()
        # Kontrola barev
        while True:
            if (pyautogui.pixelMatchesColor(check_x, check_y, (1,1,1)) or 
                pyautogui.pixelMatchesColor(check_x, check_y, (0, 0, 170)) or 
                pyautogui.pixelMatchesColor(check_x, check_y, (170, 0, 0))):
                return # Barva nalezena, úspěch!
            
            # Pokud uběhlo 5s a barva nikde
            if time.time() - start_time > 5:
                if retry_x is not None and pokusy < max_pokusu:
                    def PNP(check_x, check_y, retry_x=None, retry_y=None):
                        pokusy = 1
                        max_pokusu = 3
                        
                        while pokusy <= max_pokusu:
                            start_time = time.time()
                            while True:
                                if (pyautogui.pixelMatchesColor(check_x, check_y, (198, 198, 198)) or 
                                    pyautogui.pixelMatchesColor(check_x, check_y, (0, 0, 170)) or 
                                    pyautogui.pixelMatchesColor(check_x, check_y, (142, 30, 17))):
                                    return True
                                
                                if time.time() - start_time > 5:
                                    if retry_x is not None and pokusy < max_pokusu:
                                        print(f"Varování: Bod nenalezen (Pokus {pokusy}/{max_pokusu}). Zkouším znovu kliknout na [{retry_x}, {retry_y}]")
                                        pyautogui.click(retry_x, retry_y)
                                        pokusy += 1
                                        break
                                    else:
                                        return False
                                
                                time.sleep(0.05)
                else:
                    print(f"CHYBA: Bod nenalezen ani po {max_pokusu} pokusech. Vypínám.")
                    sys.exit()
            
            time.sleep(0.05)
while True:
    keyboard.wait('4')
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')
    PNP(822, 261)
    pyautogui.moveTo(1069, 419)
    PNP(757, 253)
    pyautogui.moveTo(795, 315)
    PNP(823, 226)
    pyautogui.moveTo(965, 549)
    PNP(790, 348)
    pyautogui.moveTo(1184, 395)
    pyautogui.press('esc')