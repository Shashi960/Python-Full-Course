import math
class Shape:
    def calculate_area(self):
        pass 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height

shapes = [
    Circle(5),
    Rectangle(4, 6)
]

for shape in shapes:
    area = shape.calculate_area()
    print(f"Area: {area:.2f}")