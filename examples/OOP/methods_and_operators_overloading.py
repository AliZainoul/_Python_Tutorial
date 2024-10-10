class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point ({self.x}, {self.y})"
    
    def __len__(self):
        # print(self.__dict__)
        return len(self.__dict__)
    
    def __add__(self, other):
        # In the euclidian space, one can add two points of a plane (2D):
        # Assume that we have point p1 of coordinates: (x1 , y1)
        #                     point p2 of coordinates: (x2 , y2)
        # result = p1 + p2 = (x1 , y1) + (x2 , y2) = (x1 + x2 , y1 + y2)

        # Example:  if p1 = (1 , 2) and p2 = (3 , 4) 
        #           then result = p1 + p2 
        #                       = (1 , 2) + (3 , 4)
        #                       = (4 , 6)               
        return Point(self.x + other.x , self.y + other.y)
    

    def __sub__(self, other):
        # In the euclidian space, one can substract one point from another in a (2D) plane:
        # Assume that we have point p1 of coordinates: (x1 , y1)
        #                     point p2 of coordinates: (x2 , y2)
        # result = p1 - p2 = (x1 , y1) - (x2 , y2) = (x1 - x2 , y1 - y2)

        # Example:  if p1 = (1 , 2) and p2 = (3 , 4) 
        #           then result = p1 - p2 
        #                       = (1 , 2) - (3 , 4)
        #                       = (1-3 , 2-4) = (-2, -2)               
        return Point(self.x - other.x , self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

p1 = Point(4, 4)
p2 = Point(4, 4)

p3 = Point(5, 4)
p4 = Point(6, 4)

p5 = Point(3, 4)
p6 = Point(4, 3)

p7 = p5 + p2
p8 = p7 + p6 - (p1 + p3 + p4)

list_of_points = [p1, p2, p3, p4, p5, p6, p7, p8]

i = 0
for point in list_of_points:
    print(f" Point  P{i+1}: {point} and it's length = {len(point)}")
    i += 1

print(p1 == p2)
print(p3 >= p4)
print(p5 == p6)

