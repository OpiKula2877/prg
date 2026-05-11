from abc import ABC, abstractmethod

class FastFood(ABC):
    
    @abstractmethod
    def accept_order(self, what, deliver_number):
        pass

    @abstractmethod
    def cook(self, what, deliver_number):
        pass
    
    @abstractmethod
    def pack(self, deliver_number):
        pass
    
    @abstractmethod
    def deliver(self, deliver_number):
        pass
    
class KFC(FastFood):
    pass

class McDonald(FastFood):
    pass

class BurgerKing(FastFood):
    pass

