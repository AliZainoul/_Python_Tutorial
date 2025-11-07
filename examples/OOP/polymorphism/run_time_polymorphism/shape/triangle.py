from math import sqrt

from shape import Shape

class Triangle(Shape):
    def __init__(self, a: float,b: float,c: float):
        self.side_1 = a
        self.side_2 = b
        self.side_3 = c
    
    def area(self) -> float:
        s = (self.side_1 + self.side_2 + self.side_3) / 2
        return sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3)) # Heron formula to calculate the area of a Triangle
    
    def perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3

    def __str__(self) -> str:
        return f"Triangle({id(self) = }, {(self.side_1, self.side_2, self.side_3) = }, {self.area() = }, {self.perimeter() = })"
