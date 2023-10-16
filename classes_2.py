class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length = int(input())

    def area(self):
        return self.length ** 2

shape = Shape()
square = Square()

print(shape.area())
print(square.area())