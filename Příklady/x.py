decimal_number = int(input("Zadejte číslo v desítkové soustavě: "))

binary_number = ""  
number = decimal_number  

while number > 0:
    remainder = number % 2  
    binary_number = str(remainder) + binary_number  
    number = number // 2  

print(f"Číslo {decimal_number} v dvojkové soustavě je: {binary_number}")