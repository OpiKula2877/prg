import random

# Vytvoření seznamu 100 náhodných čísel od 1 do 100 - pozor, mohou se opakovat
nahodna_cisla = [random.randint(1, 100) for i in range(100)]
# Výpis výsledku
print(nahodna_cisla)

#-----------------------------------------------------------------------------------

# Vytvoření seznamu 100 unikátních náhodných čísel od 1 do 100
nahodna_cisla2 = random.sample(range(1, 101), 100)
# Výpis výsledku
print(nahodna_cisla2)

function_sorted = sorted(nahodna_cisla2)
print(function_sorted)

print(function_sorted[6])