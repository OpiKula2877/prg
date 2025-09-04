def prumerna_rychlost(draha, cas):
    return draha / cas
draha = float(input("Zadej vzdálenost dráhy v metrech: "))
cas = float(input("Zadej za jak dlouho se dostal na konec: "))
print("Průměrná rychlost je", prumerna_rychlost(draha, cas), "m/s")