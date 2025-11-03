# =============================
# Simple Inheritance Example
# =============================
class A:
    """Class A demonstrates a simple class with one member variable.

    This class serves as a base class for demonstrating multiple inheritance.
    It defines a single attribute initialized at object creation.
    """

    def __init__(self, value_1):
        """Initialize an instance of class A.

        Args:
            value_1: The value to assign to `member_1`.
        """
        self.__member_1 = value_1

    def get_member_1(self):
        """Get the value of member_1."""
        return self.__member_1
    
class B(A):

    def __init__(self, value_1, value_2):
        """Initialize an instance of class B.

        Args:
            value_2: The value to assign to `member_2`.
        """
        super().__init__(value_1)
        self.__member_2 = value_2

    def get_member_2(self):
        """Get the value of member_2."""
        return self.__member_2

# Real example:
class Animal:
    """Class Animal represents a generic animal with a name."""
    def __init__(self, name):
        """Initialize an instance of class Animal.

        Args:
            name: The name of the animal.
        """
        self.__name = name

    def get_name(self):
        """Get the name of the animal."""
        return self.__name
    
class Cat(Animal):
    """Class Cat represents a Cat, inheriting from Animal."""
    def __init__(self, name, breed):
        """Initialize an instance of class Cat.
        Args:
            breed: The breed of the cat.
        """
        super().__init__(name)
        self.__breed = breed
    
    def get_breed(self):
        """Get the name of the cat."""
        return self.__breed    

    def meow(self):
        """Make the cat meow."""
        return "Meo_www_catalks_cow!"
    
def main():
    """Demonstrate simple inheritance (A → B)."""
    # Generic example : Demonstrate inheritance using classes A and B.
    print()
    print("--- Simple Inheritance Example ---") 
    print("Generic Example:")
    print("Demonstrate inheritance using classes A and B (A → B).")
    print("B inherits from A.")
    b = B(1, 2)
    print(f"{b.get_member_1() = }")
    print(f"{b.get_member_2() = }")
    print(f"{B.__mro__        = }")
    print()

    """Demonstrate single inheritance using classes Animal and Cat."""
    # Real example :
    print("--- Simple Inheritance (Real) Example ---")
    print("Demonstrate single inheritance using classes Animal and Cat. (Cat → Animal)")
    print("Real Example:")
    print("Cat inherits from Animal.")

    cat = Cat("Flake", "European Shorthair")
    print(f"{cat.get_name()= }")
    print(f"{cat.get_breed() = }")
    print(f"{cat.meow() = }")
    print(f"{Cat.__mro__        = }")
    print()

if __name__ == "__main__":
    main()
