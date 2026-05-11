class Animal:
    def __init__(self, name, sound, weight):
        self.__name = name
        self.__sound = sound
        self.__weight = weight
    
    def getIdentity(self):
        return self.__name
    def getSound(self):
        return self.__sound
    def getWeight(self):
        return self.__weight
    def setIdentity(self, name, sound, weight):
        self.__name = name
        self.__sound = sound
        self.__weight = weight
    def __str__(self):
        return f"Animal: {self.__name}, Sound: {self.__sound}, Weight: {self.__weight}"
vlk = Animal("Vlk", "Hauuu", 45)
print(vlk)

class Dog(Animal):
    def __init__(self, name, sound, weight, kind):
        Animal.__init__(self, name, sound, weight)
        self.__kind = kind

    def __str__(self):
        return super().__str__() + f", \nKind: {self.__kind}"

a=Animal("default","default","default")
print(a)
d = Dog("Alík", "Haf", "12", "Shiba-inu")
print(d)