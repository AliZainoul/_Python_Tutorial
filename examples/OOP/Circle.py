import math

class Circle:
    a_classvar = "I am a class variable, shared by all instances of Circle"
    def __init__(self, radius):
        self.__radius = radius
        print(globals())

    def __str__(self):
        return f"Circle of id : {id(self)} and of radius : {self.__radius}"
    
    @property
    def radius(self) -> float:
        """ The radius property """
        print("Get Radius property: \n")
        return self.__radius

    @radius.setter
    def radius(self, value) -> None:
        """ The radius Setter property """
        self.__radius = value
        print(f"Set Radius property: new value = {self.__radius}\n")

    
    @radius.deleter
    def radius(self) -> None:
        """ The radius Deleter property """
        print("Del Radius property : \n")
        del self.__radius


print("-" * 28 + "Printing the original state of my Circle" + "-" * 28 + '\n')
c = Circle(math.pi)
print(c)
print(c.__dict__)
print(Circle.__dict__)


print("-" * 28 + "Accessing the radius property" + "-" * 28 )
print(c.radius)

print("-" * 28 + "Setting the private member __radius DIRECTLY !!!" + "-" * 28 + '\n')
c.__radius =  42 
print(f"c__radius = {c.__radius}")
print(c)

#   THE AFFECTION COMPILES AND NO ERRORS ARE THROWN 
#   EITHER IN COMPILE OR RUNTIME, 
#   HOWEVER THE __radius member of instance c is not modified !!!!

print("-" * 28 + "Setting the private member via the setter property " + "-" * 28 + '\n')
c.radius = 123
print(c)

# print("-" * 50)
# del c.radius
# print(c)
