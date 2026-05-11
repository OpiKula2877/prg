from abc import ABC, abstractmethod

class Operation(ABC):
    
    @abstractmethod
    def calculate(self, *args):
        """
        Abstraktní metoda: musí být implementována v potomcích.
        *args = libovolný počet vstupních hodnot (jako tuple)
        """
        pass

class Sum(Operation):
    
    def calculate(self, *args):
        """
        Sečte všechny zadané číselné hodnoty.
        Např.: calculate(1, 2, 3) → 6
        """
        return sum(args)  # vestavěná funkce sum() sečte vše v iterable (např. tuple)

class Multiply(Operation):
    
    def calculate(self, *args):
        """
        Vynásobí všechny zadané hodnoty.
        Např.: calculate(2, 3, 4) → 24
        """
        result = 1
        for num in args:
            result *= num
        return result

sum_obj = Sum()
mul_obj = Multiply()

print(sum_obj.calculate(1, 3, 5, 0.1))
print(mul_obj.calculate(1, 3, 5, 0.1))