def playerscard (*prisemoney, firstname, lastname, ranking):
    print(f"Jméno: {firstname}\nPříjmení: {lastname}\nHodnocení: {ranking}\nVýhry: {sum(prisemoney)} Kč")
playerscard(1000, 5400, 7000, 1900  , firstname="Janik", lastname="Simon", ranking=1)