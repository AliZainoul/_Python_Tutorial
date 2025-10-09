from shape import Shape

class Square(Shape):
    def __init__(self, s: float):
        self.side = s

    def area(self) -> float:
        return self.side ** 2
    
    def perimeter(self) -> float:
        return 4 * (self.side)

    def __repr__(self) -> str:
        return f"({id(self) = }, {self.side = }, {self.area() = }, {self.perimeter() = })"
