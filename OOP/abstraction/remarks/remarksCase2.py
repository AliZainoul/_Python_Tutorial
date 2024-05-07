from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def method_a(self):
        pass

class B(ABC):
    @abstractmethod
    def method_b(self):
        pass

class C(B, A):
    def method_b(self):
        print("Implementation of method_b in class C")

    def method_a(self):
        print("Implementation of method_a in class C")


c = C()
c.method_a()
c.method_b()