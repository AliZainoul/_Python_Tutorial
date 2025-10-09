from shape import Shape

class Rectangle(Shape):
    def __init__(self, l: float, w: float):
        self.length = l
        self.width = w

    def area(self) -> float:
        return self.length * self.width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

    def __repr__(self) -> str:
        return f"({id(self) = }, {self.length = }, {self.width = }, {self.area() = }, {self.perimeter() = })"
