class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.z = 10
    
    def __len__(self):
        print(self.__dict__)
        return len(self.__dict__)
    
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

list_of_points = [p1, p2, p3, p4, p5, p6]

for point in list_of_points:
    print(len(point))

print(p1 == p2)
print(p3 >= p4)
print(p5 == p6)