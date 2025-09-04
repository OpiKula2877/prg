x=[1,2,3,4,5,6]
x.remove(5)
print(x)


y = int(input("dej číslo do kolika se bude počítat: "))
# Vytvoříme seznam s čísly od 0 do 100
pole = list(range(y + 1))

# Vypíšeme každý druhý prvek
for i in range(0, len(pole), 1):
   print(pole[i])





# Vytvoříme seznam s čísly od 0 do 100
pole = [i for i in range(101)]

# Vytvoříme nový seznam obsahující každý druhý prvek
druhe_prvky = [pole[i] for i in range(0, len(pole), 2)]

# Vypíšeme všechny prvky najednou
for prvek in druhe_prvky:
   print(prvek)