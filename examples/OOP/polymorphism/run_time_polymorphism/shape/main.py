# main.py

from math import pi as PI

from shape import Shape

from circle import Circle
from square import Square
from triangle import Triangle
from rectangle import Rectangle


r : Rectangle = Rectangle(36.7, 32.5)
s : Square = Square(4)
c : Circle = Circle(PI)
t : Triangle = Triangle(3,4,5)

# Duck typing for shape parameter
def print_shape_info(shape: Shape | Rectangle | Square | Circle | Triangle) -> None:
    print(str(shape))

# List of various shapes
list_of_shapes : list[Rectangle | Square | Circle | Triangle] = [r, s, c, t]

print("\n" + "-" * 69 * 2)

# Iterate and print info for each shape
for shape in list_of_shapes:
    print_shape_info(shape)
    print("-" * 69 * 2)

print()
