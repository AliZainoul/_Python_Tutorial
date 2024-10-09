class Rectangle:
  def __init__(self, length: float, width: float):
    if (length <= 0.0 or width <= 0.0):
      raise ValueError("Invalid length and/or width.")
    self.length = length
    self.width = width
  
  def area(self):
    return self.length * self.width
  
  def perimeter(self):
    return (self.length + self.width) * 2
  
  def __str__(self):
    return f"The area of the rectangle is: {self.area()} cm and the perimeter of the rectangle is: {self.perimeter()} cm"
  
rect = Rectangle(10.4, 2)
print(rect)
# Equivalent to: (*IF* str method is overloaded " def __str__(self): ... ")
print(str(rect))
