import random
tocislo = random.randint(1, 100)
print(tocislo)
pokus = 0
pokusy = []
while True:
    tip = int(input(f"Zde zadej svůj tip, jaké by tam mohlo být číslo (pokus číslo {pokus}): "))
    pokus = pokus + 1
    pokusy.append(tip)
    if tip == tocislo:
        print("Vyhrál jsi, gratuluji.")
        print(f"Pokusů bylo {pokus}.")
        print(pokusy)
        break
    elif tip > tocislo:
        print(f"Neznámé číslo je menší, jak {tip}")
    elif tip < tocislo:
        print(f"Neznámé číslo je větší, jak {tip}")