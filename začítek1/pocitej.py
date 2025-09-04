def pocitej(**kwargs):
    operace = kwargs.get("operace")
    cisla = kwargs.get("cisla")
    
    if not cisla or not isinstance(cisla, (list, tuple)):
        return "Chyba"
    
    if operace == "prumer":
        return sum(cisla) / len(cisla)
    if operace == "minimum":
        return min(cisla)
    if operace == "maximum":
        return max(cisla)
    else:
        return "Chyba"

print(pocitej(operace="prumer", cisla=[1, 2, 3, 4, 5]))
print(pocitej(operace="minimum", cisla=[1, 2, 3, 4, 5]))
print(pocitej(operace="maximum", cisla=[1, 2, 3, 4, 5]))