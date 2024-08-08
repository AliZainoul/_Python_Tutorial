import cmath
from shape import Shape

class Circle():
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return 2 * cmath.pi * self.r
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, radius = {self.r}, area = {self.area()})"

    
