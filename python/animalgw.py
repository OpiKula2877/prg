class Animal:
    
    def __init__(self, name, sound, weight):        
        self.__name = name
        self.__sound = sound
        self.__weight = weight
        
    def __str__(self):
        return self.__name + ", " + self.__sound + ", " + str(self.__weight)
    
    def makeSound(self):
        return self.__sound
    
class Dog(Animal):
    
    def __init__(self, name, sound, weight, kind):
        Animal.__init__(self, name, sound, weight)
        self.__kind = kind
        
    def __str__(self):
        return super().__str__() + "\nHi, I am dog."
        
   
a = Animal("default", "default", 0)
print(a)
print(a.makeSound())

d = Dog("Alík", "Hafinky haf.", 12, "Shiba-Inu")
print(d)
print(d.makeSound())
