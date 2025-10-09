import cmath
from shape import Shape

class Circle():
    def __init__(self, r: float):
        self.r = r

    def area(self) -> float:
        return cmath.pi * self.r ** 2
    
    def __repr__(self) -> str:
        return f"(id = {id(self)}, radius = {self.r}, area = {self.area()})"

    
