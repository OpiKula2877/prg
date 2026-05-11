print("Máme tady rovnici ax + b = 0, doplňte a potom b. Progra Vám vypočítá x.")
a = float(input("Doplňte realnou proměnou pro a: "))
if a == 0:
    print("Pro neznámou x není mnoho řešení.")
else:
    b = float(input("Doplňte realnou proměnou pro b: "))
    x = 0
    x = (a*-1)/b
    print(f"Pro neznámou x je číslo {x}.")