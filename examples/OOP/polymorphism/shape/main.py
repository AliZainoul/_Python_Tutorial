# main.py

from math import pi
from shape import Shape
from circle import Circle
from square import Square
from triangle import Triangle
from rectangle import Rectangle


r = Rectangle(36.7, 32.5)
s = Square(4)
c = Circle(pi)
t = Triangle(3,4,5)

list_of_shapes : list[Shape, Shape, Shape, Shape] = [r, s, c, t]


for shape in list_of_shapes:
    print(f"{repr(shape)}")