class Triangle:
    def __init__(self, r):
        self.radius_okrujnosti = r

    def area(self):
        return self.radius_okrujnosti**2*2
t1 = Triangle(10)
print(t1.area())
