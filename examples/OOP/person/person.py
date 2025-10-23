class Person:
    """
    A simple class to demonstrate private attributes and name mangling in Python.

    Attributes
    ----------
    __name : str
        The "private" name of the person. It is name-mangled to _Person__name internally.

    Methods
    -------
    get_name():
        Returns the value of the private __name attribute.
    """

    def __init__(self, name: str):
        """
        Initializes a Person instance with a private name.

        Parameters
        ----------
        name : str
            The name of the person.
        """
        self.__name = name

    def get_name(self) -> str:
        """
        Getter method for the private __name attribute.

        Returns
        -------
        str
            The name of the person.
        """
        return self.__name


def main():
    """
    Demonstrates how Python handles private attributes (__name),
    name mangling, and attribute shadowing.
    """
    p = Person("Ali")

    # Access via the getter (correct way)
    print(f"Accessing the name member via the getter {p.get_name() = }")  # Prints: 'Ali'

    # Direct access to the mangled attribute (not recommended, but possible)
    print(f"Accessing the dict {p.__dict__ = }")  # Shows internal attribute: {'_Person__name': 'Ali'}
    
    # Accessing the mangled name directly, prints: 'Ali'
    print(p._Person__name)  # Prints: 'Ali'

    # Creating a new attribute with the same name does not override the mangled one
    p.__name = "Veli"  
    
    # This creates a new attribute '__name' in the instance's __dict__
    print(f"Accessing the dict {p.__dict__ = }")  # Shows both '_Person__name' and '__name' exist separately

    # Accessing the new attribute
    print(f"Accessing the new __name attribute {p.__name = }")  # Prints: 'Veli'

    # Original name is unchanged
    print(f"Accessing the original name via getter after shadowing {p.get_name() = }") # Still prints 'Ali'

    # Demonstrates that Python's "private" attributes are only name-mangled, not truly private


if __name__ == "__main__":
    main()
