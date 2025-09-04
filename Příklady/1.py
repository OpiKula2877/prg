penize = 0
running = True


while running:
    komand = str(input("Zadej command: "))
    if(komand == "new"):
        penize = int(input("Zadej hodnotu kolik chceš mít na účtě: "))
        print("Váš aktuální stav je: " + str(penize) + "kč.")
    elif(komand == "bank"):
        print("Tvůj momentální zůstatek na účtě je " + str(penize) + "kč.")
    elif(komand == "min"):
        minus = int(input("Zadejte hodnotu o jakou chcete příjít: "))
        if (penize >= minus):
            penize = (penize - minus)
            print("Tvůj momentální zůstatek na účtě je " + str(penize) + "kč.")
        else:
            print("Nemůžeš odečíst hodnotu větší, jak máš na účtě.")
    elif(komand == "plu"):
        minus = int(input("Zadejte hodnotu o jakou chcete navýšit váš účet: "))
        penize = (penize + minus)
        print("Tvůj momentální zůstatek na účtě je " + str(penize) + "kč.")
    elif(komand == "exit"):
        running = False
    elif(komand == "help"):
        print(" new = Udělá vám nový účet se začátečním kontem, který si zvolíte. \n bank = Ukáže vám kolik máte aktuálně na vašem kontě. \n min = Odečtete určitou zvolennou částku z vašeho aktuálního účtu. \n plu = Přičte určitou zvolennou částku na váš aktuální účet. \n help = Nápověda na všechny commandy. \n exit = Odejdete z programu.")
    else:
        print("Špatný cmd.")
