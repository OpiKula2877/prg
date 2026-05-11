class Point:
    def __init__(self, x, y):
        self.setx(x)
        self.sety(y)

    def getx(self):
        return self._x

    def gety(self):
        return self._y 
    
    def setx(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self._x = value

    def sety(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self._y = value

    def __str__(self):
        return f"[{self.getx()}, {self.gety()}]"
        
p = Point(10, 20)
print(p)