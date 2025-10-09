from math import sqrt

class Triangle:
    def __init__(self, a: float,b: float,c: float):
        self.side_1 = a
        self.side_2 = b
        self.side_3 = c
    
    def area(self) -> float:
        s = (self.side_1 + self.side_2 + self.side_3) / 2
        return sqrt(s * (s - self.side_1) * (s - self.side_2) * (s - self.side_3))
        return self.length * self.width
    
    def perimeter(self) -> float:
        return self.side_1 + self.side_2 + self.side_3

    def __repr__(self) -> str:
        return f"({id(self) = }, {(self.side_1, self.side_2, self.side_3) =}, {self.area() = }, {self.perimeter() = })"
