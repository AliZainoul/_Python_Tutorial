import math
from typing import List, Tuple
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def __str__(self) -> str:
        return f"{id(self)}"

class Rectangle(Shape):
    def __init__(self, length: float, height: float):
        self.length = length
        self.height = height

    def area(self) -> float:
        return float(self.length * self.height)

    def perimeter(self) -> float:
        return float(2 * (self.length + self.height))
    

class Circle(Shape):
    def __init__(self, radius : float):
        self.radius = radius

    def area(self) -> float:
        return float(math.pi * self.radius ** 2)

    def perimeter(self) -> float:
        return float(2 * math.pi * self.radius)


# Duck typing : 
def calculate_area_and_perimeter(obj: Shape) -> Tuple[float, float] :
    return (obj.area(), obj.perimeter())
# Please note that the function above is INDEED A FUNCTION, and takes obj of type
# Shape but does not *INHERITS* from class Shape...

# Example usage
rectangle = Rectangle(5, 4)
circle = Circle(3)

list_of_shapes : List[Shape] = [rectangle, circle]

print("Rectangle Area:", rectangle.area())     # Output: Rectangle Area: 20
print("Rectangle Perimeter:", rectangle.perimeter())   # Output: Rectangle Perimeter: 18
print("Circle Area:", circle.area())        # Output: Circle Area: 28.26
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 18.84

for shape in list_of_shapes:
    print(f"The area and perimeter respectively of id: {shape} is {calculate_area_and_perimeter(shape)}")