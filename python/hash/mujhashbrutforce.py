import hashlib
import random

hash = "5c4c3d6b1e6c7c0c5a5f9e3c6f4e3c0d"

def genpass():
    password = ""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#$_-"
    for _ in range(12):
        char = random.choice(chars)
        password += char
    return password
    
def frompasstohash(password):
    hashfrompass = "5c4c3d6b1e6c7c0c5a5f9e3c6f4e3c0e" # generování hash z hesla - Nevím jak to udělat jelikož to nevidím na W3Schools
    return hashfrompass

def isitmaching(password, hashfrompass):
    if hash == hashfrompass:
        print("Heslo je " + password)
        return True
    return False

def pokusy(x=1):
    for i in range(x):
        password = genpass()
        hashfrompass = frompasstohash(password)
        if isitmaching(password, hashfrompass):
            break

pokusy(1000000000)

