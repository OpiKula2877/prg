import random
cisla = random.sample(range(1,101), 10)
soucet = 0
for cislo in cisla:
    soucet += cislo
print(cisla)
print("Součet čísel v seznamu je: ", soucet)