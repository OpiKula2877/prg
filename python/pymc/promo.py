import pyautogui, keyboard, pyperclip, time

keyboard.wait("9")

def napis_zpravu(text):
    pyautogui.press('t')
    time.sleep(0.1) # Malá pauza, aby se otevřel chat
    pyperclip.copy(text) # Zkopíruje text do schránky
    pyautogui.hotkey('ctrl', 'v') # Vloží text
    pyautogui.press('enter')

# Tvůj text:
napis_zpravu("&2Nejlevnější &ashop &f(+ vykupuji &l&4T&fN&4T&r) &2na &aSkyBlocku :co: &2jedině &ana &4/warp OpiKula.")
napis_zpravu("-----------------------")
napis_zpravu(":ez: &2Slušné peníze :ez: &e+ &8zdarma gunpowder &fdostanete jedině na &4/warp cxp.")
napis_zpravu("-----------------------")
napis_zpravu("&fNa &4/warp exp &6ZADARMO :harold: &fmůžete získat &aemeraldy&f, které v &4/shop &fprodáte.:husty:")