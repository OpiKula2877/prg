class pozemky:
    total_area = 0
    total_build = 0
    total_agri = 0
    
    def __init__(self, id, area, kind):
        self.id = id
        self.area = area
        self.kind = kind
        if self.kind == "stavebni" or self.kind == "zpf" or self.kind == "mixed":
            print("Vše je ok")
        else:
            print(f"{pozemky.id} má neplatný druh pozemku")
            exit()
        pozemky.total_area += 1
        if self.kind == "stavebni":
            pozemky.total_agri += 1
        if self.kind == "zpf":
            pozemky.total_agri += 1

    def __del__(self):
        pozemky.total_area -= 1
        if self.kind == "stavebni":
            pozemky.total_agri -= 1
        if self.kind == "zpf":
            pozemky.total_agri -= 1

    def summary(self):
        print(f"Celkový počet pozemků: {pozemky.total_area}")
        print(f"Celkový počet stavebních pozemků: {pozemky.total_build}")
        print(f"Celkový počet zemědělských pozemků: {pozemky.total_agri}")
    