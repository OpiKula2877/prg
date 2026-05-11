import pyautogui, keyboard, time, sys

def generate_warps():
    warps = []
    for c1 in 'abcdefghijklmnopqrstuvwxyz': #abcdefghijklmnopqrstuvwxyz
        warps.append(f'aa{c1}')
    for c1 in 'abcdefghijklmnopqrstuvw': #abcdefghijklmnopqrstuvw
        warps.append(f'ab{c1}')
    return warps

def PNP(check_x, check_y, retry_x=None, retry_y=None):
    pokusy = 1
    max_pokusu = 3
    
    while pokusy <= max_pokusu:
        start_time = time.time()
        # Kontrola barev
        while True:
            if (pyautogui.pixelMatchesColor(check_x, check_y, (198, 198, 198)) or 
                pyautogui.pixelMatchesColor(check_x, check_y, (168, 0, 0)) or 
                pyautogui.pixelMatchesColor(check_x, check_y, (140, 30, 17))):
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
                                    pyautogui.pixelMatchesColor(check_x, check_y, (170, 0, 0)) or 
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

warps = generate_warps()

print("Čekám na stisk klávesy 4...")
keyboard.wait('4')
print("Spouštím program!")
time.sleep(0.5)
for warp in warps:
    pyautogui.PAUSE = 0.1
    pyautogui.press('t')
    pyautogui.write(f'/warp {warp}')
    pyautogui.press('enter')
    
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    PNP(956, 257) #Obchod
    pyautogui.moveTo(798, 365)
    pyautogui.moveTo(797, 365)
    pyautogui.click(797, 365)
    PNP(1111, 220) #Bloky
    pyautogui.moveTo(1124, 286)
    pyautogui.moveTo(1123, 286)
    pyautogui.click(1123, 286)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(956, 552)
    pyautogui.moveTo(955, 552)
    pyautogui.click(955, 552)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1122, 399)
    pyautogui.moveTo(1121, 399)
    pyautogui.click(1121, 399)
    PNP(1111, 220) #Bloky
    pyautogui.moveTo(1120, 288)
    pyautogui.moveTo(1119, 288)
    pyautogui.click(1119, 288)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(963, 556)
    pyautogui.moveTo(962, 556)
    pyautogui.click(962, 556)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1125, 388)
    pyautogui.moveTo(1124, 388)
    pyautogui.click(1124, 388)
    PNP(1111, 220) #Bloky
    pyautogui.moveTo(960, 554)
    pyautogui.moveTo(959, 554)
    pyautogui.click(959, 554)
    PNP(956, 257) #Obchod
    pyautogui.moveTo(1017, 472)
    pyautogui.moveTo(1016, 472)
    pyautogui.click(1016, 472)
    PNP(955, 297) #Mobové
    pyautogui.moveTo(847, 338)
    pyautogui.moveTo(846, 338)
    pyautogui.click(846, 338)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(953, 544)
    pyautogui.moveTo(952, 544)
    pyautogui.click(952, 544)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1126, 390)
    pyautogui.moveTo(1125, 390)
    pyautogui.click(1125, 390)
    PNP(955, 297) #Mobové
    pyautogui.moveTo(856, 342)
    pyautogui.moveTo(855, 342)
    pyautogui.click(855, 342)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(956, 561)
    pyautogui.moveTo(955, 561)
    pyautogui.click(955, 561)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1065, 395)
    pyautogui.moveTo(1064, 395)
    pyautogui.click(1064, 395)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')

    PNP(1189, 317)
    pyautogui.keyDown('shift')

    pyautogui.moveTo(634, 416)
    pyautogui.click(634, 416, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1320, 427)
    pyautogui.click(1320, 427, button='left')
    pyautogui.moveTo(625, 425)
    pyautogui.click(625, 425, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1315, 421)
    pyautogui.click(1315, 421, button='left')
    pyautogui.moveTo(619, 417)
    pyautogui.click(619, 417, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1310, 442)
    pyautogui.click(1310, 442, button='left')
    
    pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/shop')
    pyautogui.press('enter')

    PNP(956, 257) #Obchod
    pyautogui.moveTo(799, 370)
    pyautogui.moveTo(798, 370)
    pyautogui.click(798, 370)
    PNP(1111, 220) #Bloky
    pyautogui.moveTo(1122, 281)
    pyautogui.moveTo(1121, 281)
    pyautogui.click(1121, 281)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(958, 555)
    pyautogui.moveTo(957, 555)
    pyautogui.click(957, 555)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1125, 393)
    pyautogui.moveTo(1124, 393)
    pyautogui.click(1124, 393)
    PNP(1111, 220) #Bloky
    pyautogui.moveTo(956, 552)
    pyautogui.moveTo(955, 552)
    pyautogui.click(955, 552)
    PNP(956, 257) #Obchod
    pyautogui.moveTo(1017, 472)
    pyautogui.moveTo(1016, 472)
    pyautogui.click(1016, 472)
    PNP(955, 297) #Mobové
    pyautogui.moveTo(849, 338)
    pyautogui.moveTo(848, 338)
    pyautogui.click(848, 338)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(959, 557)
    pyautogui.moveTo(958, 557)
    pyautogui.click(958, 557)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1123, 395)
    pyautogui.moveTo(1122, 395)
    pyautogui.click(1122, 395)
    PNP(955, 297) #Mobové
    pyautogui.moveTo(850, 339)
    pyautogui.moveTo(849, 339)
    pyautogui.click(849, 339)
    PNP(886, 235) #Nákup
    pyautogui.moveTo(958, 554)
    pyautogui.moveTo(957, 554)
    pyautogui.click(957, 554)
    PNP(900, 359) #Množství
    pyautogui.moveTo(1067, 390)
    pyautogui.moveTo(1066, 390)
    pyautogui.click(1066, 390)

    pyautogui.press('esc')
    pyautogui.press('t')
    pyautogui.write('/craft')
    pyautogui.press('enter')
    PNP(1189, 317)
    pyautogui.keyDown('shift')

    pyautogui.moveTo(634, 416)
    pyautogui.click(634, 416, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1320, 427)
    pyautogui.click(1320, 427, button='left')
    pyautogui.moveTo(625, 425)
    pyautogui.click(625, 425, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1315, 421)
    pyautogui.click(1315, 421, button='left')
    pyautogui.moveTo(619, 417)
    pyautogui.click(619, 417, button='left')
    PNP(1319, 418)
    pyautogui.moveTo(1310, 442)
    pyautogui.click(1310, 442, button='left')
    
    pyautogui.keyUp('shift')

    pyautogui.press('esc')
    pyautogui.rightClick()

    PNP(978, 239)
    pyautogui.PAUSE = 0.01
    pyautogui.moveTo(1128, 829)
    pyautogui.keyDown('shift')
    pyautogui.click(1128, 829, button='left')
    pyautogui.keyUp('shift')
    pyautogui.moveTo(1063, 828)
    pyautogui.keyDown('shift')
    pyautogui.click(1063, 828, button='left')
    pyautogui.keyUp('shift')
    pyautogui.moveTo(1018, 822)
    pyautogui.keyDown('shift')
    pyautogui.click(1018, 822, button='left')
    pyautogui.keyUp('shift')
    pyautogui.moveTo(972, 824)
    pyautogui.keyDown('shift')
    pyautogui.click(972, 824, button='left')
    pyautogui.keyUp('shift')
    pyautogui.moveTo(895, 828)
    pyautogui.keyDown('shift')
    pyautogui.click(895, 828, button='left')
    pyautogui.keyUp('shift')
    pyautogui.moveTo(852, 820)
    pyautogui.keyDown('shift')
    pyautogui.click(852, 820, button='left')
    pyautogui.keyUp('shift')
    pyautogui.press('esc')
    
    print(f'Hotovo: /warp {warp}')

print("Všechny warpy dokončeny!")