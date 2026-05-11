class Teacher:
    
    def __init__(self, fname, lname, nick, age, status, grade):
        self.fname = fname
        self.lname = lname
        self.nick = nick
        self.age = age
        self.status = status
        self.grade = grade

    def GetInfo(self):
        return str(self.fname) + " " + str(self.lname) + " " + str(self.grade)

sbor = {
    "kozina" : Teacher("Petr", "Kozak", "kozy", 52, "Married", 9),
    "herman" : Teacher("Petr", "Heřmanský", "Berta", 60, "Angry", 7),
    "cyril" : Teacher("Cyril", "Kochrda", "cinko", 52, "Active", 8)
}
print(sbor["cyril"].status)