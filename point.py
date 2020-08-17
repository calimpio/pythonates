class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y
    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)
    
    def __str__(self):
        return 'x: ' + str(self.x) + ', y: ' + str(self.y)

    def __pow__(self, power):
        return Point(self.x**power, self.y**power)

    def __mul__(self,other):
        # other is integer or other is float?
        if isinstance(other, int) or isinstance(other,float):
            return Point(self.x*other, self.y*other)
        # other is Point?
        if isinstance(other, Point):
            return Point(self.x*other.x, self.y*other.y)
        return None