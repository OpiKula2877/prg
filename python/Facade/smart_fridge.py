class SmartFridge:
    BeerNumber = 6
    Money = 250

    def __init__(self):
        self.give_me_beer = self.GiveMeBeer()
        self.what_i_have = self.WhatIHave()
        self.order_some_beer = self.OrderSomeBeer()
        self.mine_crypto = self.MineCrypto()

    def execute_command(self, command):
        if command == "GetMeBeer":
            self.give_me_beer.execute_command()
        elif command == "WhatIHave":
            self.what_i_have.execute_command()
        elif command == "OrderSomeBeer":
            self.order_some_beer.execute_command()
        elif command == "MineCrypto":
            self.mine_crypto.execute_command()
        else:
            print("Unknown command.")

    class GiveMeBeer:
        def execute_command(self):
            if SmartFridge.BeerNumber >= 0:
                HowMuchBeer = float(input("How many liters of beer do you want? "))
                if HowMuchBeer <= SmartFridge.BeerNumber or HowMuchBeer == SmartFridge.BeerNumber:
                    SmartFridge.BeerNumber -= HowMuchBeer
                    print("Beer is cooling...")
                    print("Beer is pouring...")
                    print("Beer is ready! Enjoy!")
                else:
                    print("Not enough beer in the fridge!")
            else:
                print("Not enough beer in the fridge!")

    class WhatIHave:
        def execute_command(self):
            print(f"You have {SmartFridge.BeerNumber} liters of beer in the fridge.")

    class OrderSomeBeer:
        def execute_command(self):
            print(f"The current price of beer is 50 CZK per liter.\nYou have {SmartFridge.Money} CZK.")
            yes_no = input("Do you want to order some beer? (Yes/No): ")
            if yes_no.lower() == "yes":
                how_many = float(input("How many liters do you want to order: "))
                if SmartFridge.Money >= how_many * 50:
                    SmartFridge.BeerNumber += how_many
                    SmartFridge.Money -= how_many * 50
                    print(f"You have ordered {how_many} liters of beer.\nYou have {SmartFridge.Money} CZK left.")
                else:
                    print(f"You don't have enough money to order that much beer. :(\nYou are short by {how_many * 50 - SmartFridge.Money} CZK.")
            else:
                print("Order canceled.")

    class MineCrypto:
        def execute_command(self):
            print("Mining cryptocurrency... This may take a while.")
            print("One Missisippi...")
            print("Two Missisippi...")
            print("Three Missisippi...")
            YesNo2 = input("Done! Do you want to sell your mined cryptocurrency? (Yes/No): ")
            if YesNo2 == "Yes":
                print("Selling cryptocurrency...")
                print("Done! You earned 200 CZK from selling your mined cryptocurrency.")
                SmartFridge.Money += 200
                print (f"You now have {SmartFridge.Money} CZK.")
            else:
                print("You decided not to sell your mined cryptocurrency.")
                print("Someone stole your mined cryptocurrency while you were deciding. You lost your crypto.")

fridge = SmartFridge()
while True:
    command = input("Enter command (GetMeBeer, WhatIHave, OrderSomeBeer, MineCrypto, Exit): ")

    if command == "Exit":
        break
    fridge.execute_command(command)