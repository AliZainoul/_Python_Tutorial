import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def __str__(self):
        return f"Circle of id : {id(self)} and of radius : {self.__radius}"
    
    @property
    def radius(self):
        """ The radius property """
        print("Get Radius : \n")
        return self.__radius

    @radius.setter
    def radius(self, value):
        """ The radius Setter property """
        print("Set Radius : \n")
        self.__radius = value
    
    @radius.deleter
    def radius(self):
        """ The radius Deleter property """
        print("Del Radius : \n")
        del self.__radius


c = Circle(math.pi)
print(c)

print(c.radius)

#c.__radius = 46474 
# THE AFFECTION COMPILES AND NO ERRORS ARE THROWN 
# EITHER IN COMPILE OR RUNTIME, 
# HOWEVER THE __radius member of instance c is not modified !!!!

c.radius = 46474
print(c)

# del c.radius
# print(c)
