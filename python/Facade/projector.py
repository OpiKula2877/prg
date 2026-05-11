class DVDPlayer:
    """
    Třída reprezentující DVD přehrávač.
    """
    def on(self):
        """Zapne DVD přehrávač."""
        # Simuluje zapnutí DVD přehrávače
        print("DVD Player is ON")
    
    def play(self, movie):
        """Přehraje zadaný film.
        
        Args:
            movie (str): Název filmu.
        """
        # Simuluje přehrávání filmu s názvem `movie`
        print(f"Playing '{movie}'")
    
    def off(self):
        """Vypne DVD přehrávač."""
        # Simuluje vypnutí DVD přehrávače
        print("DVD Player is OFF")

class Projector:
    """
    Třída reprezentující projektor.
    """
    def on(self):
        """Zapne projektor."""
        # Simuluje zapnutí projektoru
        print("Projector is ON")
    
    def set_input(self, source):
        """Nastaví vstup projektoru.
        
        Args:
            source (str): Zdroj signálu.
        """
        # Nastavuje zdroj signálu pro projektor (např. DVD přehrávač)
        print(f"Projector input set to {source}")
    
    def off(self):
        """Vypne projektor."""
        # Simuluje vypnutí projektoru
        print("Projector is OFF")

class SoundSystem:
    """
    Třída reprezentující zvukový systém.
    """
    def on(self):
        """Zapne zvukový systém."""
        # Simuluje zapnutí zvukového systému
        print("Sound System is ON")
    
    def set_volume(self, level):
        """Nastaví hlasitost.
        
        Args:
            level (int): Úroveň hlasitosti.
        """
        # Nastavuje hlasitost zvukového systému na úroveň `level`
        print(f"Volume set to {level}")
    
    def off(self):
        """Vypne zvukový systém."""
        # Simuluje vypnutí zvukového systému
        print("Sound System is OFF")

class Lights:
    """
    Třída reprezentující osvětlení.
    """
    def dim(self, level):
        """Ztlumí světla na požadovanou úroveň.
        
        Args:
            level (int): Úroveň ztlumení v procentech.
        """
        # Nastavuje úroveň ztlumení světel na `level` procent
        print(f"Lights dimmed to {level}%")

class HomeTheaterFacade:
    """
    Fasáda pro ovládání domácího kina.
    """
    def __init__(self, dvd: DVDPlayer, projector: Projector, sound: SoundSystem, lights: Lights):
        """Inicializuje domácí kino.
        
        Args:
            dvd (DVDPlayer): DVD přehrávač.
            projector (Projector): Projektor.
            sound (SoundSystem): Zvukový systém.
            lights (Lights): Osvětlení.
        """
        # Ukládá jednotlivé komponenty domácího kina
        self.dvd = dvd
        self.projector = projector
        self.sound = sound
        self.lights = lights
    
    def watch_movie(self, movie):
        """Připraví domácí kino a spustí film.
        
        Args:
            movie (str): Název filmu.
        """
        # Sekvence kroků pro přípravu a spuštění filmu
        print("Getting ready to watch a movie...")
        self.lights.dim(30)  # Ztlumí světla na 30 %
        self.projector.on()  # Zapne projektor
        self.projector.set_input("DVD Player")  # Nastaví vstup projektoru na DVD přehrávač
        self.sound.on()  # Zapne zvukový systém
        self.sound.set_volume(50)  # Nastaví hlasitost na 50
        self.dvd.on()  # Zapne DVD přehrávač
        self.dvd.play(movie)  # Spustí přehrávání filmu
    
    def end_movie(self):
        """Vypne domácí kino a uvede systém do klidového stavu."""
        # Sekvence kroků pro vypnutí domácího kina
        print("Shutting movie theater down...")
        self.dvd.off()  # Vypne DVD přehrávač
        self.sound.off()  # Vypne zvukový systém
        self.projector.off()  # Vypne projektor
        self.lights.dim(100)  # Rozsvítí světla na 100 %

# Použití facade
if __name__ == "__main__": #Tento kod zde být nemusí
    # Vytvoření instancí jednotlivých komponent domácího kina
    dvd = DVDPlayer()
    projector = Projector()
    sound = SoundSystem()
    lights = Lights()
    
    # Vytvoření instance fasády pro domácí kino
    home_theater = HomeTheaterFacade(dvd, projector, sound, lights)
    
    # Spuštění filmu
    home_theater.watch_movie("Inception")
    print("\n---\n")
    # Ukončení filmu
    home_theater.end_movie()

import tkinter as tk
def on_watch_movie():
    movie_name = movie_entry.get()
    if movie_name.strip():
        home_theater.watch_movie(movie_name)
    else:
        print("Please enter a movie name.")

def on_end_movie():
    home_theater.end_movie()

root = tk.Tk()
root.title("Home Theater Control")
root.geometry("300x300")

movie_label = tk.Label(root, text="Zadejte název filmu:")
movie_label.pack(pady=10)

movie_entry = tk.Entry(root, width=30)
movie_entry.pack(pady=5)

on_button = tk.Button(root, text="ON", command=on_watch_movie)
on_button.pack(pady=10)

off_button = tk.Button(root, text="OFF", command=on_end_movie)
off_button.pack(pady=10)

root.mainloop()