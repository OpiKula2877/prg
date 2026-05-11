Ax = 0
Ay = 3
Bx = 4
By = 0
def vzdalenostBodu (Ax, Ay, Bx, By) -> float:
    AxBx = abs(Ax - Bx)
    AyBy = abs(Ay - By)
    return (AxBx ** 2 + AyBy ** 2) ** 0.5

def vzdalenostBodu2 (A, B) -> float:
    AxBx = abs(A[0] - B[0])
    AyBy = abs(A[1] - B[1])
    return (AxBx ** 2 + AyBy ** 2) ** 0.5

def vzdalenostBodu3(A, B) -> float:
    AxBx = abs(A["x"] - B["x"])
    AyBy = abs(A["y"] - B["y"])
    return (AxBx ** 2 + AyBy ** 2) ** 0.5

A = {"x": 0, "y": 3}
B = {"x": 4, "y": 0}


print(vzdalenostBodu (Ax, Ay, Bx, By)) 
print(vzdalenostBodu2 ([0, 3], [4, 0]))
print(vzdalenostBodu3({"y": 3, "x": 0}, {"x": 4, "y": 0}))