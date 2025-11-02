import math
from shape import Shape

class Circle(Shape):
    def __init__(self, r: float):
        self.radius = r

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __str__(self) -> str:
        return f"Circle({id(self) = }, {self.radius = }, {self.area() = }, {self.perimeter() = })"
        