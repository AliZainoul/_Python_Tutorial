from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, height):
        self.length = length
        self.height = height

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2 * (self.length + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

# Example usage
rectangle = Rectangle(5, 4)
circle = Circle(3)

print("Rectangle Area:", rectangle.area())     # Output: Rectangle Area: 20
print("Rectangle Perimeter:", rectangle.perimeter())   # Output: Rectangle Perimeter: 18
print("Circle Area:", circle.area())        # Output: Circle Area: 28.26
print("Circle Perimeter:", circle.perimeter())  # Output: Circle Perimeter: 18.84