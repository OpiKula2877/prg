def vstupenka(det, dos, sen):
    cena = 0
    cena += det * 85
    cena += dos * 150
    cena += sen * 70
    if cena < 1000:
        return cena
    else:
        return cena * 0.8

det = int(input("Zadej pocet lístků pro dítě: "))
dos = int(input("Zadej pocet lístků pro dospělého: "))
sen = int(input("Zadej pocet lístků pro seniora: "))
print ("Celková cena je ", vstupenka(det, dos, sen), " kč.")