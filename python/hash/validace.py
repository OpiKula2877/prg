import hashlib

# hodnotí délku hesla, 0 pro méně než 8 znaků, 1 pro 8-11 znaků, 2 pro 12 a více znaků
def charsAmount(password): 
    pwd_len = len(password)
    return 0 if pwd_len < 8 else 1 if pwd_len < 12 else 2 # vrací 0 (méně než 8), 1 (8-11) nebo 2 (12 a více) podle délky hesla

# hodnotí přítomnost malých písmen, 2 pokud heslo obsahuje, jinak 0
def hasLower(password):
    return 2 if any(c.islower() for c in password) else 0 

# hodnotí přítomnost velkých písmen, 2 pokud heslo obsahuje, jinak 0
def hasUpper(password):
    return 2 if any(c.isupper() for c in password) else 0 

# hodnotí přítomnost číslic, 2 pokud heslo obsahuje, jinak 0
def hasDigit(password):
    return 2 if any(c.isdigit() for c in password) else 0 

# hodnotí přítomnost speciálních znaků, 2 pokud heslo obsahuje, jinak 0
def hasSpecial(password): 
    special_chars = "~@#$_-"
    return 2 if any(c in special_chars for c in password) else 0

# hodnotí opakování znaků, vrací 2 pro méně než 3 opakování, 1 pro přesně 3 a 0 pro více než 3
def repeatedCharsScore(password): 
    max_repeat = 1
    current = 1

    for i in range(1, len(password)):
        if password[i] == password[i - 1]:
            current += 1
            max_repeat = max(max_repeat, current)
        else:
            current = 1

    return 2 if max_repeat < 3 else 1 if max_repeat == 3 else 0

# kombinuje všechny faktory a vrací celkové hodnocení síly hesla podle zadání (0 pro slabé, 1 pro střední, 2 pro silné)
def calculateStrength(password): 
    return min(
        charsAmount(password),
        min(hasLower(password),
            hasUpper(password),
            hasDigit(password),
            hasSpecial(password)
        ),
        repeatedCharsScore(password)
    )
    
pswd = str(input("Zadejte heslo: "))
strength = calculateStrength(pswd) 
print(f"Síla hesla: "+ ("Slabé" if strength == 0 else "Střední" if strength == 1 else "Silné"))