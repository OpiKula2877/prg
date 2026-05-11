from abc import ABC, abstractmethod
class Vehicle(ABC):
    
    @abstractmethod
    def whoami(self):
        pass
    
    @abstractmethod
    def max_speed(self, speed):
        pass

    @abstractmethod
    def fuel(self, f):
        pass

# Vytvoř třídu Bugatti jako potomka třídy Vehicle.
# Přepiš abstraktní metody whoami, max_speed a fuel.
