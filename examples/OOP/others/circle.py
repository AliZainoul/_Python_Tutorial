import math


class OldCircle:
    def __init__(self, radius):
        self.__radius = radius
        # print(globals())

    def __str__(self):
        return f"Circle of id : {id(self)} and of radius : {self.__radius}"
    
    
    def get_radius(self) -> float:
        """ The radius property """
        print("Get Radius property: \n")
        return self.__radius

    def set_radius(self, value) -> None:
        """ The radius Setter property """
        self.__radius = value
        print(f"Set Radius property: new value = {self.__radius}\n")

    def delete_radius(self) -> None:
        """ The radius Deleter property """
        print("Del Radius property : \n")
        del self.__radius


class Circle:
    def __init__(self, radius):
        self.__radius = radius
        # print(globals())

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


def main() : 
    # TODO: add OldCircle getter / setter manip 


    print("-" * 28 + "Printing the original state of my Circle" + "-" * 28 + '\n')
    c = Circle(math.pi)
    print(c)
    print(c.__dict__)
    # print(Circle.__dict__)


    print("-" * 28 + "Accessing the radius property" + "-" * 28 )
    # print(c.__radius)  # This will raise an AttributeError because __radius is private
    # print(c._Circle__radius)  # This works because of name mangling
    print(c.radius)

    print("-" * 28 + "Setting the private member __radius DIRECTLY !!!" + "-" * 28 + '\n')
    c.__radius =  42
    print(c.__dict__)
    print(f"c__radius = {c.__radius}")
    print(c)

    #   THE AFFECTION COMPILES AND NO ERRORS ARE THROWN 
    #   EITHER IN COMPILE OR RUNTIME, 
    #   HOWEVER THE __radius member of instance c is not modified !!!!

    print("-" * 28 + "Setting the private member via the setter property " + "-" * 28 + '\n')
    c.radius = 10 * math.pi
    print(c)

    print("-" * 28 + "Deleting the private member via the deleter property " + "-" * 28 + '\n')
    print(c.__dict__)
    del c.radius
    # del c._Circle__radius                     # Deletes the private member via name mangling
    # del c.__radius                            # Deletes the newly created member named __radius in __dict__
    print(c.__dict__)

    del c
    # print(c)                                  # This will raise an AttributeError because __radius has been deleted, beware of the fact that you MUST NOT DELETE
    # the private member directly, but only via the deleter property if it is defined !


if __name__ == "__main__":
    main()
