class MyClass:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        print("Setting value using property setter")
        self.__value = value

    @property
    def value_with_validation(self):
        return self.__value

    @value_with_validation.setter
    def value_with_validation(self, value):
        print("Setting value using property setter with validation")
        if isinstance(value, int):
            self.__value = value
        else:
            raise ValueError("Value must be an integer")

# Creating an instance of MyClass
obj = MyClass()

# Using property setter
obj.value = 0
print("Value:", obj.value)                  # Output: Value: 0
print("Value:", obj.value_with_validation)  # Output: Value: 0

# Using property setter with validation
obj.value_with_validation = 1
print("Value:", obj.value)                  # Output: Value: 1
print("Value:", obj.value_with_validation)  # Output: Value: 1


# Trying to set value with invalid type
try:
    obj.value_with_validation = "invalid"
except ValueError as e:
    print("Error:", e)  # Output: Error: Value must be an integer
