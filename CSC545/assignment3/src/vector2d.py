import math

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def dist(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y)**2))

    def subtract(self, other):
        return Vector2D(math.sqrt((self.x - other.x) ** 2), math.sqrt((self.y - other.y)**2))

    def scale(self, scalar):
        return Vector2D(scalar * self.x, scalar * self.y)

    def abs(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def asTuple(self):
        return tuple(self.x, self.y)
