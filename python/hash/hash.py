import hashlib
import random

hash = "5c4c3d6b1e6c7c0c5a5f9e3c6f4e3c0d" # MD5 hash hesla

def generatePassword():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~@#$_-"
    password = ""
    for _ in range(12):
        password += random.choice(chars)
    return password
    print(password)

def hashPassword(password):
    return hashlib.md5(password.encode()).hexdigest()

def compareHash(generatedHash, targetHash):
    return generatedHash == targetHash

def main(amount = 1000):
    global hash
    for i in range(amount): # každý krok iterace je jeden brute-force pokus
        password = generatePassword() # vygeneruje náhodné heslo
        generatedHash = hashPassword(password) # vygeneruje hash z vygenerovaného hesla
        if compareHash(generatedHash, hash): # porovná vygenerovaný hash s cílovým hashem
            print(f"Heslo je {password}")  
            return True
    print("Brute útok nebyl úspěšný") 
    return False

main(1000000000) # spustí hlavní funkci s nastavením počtu pokusů na 1 milion