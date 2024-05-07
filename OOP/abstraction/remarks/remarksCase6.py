from abc import ABC, abstractmethod

class Interface1(ABC):
    @abstractmethod
    def method_interface_1(self):
        pass

class Interface2(Interface1):
    @abstractmethod
    def method_interface_2(self):
        pass

class Interface3(Interface2, Interface1):
    @abstractmethod
    def method_interface_3(self):
        pass

class MyClass(Interface3):
    def method_interface_1(self):
        print("Implementation of method_interface_1 in MyClass")

    def method_interface_2(self):
        print("Implementation of method_interface_2 in MyClass")

    def method_interface_3(self):
        print("Implementation of method_interface_3 in MyClass")

# Instantiating MyClass3
obj = MyClass()
obj.method_interface_1()
obj.method_interface_2()
obj.method_interface_3()