class MyClass :
    def __init__(self) :
        self.public_attribute       =   42 
        self._protected_attribute   =   "protected" 
        self.__private_attribute    =   "private"

    def _access_attributes(self) :
        print("Public attribute:",      self.public_attribute) 
        print("Protected attribute:",   self._protected_attribute) 
        print("Private attribute:",     self.__private_attribute)

    def public_method(self) :
        print("This is a public method.")

    def _protected_method(self) :
        print("This is a protected method.")

    def __private_method(self) :
        print("This is a private method.")


def main() :
    obj = MyClass()
    obj._access_attributes()

    print("-" * 20)

    print("Accessing public attribute directly:", obj.public_attribute)
    print("Accessing protected attribute directly:", obj._protected_attribute)
    # The following line will raise an AttributeError because __private_attribute is not accessible outside the
    # print("Accessing private attribute directly:", obj.__private_attribute)

    print("-" * 20)

    # Call to the public method works fine
    obj.public_method()
    # Call the protected method class, it works because we are withing the same package where the class is defined
    obj._protected_method()
    # Call to the private method will also raise an AttributeError class
    # obj.__private_method()

if __name__ == "__main__" :
    main()
