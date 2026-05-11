## Úkol č.1
cisla = [5,3,8,2,10]
soucet = 0
for i in range (len(cisla)):
    soucet = soucet + cisla[i]
print(soucet)

## Úkol č.2 A
cisla = [12, 7, 22, 30, 9]
nejvetsi = 0
for n in range (100):
    for i in range (len(cisla)):
        if cisla[i] > n:
            nejvetsi = cisla[i]
print(nejvetsi)

cisla = [12, 7, 22, 30, 9]
nejmensi = 0
for n in range (100, 1, -1):
    for i in range (len(cisla)):
        if cisla[i] < n:
            nejvetsi = cisla[i]
print(nejvetsi)

## Úkol č.2 B
print(min(cisla))
print(max(cisla))

## Úkol č.3
cisla = [4, 7, 2, 9, 10, 15, 8]
sudy = 0
liche = 0
for i in range (len(cisla)):
    if cisla[i] %2==0:
        sudy += 1
    else:
        liche += 1
print(f"Sudých čísel je {sudy}")
print(f"Lichých čísel je {liche}")

## Úkol č.4
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