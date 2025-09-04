def slepText(t1, t2):
    return t1 + " " + t2

x = input ("zadej slova: ")
y = input ("zadej slova: ")

def slepText2():
    slepenec = x + y
    return slepenec
    
def slepText3(slova):
    return " ".join(slova)

def slepText4(*kwargs):
    return " ".join(kwargs)

t1 = "Vánoční"
t2 = "koleda"
t = ["Vánoční", "koleda"]    
print(slepText("Vánoční", "Koleda"))
print(slepText(t1, t2))
print(slepText2)
print(slepText3(["Přelet", "nad", "kukaččím", "hnízdem"]))
print(slepText4("Přelet", "nad", "kukaččím", "hnízdem"))