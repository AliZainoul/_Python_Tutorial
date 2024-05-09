from abc import ABC, abstractmethod

# Une classe peut-elle dériver de plusieurs interfaces ?
class Interface1(ABC):
    @abstractmethod
    def method1(self):
        pass

class Interface2(ABC):
    @abstractmethod
    def method2(self):
        pass

class MyClass(Interface1, Interface2):
    def method1(self):
        print("Implementation of method1 in MyClass")

    def method2(self):
        print("Implementation of method2 in MyClass")

# Instantiating MyClass
obj = MyClass()
obj.method1()
obj.method2()