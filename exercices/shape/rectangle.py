from shape import Shape

class Rectangle():
    def __init__(self, l: float, w: float):
        self.l = l
        self.w = w

    def area(self) -> float:
        return self.l * self.w

    def __repr__(self) -> str:
        return f"(id = {id(self)}, (l,w) = {(self.l, self.w)}, area = {self.area()})"
