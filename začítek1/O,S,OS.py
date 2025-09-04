import math
def kruznice(polomer, operace):
    """Výpočet obsahu, obvodu nebo obojího"""
    pi = math.pi
    pi = 3.14159265358979
    r = polomer
    o = operace  # O, S, OS

polomer = 3
obvod_kruznice = kruznice(polomer, "O")
obsah_kruznice = kruznice(polomer, "S")
obsah_obvod_kruznice = kruznice(polomer, "OS")

