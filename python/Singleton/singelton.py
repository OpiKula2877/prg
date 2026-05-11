class Jews:

    __instance = None
    
    @staticmethod
    def buy(name, price): 
        if Jews.__instance is None:
            if price <= 1000:
                Jews()
            else:
                print(f"This {name} is too expensive, honey!")
        else:
            print("Only one jewel, honey!")
        return Jews.__instance
    
    def __init__(self):
        if Jews.__instance is not None:
            raise Exception("Only one Jewel, honey!")
        else:
            Jews.__instance = self
        
j1 = Jews.buy("Ginger", 1001)
j2 = Jews.buy("Black", 999)
print(j1, j2)