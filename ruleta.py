import random
import os

black = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
zero = [0]

money = 100

r = "\033[41m"
b = "\033[40m"
g = "\033[42m"
a = "\033[0m"

"""Print roulette table"""
def print_roulette():
     def colorize(number):
          if number in black:
               return f"{b} {number:2} {a}"
          elif number in red:
               return f"{r} {number:2} {a}"
          elif number in zero:
               return f"{g} {number:2} {a}"
               

     print(f"""
     +-------------------+-------------------+-------------------+
     |      1st 12       |      2nd 12       |      3rd 12       |    
+----+----+----+----+----+----+----+----+----+----+----+----+----+----+
|{colorize(0)}|{colorize(3)}|{colorize(6)}|{colorize(9)}|{colorize(12)}|{colorize(15)}|{colorize(18)}|{colorize(21)}|{colorize(24)}|{colorize(27)}|{colorize(30)}|{colorize(33)}|{colorize(36)}|1st |
|{g}    {a}+----+----+----+----+----+----+----+----+----+----+----+----+----+
+----|{colorize(2)}|{colorize(5)}|{colorize(8)}|{colorize(11)}|{colorize(14)}|{colorize(17)}|{colorize(20)}|{colorize(23)}|{colorize(26)}|{colorize(29)}|{colorize(32)}|{colorize(35)}|2nd | 
|{g}    {a}+----+----+----+----+----+----+----+----+----+----+----+----+----+
|{colorize(0)}|{colorize(1)}|{colorize(4)}|{colorize(7)}|{colorize(10)}|{colorize(13)}|{colorize(16)}|{colorize(19)}|{colorize(22)}|{colorize(25)}|{colorize(28)}|{colorize(31)}|{colorize(34)}|3rd |
+----+---------+---------+---------+---------+---------+---------+----+ 
     |   1-18  |  EVEN   |{r}   RED   {a}|{b}  BLACK  {a}|   ODD   |  19-36  |
     +---------+---------+---------+---------+---------+---------+    
""")

"""Print money that you have."""
def print_money():
    print("You have", money, "money.")

"""Place bet and bet type"""
def place_bet():
     bets = []
     while True:
          print("---------------------------------------------------------------------------------")
          bet = int(input("Enter your bet: "))
          if bet > money:
               print("You don't have enough money.")
               place_bet()

          print("""
Bet types: 
1. red("red"), black("black")
2. odd("odd"), even("even")
3. 1-18("1-18"), 19-36("19-36")
4. 1st 12("1st 12"), 2nd 12("2nd 12"), 3rd 12("3rd 12")
5. 1st 2:1 ("1st 2:1"), 2nd 2:1 ("2nd 2:1"), 3rd 2:1 ("3rd 2:1")
5. number
6. zero("0")
""")
          bet_type = input("Enter your bet type: ")
          if bet_type == "number":
               bet_type = int(input("Enter number: "))

          bets.append((bet, bet_type))

          print("---------------------------------------------------------------------------------")
          more_bets = input("Do you want to place another bet? (y/n): ").strip().lower()
          if more_bets != 'y':
               break
     
     return bets

"""Spin"""
def play(bets, money):
     total_bet = sum(bet for bet, bet_type in bets)
     if total_bet > money:
          print("You don't have enough money for these bets.")
          return money

     money -= total_bet
     number = random.choice(black + red + zero)

     if number in black:
          color = "black"
     elif number in red:
          color = "red"
     else:
          color = "green"

     if color != "green":
          if number % 2 == 0:
               odd_even = "even"
          else:
               odd_even = "odd"
          
          if number in range(1, 19):
               radius = "1-18"
          else:
               radius = "19-36"
          
          if number in range(1, 13):
               twelve = "1st 12"
          elif number in range(13, 25):
               twelve = "2nd 12"
          else:
               twelve = "3rd 12"
          
          if number in range(1, 34, 3):
               column = "1st 2:1"
          elif number in range(2, 35, 3):
               column = "2nd 2:1"
          else:
               column = "3rd 2:1"

     else:
          odd_even = False
          radius = False
          twelve = False
          column = False

     for bet, entered_bet_type in bets:
          if entered_bet_type == "red" or entered_bet_type == "black":
               if entered_bet_type == color:
                    print("You won.")
                    money += bet * 2
               else:
                    print("You lost.")
          elif entered_bet_type == "odd" or entered_bet_type == "even":
               if entered_bet_type == odd_even:
                    print("You won.")
                    money += bet * 2
               else:
                    print("You lost.")
          elif entered_bet_type == "1-18" or entered_bet_type == "19-36":
               if entered_bet_type == radius:
                    print("You won.")
                    money += bet * 2
               else:
                    print("You lost.")
          elif entered_bet_type == "1st 12" or entered_bet_type == "2nd 12" or entered_bet_type == "3rd 12":
               if entered_bet_type == twelve:
                    print("You won.")
                    money += bet * 3
               else:
                    print("You lost.")

          elif entered_bet_type == "1st 2:1" or entered_bet_type == "2nd 2:1" or entered_bet_type == "3rd 2:1":
               if entered_bet_type == column:
                    print("You won.")
                    money += bet * 3
               else:
                    print("You lost.")

          elif entered_bet_type == "0" or entered_bet_type == "00":
               if entered_bet_type == number:
                    print("You won.")
                    money += bet * 36
               else:
                    print("You lost.")
          elif entered_bet_type and entered_bet_type in range(1, 37):
               if entered_bet_type == number:
                    print("You won.")
                    money += bet * 36
               else:
                    print("You lost.")
          else:
               print("Invalid bet type.")

     print("The number is", number, "and the color is", color)
     print("---------------------------------------------------------------------------------")
     return money


while money > 0:
     print_roulette()
     print_money()
     bets = place_bet()
     print("---------------------------------------------------------------------------------")
     money = play(bets, money)
     input("Press enter to play again.")
     os.system("cls")
