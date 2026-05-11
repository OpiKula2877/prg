n = float(input("Zadej hodnotu, která se bude mocnit: "))
d = int(input("Zadej hodnotu mocnitele: "))
print(n ** d) #Řešení první
v=1
for x in range(d):
    v *= n
print (v) #Řešení druhé