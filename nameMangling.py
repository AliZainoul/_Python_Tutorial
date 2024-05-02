class MyClass:
    def __init__(self):
        self.__private_attritube = 420

    def __private_method(self):
        print("This is a private method")

# Creating an instance of the class
obj = MyClass()

# Accessing the private attribute from outside the class
# print(obj.__private_attritube)  # This will raise an AttributeError

# Calling the private method from outside the class
# obj.__private_method()  # This will also raise an AttributeError

# Accessing the private attribute using name mangling
print(obj._MyClass__private_attritube)  # This will print 420

# Calling the private method using name mangling
obj._MyClass__private_method()  # This will print "This is a private method"
