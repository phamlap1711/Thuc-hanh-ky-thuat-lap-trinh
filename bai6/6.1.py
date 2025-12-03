print("Pham Tien lap")
print("248752021610071")

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius ** 2) * 3.14

aCircle = Circle(5)
print(aCircle.area())
