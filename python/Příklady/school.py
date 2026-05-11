class school:

    count_in_class = 0
    count_of_girls = 0
    count_of_boys = 0

    def __init__(self, boys, girls):
        self.boys = boys
        self.girls = girls
        school.count_of_boys += boys
        school.count_of_girls += girls
        school.count_in_class += boys + girls
    def __del__(self):
        school.count_of_boys -= self.boys
        school.count_of_girls -= self.girls
        school.count_in_class -= self.boys + self.girls


C1A = school(15, 15)
C2A = school(14, 14)
C3A = school(16, 16)
C4A = school(13, 16)
C1B = school(12, 15)
C2B = school(17, 14)
C3B = school(13, 13)
C1C = school(10, 15)
C2C = school(15, 15)

print(school.count_of_boys)
print(school.count_of_girls)
print(school.count_in_class)
del C2A
print(school.count_of_boys)
print(school.count_of_girls)
print(school.count_in_class)


