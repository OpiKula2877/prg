def posunX(bod, posun_X) -> list:
    return [bod[0] + posun_X, bod[1]]

def posunY(bod, posun_Y) -> list:
    return [bod[0], bod[1] + posun_Y]

A = [3, 7]
B = posunX(A, -2)
print(B)

C = posunY(A, -5)
print(C)
