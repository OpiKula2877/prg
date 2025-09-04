vyska = int(input("Zadejte výšku stromku (v počtu řad): "))

ozdoby = 0
for rada in range(1, vyska + 1):
    ozdoby = ozdoby + 2 ** (rada - 1)

print(f"Celkový počet ozdob: {ozdoby}")

druhy = (int(input("Zadejte počet cukroví: ")))
doby = (int(input("Zadejte dobu jednotlivého pečení: ")))
cas = 0

