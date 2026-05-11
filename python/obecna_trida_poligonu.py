class polygon:
    
    def __init__(self, sides):
        self.__sides = sides # private attribute

    def getSides(self):
        return self.__sides
    
    def setsizes(self, sides):
        self.__sides = sides

    def __str__(self): # string representation of the object # string is built-in method
        return f"Polygon with {self.__sides} sides"

class Triangle(polygon):
    def __init__(self):
        super().__init__(3)
#       polygon().__init__(self, 3) # alternative way to call the parent constructor

    def __str__(self):
        return "polygon with 3 sides is triangle"

class Penthagon(polygon):
    def __init__(self):
        super().__init__(5)

    def __str__(self):
        return "polygon with 5 sides is pentagon"

t = Triangle()
print(t)


p = polygon(7)
# print(p.__sides)   # This will raise an AttributeError because __sides is private
# print(p.__sides()) # This will raise an AttributeError because __sides is private
# p.__sides = 8      # This will raise an AttributeError because __sides is private
p.setsizes(8)
print(p.getSides())  # This will print 8
print(p.__str__())  # This will print 8