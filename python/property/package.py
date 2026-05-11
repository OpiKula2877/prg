class Package:
    def __init__(self, width, height, depth, weight):
        self.width = width
        self.height = height
        self.depth = depth
        self.weight = weight

        if self.width * self.height * self.depth > 500:
            raise ValueError("Total volume (w*h*d) must not exceed 500")
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Width must be a number")
        if value < 0 or value > 50:
            raise TypeError("Width must be between 0 and 50")
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Height must be a number")
        if value < 0 or value > 50:
            raise TypeError("Height must be between 0 and 50")
        self._height = value

    @property
    def depth(self):
        return self._depth
    
    @depth.setter
    def depth(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Depth must be a number")
        if value < 0 or value > 50:
            raise TypeError("Depth must be between 0 and 50")
        self._depth = value

    @property
    def weight(self):
        return self._weight
    
    @weight.setter
    def weight(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a number")
        if value > 20 or value <= 0:
            raise ValueError("Weight must be between 0 and 20")
        self._weight = value

p = Package(2, 50, 1, 15)
print(p.width, p.height, p.depth, p.weight)