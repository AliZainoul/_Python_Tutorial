# def add(a: float, b: float) -> float:
#     return float(a+b)

# input_1 : float = float(input("Please enter your first input : "))
# print("\n")
# input_2 : float = float(input("Please enter your second input : "))

# print(f"The first argument is {input_1}, \
#       whereas the second argument is {input_2}")

# print(f"The addition of {input_1} and {input_2} \
#       is : {add(input_1,input_2)}. \n")


# -------------------------------------------------------------------

# class MathOps:
#     def __init__(self, a: float = 0.0, b: float = 0.0):
#         self.a : float = float(a)
#         self.b : float = float(b)

#     def add(self):
#         return (self.a + self.b)

#     def sub(self):
#         return (self.a - self.b)

#     def mult(self):
#         return (self.a * self.b)

#     def div(self):
#         if self.b != 0.0:
#             return (self.a / self.b)
#         else:
#             raise ZeroDivisionError

#     def set_a(self, a: float) -> None:
#         self.a = a

#     def set_b(self, b: float) -> None:
#         self.b = b

#     def get_a(self) -> float:
#         return self.a

#     def get_b(self) -> float:
#         return self.b
    
#     def __str__(self) -> str:
#         return f"(a = {self.a}, b = {self.b}, add={self.add()}, sub={self.sub()}, mult={self.mult()}, div={self.div()})"
    

# o1 = MathOps()
# o1.set_b(1)
# print(str(o1))

# o2 = MathOps(a=32.5)
# o2.set_b(1)
# print(str(o2))

# o3 = MathOps(b=0.5)
# print(str(o3))

# o4 = MathOps(1,1)
# print(str(o4))


# -------------------------------------------------------------------


class MathOps:
    a : float = 0.0
    b : float = 0.0

    @staticmethod
    def static_add():
        return (MathOps.a + MathOps.b)

    @staticmethod
    def static_sub():
        return (MathOps.a - MathOps.b)

    @staticmethod
    def static_mult():
        return (MathOps.a * MathOps.b)

    @staticmethod
    def static_div():
        if MathOps.b != 0.0:
            return (MathOps.a / MathOps.b)
        else:
            raise ZeroDivisionError

    @classmethod
    def set_cls_var_a(cls, a: float) -> None:
        cls.a = a

    @classmethod
    def set_cls_var_b(cls, b: float) -> None:
        cls.b = b

    @classmethod
    def get_cls_var_a(cls) -> float:
        return cls.a

    @classmethod
    def get_cls_var_b(cls) -> float:
        return cls.b

    @staticmethod
    def display_infos():
        print(f"STATIC METHOD: (a = {MathOps.a}, b = {MathOps.b}, add={MathOps.static_add()}, sub={MathOps.static_sub()}, mult={MathOps.static_mult()}, div={MathOps.static_div()})")

    @classmethod
    def display_infos(cls):
        print(f"CLASS METHOD: (a = {cls.a}, b = {cls.b}, add={cls.static_add()}, sub={cls.static_sub()}, mult={cls.static_mult()}, div={cls.static_div()})")

MathOps.set_cls_var_b(1)
MathOps.display_infos()