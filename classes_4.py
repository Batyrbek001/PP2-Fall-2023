import math

class Point:
    def __init__(self):
        self.point1 = (0, 0)
        self.point2 = (0, 0)

    def show(self):
        input_str = input("point1 (x1, y1): ")
        self.point1 = list(map(int, input_str.split(',')))

    def move(self):
        input_str = input("point2 (x2, y2): ")
        self.point2 = list(map(int, input_str.split(',')))

    def dist(self):
        x1, y1 = self.point1
        x2, y2 = self.point2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(f"distance: {distance:.2f}")


point = Point()
point.show()
point.move()
point.dist()