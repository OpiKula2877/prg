# Třída Cook slouží jako "fasáda" (Facade), která zjednodušuje práci s více třídami (Cutter, Boiler, Frier).
# Fasáda je návrhový vzor, který poskytuje jednotné rozhraní pro složitý systém.
class Cook:
    '''Class Facade '''
    def __init__(self):
        # Konstruktor (__init__) inicializuje tři "podtřídy" (Cutter, Boiler, Frier).
        # Tyto třídy představují jednotlivé kroky přípravy jídla.
        self.__cutter = Cutter()  # Třída pro krájení zeleniny
        self.__boiler = Boiler()  # Třída pro vaření zeleniny
        self.__frier = Frier()    # Třída pro smažení zeleniny
    
    # Metoda prepareDish kombinuje všechny kroky přípravy jídla.
    def prepareDish(self):
        # Zavolá metodu na krájení zeleniny
        result = self.__cutter.cutVegetables()
        # Přidá výsledek vaření zeleniny
        result += self.__boiler.boilVegetables()
        # Přidá výsledek smažení zeleniny
        result += self.__frier.fry()
        # Vrátí kompletní zprávu o přípravě jídla
        return result

# Třída Cutter představuje "podtřídu" pro krájení zeleniny.
class Cutter:
    ''' Subsystem class Cutter '''    
    # Metoda cutVegetables vrací zprávu, že zelenina byla nakrájena.
    def cutVegetables(self):
        return "All vegetables are chopped."

# Třída Boiler představuje "podtřídu" pro vaření zeleniny.
class Boiler:
    ''' Subsystem class Boiler ''' 
    # Metoda boilVegetables vrací zprávu, že zelenina byla uvařena.
    def boilVegetables(self):
        return "All vegetables are boiled."

# Třída Frier představuje "podtřídu" pro smažení zeleniny.
class Frier:
    ''' Subsystem class Frier ''' 
    # Metoda fry vrací zprávu, že zelenina byla smíchána a osmažena.
    def fry(self):
        return "All vegetables are mixed and fried."

# Klientský kód (zákazník) vytvoří instanci třídy Cook a zavolá metodu prepareDish.
# Tím se spustí všechny kroky přípravy jídla.
cook_it = Cook()
cook_it.prepareDish()