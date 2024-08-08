# main.py

from circle import Circle
from rectangle import Rectangle


r = Rectangle(36.7, 32.5)
c = Circle(44)

l = [f"{repr(obj)}" for obj in [r,c]]

print(l)