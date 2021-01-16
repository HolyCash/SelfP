import math

class Circle:
    def __init__(self, r):
        self.radius = r 
    def calculate_area (self):
        return self.radius ** 2 * math.pi

c1 = Circle(52)
print(c1.calculate_area())
