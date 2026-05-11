class elf:

    pocet_elfu = 0

    def __init__(self, jmeno, vyrobek): # To __init__ je konstruktor a zavolá se při vytvoření objektu.
        self.jmeno = jmeno
        self.vyrobek = vyrobek
        elf.pocet_elfu += 1
        print(f"Elf {self.jmeno} začal vyrábět {self.vyrobek}.")

    def __del__(self): # To __del__ je destruktor a zavolá se při zničení objektu.
        elf.pocet_elfu -= 1
        print(f"Elf {self.jmeno} dokončil práci a odešel od stolu.")

    def pracuj(self): # Metoda která se zobrazí, když ho zavoláme.
        print(f"Elf {self.jmeno} pilně vyrábí {self.vyrobek}...")

    def vypis_pocet(self): # Metoda která se zobrazí, když ho zavoláme.
        print(f"V dílně pracuje {elf.pocet_elfu} elfové.")

e1 = elf("Arwen", "dřevěného koníka")
e2 = elf("Borin", "plyšového medvídka")
e3 = elf("Lina", "autíčko")

e1.vypis_pocet()

e2.pracuj()
del e3

e1.vypis_pocet()