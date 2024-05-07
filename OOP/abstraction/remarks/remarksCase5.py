from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def method_a(self):
        pass

    def method(self):
        print("Implementation of method in AbstractClass")

class Interface(ABC):
    @abstractmethod
    def method_b(self):
        pass

class MyClass(AbstractClass, Interface):
    def method_a(self):
        print("Implementation of method_a in MyClass")

    def method_b(self):
        print("Implementation of method_b in MyClass")

# Instantiating MyClass
obj = MyClass()
obj.method_a()
obj.method_b()
obj.method()