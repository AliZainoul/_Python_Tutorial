def _inspect(obj : any):
    return dir(obj)


class MathOps:
    def __init__(self, a: float = 0.0, b: float = 0.0):
        self.a : float = float(a)
        self.b : float = float(b)

    def add(self):
        return (self.a + self.b)

    def sub(self):
        return (self.a - self.b)

    def mult(self):
        return (self.a * self.b)

    def div(self):
        if self.b != 0.0:
            return (self.a / self.b)
        else:
            raise ZeroDivisionError

    def set_a(self, a: float) -> None:
        self.a = a

    def set_b(self, b: float) -> None:
        self.b = b

    def get_a(self) -> float:
        return self.a

    def get_b(self) -> float:
        return self.b
    
    def __str__(self) -> str:
        return f"(a = {self.a}, b = {self.b}, add={self.add()}, sub={self.sub()}, mult={self.mult()}, div={self.div()})"
    

o = MathOps()
o.set_b(1)
print(_inspect(o))

# print(o.__class__)
# print(o.__dict__)