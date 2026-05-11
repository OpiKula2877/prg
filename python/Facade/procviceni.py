class Projektor:
    def zapnout(self):
        print("Projektor je zapnutý.")
    def vypnout(self):
        print("Projektor je vypnutý.")
    def nastavit_vstup(self, vstup):
        print(f"Projektor vstup nastaven na {vstup}.")
class Reproduktory:
    def zapnout(self):
        print("Reproduktory jsou zapnuté.")
    def vypnout(self):
        print("Reproduktory jsou vypnuté.")
    def nastavit_hlasitost(self, hodnota):
        print(f"Hlasitost nastavena na {hodnota}.")
class Plátno:
    def spustit_dolu(self):
        print("Plátno spuštěno dolů.")
    def spustit_nahoru(self):
        print("Plátno spuštěno nahoru.")

class DomaciKino:
    def __init__(self, projektor, reproduktory, platno):
        self.projektor = projektor
        self.reproduktory = reproduktory
        self.platno = platno

    def zapnout_kino(self):
        self.projektor.zapnout()
        self.projektor.nastavit_vstup("HDMI1")
        self.reproduktory.zapnout()
        self.reproduktory.nastavit_hlasitost(69)
        self.platno.spustit_dolu()
        print("Domácí kino je připraveno k použití.")
    def sledovat_video(self):
        self.reproduktory.nastavit_hlasitost(100)
    def vypnout_kino(self):
        self.projektor.vypnout()
        self.reproduktory.vypnout()
        self.platno.spustit_nahoru()
        print("Domácí kino je vypnuto.")

DomK = DomaciKino(Projektor(), Reproduktory(), Plátno())
DomK.zapnout_kino()
print("\n---\n")
DomK.vypnout_kino()