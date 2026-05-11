def soucet(n):
    if n == 0:
        return 0
    else:
        return n + soucet(n - 1)

n = int(input("Zadej nezáporné číslo: "))
print("Součet je:", soucet(n))