class dog:

    count = 0
    suma = 0

    def __init__(self, name, age, race, price):
        self.name = name
        self.age = age
        self.race = race
        self.price = price
        dog.count += 1
        dog.price = price
    
    def __del__(self):
        dog.count -= 1

shiba_inu = dog("Shazam", 1, "Shiba Inu", 15000)
shi_tzu = dog("Bobeš", 3, "Shitzu", 9000)
print(shiba_inu.age)
print(dog.count)
del shiba_inu
print(dog.count)