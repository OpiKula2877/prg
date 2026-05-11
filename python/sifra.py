class RailFence:
    
    # počáteční inicializace vlastností objektu
    def __init__(self, rails = 3):
        self.__rails = rails    # počet kolejnic == 3
        self.__ot = ""          # otevřený text
        self.__ot_len = 0       # délka otevřeného textu
        self.__ct = ""          # šifrovaný text
        self.__ct_len = 0       # délka šifrovaného textu
         
    # šifruje open_text
    def encrypt(self, open_text):

        self.__ot = open_text                   # vlastnosti self.__ot přiřadíme hodnotu paramteru open_text
        self.__ot_len = len(self.__ot)          # vlastsnosti self.__ot_len přiřadíme délku řetězce selt.__ot
        self.__ct = ""
        
        row, asc = 0, True                      # row = aktuální řádek, col = aktuální sloupec, asc = True / False (vzestupně / sestupně)
        ct = [""] * self.__rails                # list s požadovaným počtem prázdných řetězců 
        
        for i in range(0, self.__ot_len):       # iterace otevřeného textu znak po znaku, zjišťujeme pozici řádku pro každý znak
            
            # tady je implementace šifrování            
            ct[row] += self.__ot[i]

            # zde určujeme číslo řádku pro každý znak otevřeného textu
            if (asc == True and row < self.__rails - 1):
                row += 1
            elif (asc == True and row == self.__rails - 1):
                asc = False
                row -= 1
            elif (asc == False and row > 0):
                row -= 1
            else:
                asc = True
                row += 1
        self.__ct = "".join(ct)
        return self.__ct
                      
    # dešifruje cypher_text
    # dešifruje cypher_text
    def decrypt(self, cypher_text):

        self.__ct = cypher_text                 # vlastnosti self.__ct přiřadíme hodnotu parametru cypher_text
        self.__ct_len = len(self.__ct)          # vlastnosti self.__ct_len přiřadíme délku řetězce self.__ct
        self.__ot = ""                          # připravíme si prázdný řetězec pro otevřený text

        # 1. KROK: Zjistíme, kolik znaků patří na každou kolejnici (řádek)
        # Vytvoříme "šablonu" stejnou jako při šifrování – budeme potřebovat délky řádků
        
        row, asc = 0, True                      # row = aktuální řádek, asc = směr (True = dolů, False = nahoru)
        row_lengths = [0] * self.__rails        # seznam počtů znaků pro každou kolejnici (např. [2, 4, 2] pro "AHOJEVO", rails=3)

        # simulujeme průchod šifrováním – jen počítáme, kolik znaků by skončilo na každém řádku
        for i in range(self.__ct_len):
            row_lengths[row] += 1               # na aktuální řádek přičteme jeden znak

            # stejná logika jako při šifrování – určení dalšího řádku
            if asc:
                if row < self.__rails - 1:
                    row += 1
                else:
                    asc = False
                    row -= 1
            else:
                if row > 0:
                    row -= 1
                else:
                    asc = True
                    row += 1

        # 2. KROK: Rozdělíme šifrovaný text na jednotlivé řádky podle zjištěných délek
        rows = []                               # seznam řetězců – každý obsahuje znaky jednoho řádku
        index = 0                               # index v šifrovaném textu

        for length in row_lengths:
            rows.append(self.__ct[index:index + length])  # vezmeme další "length" znaků z cypher_textu
            index += length

        # 3. KROK: Simulujeme přečtení znaků podle cesty plotýnky (stejná logika jako při šifrování)
        # Tentokrát ale místo ukládání znaků do řádků je načítáme z nich a skládáme do otevřeného textu
        
        row, asc = 0, True                      # resetujeme pozici a směr
        pointers = [0] * self.__rails          # ukazatele – kolikátý znak jsme už vzali z každého řádku

        for i in range(self.__ct_len):
            # z aktuálního řádku vezmeme znak na pozici pointers[row]
            self.__ot += rows[row][pointers[row]]
            pointers[row] += 1                  # posuneme ukazatel pro tento řádek

            # opět stejná logika určení dalšího řádku
            if asc:
                if row < self.__rails - 1:
                    row += 1
                else:
                    asc = False
                    row -= 1
            else:
                if row > 0:
                    row -= 1
                else:
                    asc = True
                    row += 1

        return self.__ot
    
    # getter vrátí počet kolejnic
    def getRails(self):
        return self.__rails
    
    # getter vrátí otevřený text
    def getOpenText(self):
        return self.__ot
    
    # getter vrátí délku otevřeného textu
    def getOpenTextLen(self):
        return self.__ot_len

    # getter vrátí šifrovaný text
    def getCypherText(self):
        return self.__ct
    
    # getter vrátí délku šifrovaného textu
    def getCypherTextLen(self):
        return self.__ct_len

cypher = RailFence()
print(cypher.encrypt("AHOJEVO"))

cypher2 = RailFence(4)
print(cypher2.encrypt("AHOJEVO"))

cypher3 = RailFence()
print(cypher3.decrypt("AEHJVOO"))

cypher4 = RailFence(4)
print(cypher4.decrypt("AOHVOEJ"))