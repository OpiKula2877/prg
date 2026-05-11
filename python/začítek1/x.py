def kalkulace(**kwargs):
    # linecke, rohlicky, hnizda, kokosky, koule
    # 80, 65, 90, 45, 120 / 100 g
    # na vstupu bude počet * 100 g
    x = 0
    y = 0
    if "linecke" and "rohlicky" in kwargs.keys():
        x += 80 * kwargs["linecke"]
        y += 65 * kwargs["rohlicky"]
    return x, y

print(kalkulace(linecke = 10 and rohlicky = 2))
