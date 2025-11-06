class MyClass :
    # Constructor
    def __init__(self) :
        self.public_attribute      : int =   42                 # Public member
        self._protected_attribute  : str =   "protected"        # Protected member
        self.__private_attribute   : str =   "private"          # Private member


    # Public Method
    def public_method(self) :
        print("This is a public method.")

    # Protected Method
    def _protected_method(self) :
        print("This is a protected method.")

    # Private Method
    def __private_method(self) :
        print("This is a private method.")

    # Public  Method
    def public_access_attributes(self) :
        print("I AM IN public_access_attributes method")
        print(f"Public attribute:       {self.public_attribute = }") 
        print(f"Protected attribute:    {self._protected_attribute = }") 
        print(f"Private attribute:      {self.__private_attribute = }")
        print("-" * 69)

    # Protected Method
    def _protected_access_attributes(self) :
        print("I AM IN _protected_access_attributes method")
        print(f"Public attribute:       {self.public_attribute = }") 
        print(f"Protected attribute:    {self._protected_attribute = }") 
        print(f"Private attribute:      {self.__private_attribute = }")
        print("-" * 69)

    # Private Method
    def __private_access_attributes(self) :
        print("I AM IN __private_access_attributes method")
        print(f"Public attribute:       {self.public_attribute = }") 
        print(f"Protected attribute:    {self._protected_attribute = }") 
        print(f"Private attribute:      {self.__private_attribute = }")
        print("-" * 69)


def main() :
    obj = MyClass()

    print("-" * 69)

    print("Accessing public attribute directly:", obj.public_attribute)
    print("Accessing protected attribute directly:", obj._protected_attribute)
    # The following line will raise an AttributeError because __private_attribute is not accessible outside the
    # print("Accessing private attribute directly:", obj.__private_attribute)
    print(f"{obj.__dict__}")

    print("-" * 69)

    # Call to the public method works fine
    obj.public_method()
    # Call the protected method class, it works because we are withing the same package where the class is defined
    obj._protected_method()
    # Call to the private method will also raise an AttributeError class
    # obj.__private_method()
    print(f"{obj.__dict__}")

    print("-" * 69)

    obj.public_access_attributes()
    obj._protected_access_attributes()
    # Call to the private method will also raise an AttributeError class
    # obj.__private_access_attributes()
    print(f"{obj.__dict__}")

    print("-" * 69)

if __name__ == "__main__" :
    main()
