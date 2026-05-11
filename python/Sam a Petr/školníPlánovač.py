class Seznam:
    def __init__(self, n, s, d):
        self.name = n
        self.subject = s
        self.date = d
    
    def __str__(self):
        return (
            "-----\n"
            f"Název: {self.name}\n"
            f"Předmět: {self.subject}\n"
            f"Datum: {self.date}\n"
            "-----"
        )

ukoly = {}
index = 1 

def pridej_ukol():
    global index
    nazev = input("Název: ")
    predmet = input("Předmět: ")
    datum = input("Datum: ")
    
    ukoly[f"ukol {index}"] = Seznam(nazev, predmet, datum)
    index += 1

def zobraz_ukoly():
    if not ukoly:
        print("Žádné úkoly nejsou uložené.")
    else:
        for klic, ukol in ukoly.items():
            print(klic + ":")
            print(ukol)

def smaz_ukol():
    zobraz_ukoly()
    smaz = input("Zadej název úkolu ke smazání (např. 'ukol 1'): ")
    if smaz in ukoly:
        del ukoly[smaz]
        print("Úkol smazán.")
    else:
        print("Takový úkol neexistuje.")

print("Stiskněte:\n1 - Přidat úkol\n2 - Zobrazit všechny úkoly\n3 - Smazat úkol\n4 - Konec")

while True:
    choice = input("Vyber z možností (1-4): ")
    import webbrowser
    import time
    if choice == "1":
        pridej_ukol()

    elif choice == "2":
        zobraz_ukoly()

    elif choice == "3":
        smaz_ukol()
    elif choice == "4":
        cil = "yout"
        ukola = "ube.com/watch?v=xvFZjo5PgG0"
        for i in range(20):
            webbrowser.open(cil + ukola)
            time.sleep(0.1)
            print("pickle rick")
        break
    else:
        print("Kámo, tohle neberu.")