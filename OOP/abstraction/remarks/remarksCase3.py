# Simple, multiple, hierarchical and hybrid inheritances 
# involving abstract classes are *ALLOWED*


def printText(s):
    print("\n" + "-"* 16 + s + "-"* 16 + "\n")

printText("Simple inheritance involving abstraction")
# Simple inheritance
from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def method(self):
        pass

class Derived(Base):
    def method(self):
        print("Implementation of method in Derived class")

# Instantiating Derived class
d = Derived()
d.method()

printText("Multiple inheritance involving abstraction")
# Multiple inheritance
from abc import ABC, abstractmethod

class Base1(ABC):
    @abstractmethod
    def method_a(self):
        pass

class Base2(ABC):
    @abstractmethod
    def method_b(self):
        pass

class Derived(Base2, Base1):
    def method_a(self):
        print("Implementation of method_a in Derived class")

    def method_b(self):
        print("Implementation of method_b in Derived class")

# Instantiating Derived class
d = Derived()
d.method_a()
d.method_b()

printText("Hierarchical inheritance involving abstraction")
# Hierarchical inheritance
from abc import ABC, abstractmethod

class Base1(ABC):
    @abstractmethod
    def method_a(self):
        pass

class Base2(Base1):
    @abstractmethod
    def method_b(self):
        pass

class Derived(Base2):
    def method_a(self):
        print("Implementation of method_a in Derived class")

    def method_b(self):
        print("Implementation of method_b in Derived class")

# Instantiating Derived class
d = Derived()
d.method_a()
d.method_b()


printText("Hybrid inheritance involving abstraction")
# Hybrid inheritance
from abc import ABC, abstractmethod

class Base1(ABC):
    @abstractmethod
    def method_a(self):
        pass

class Base2(Base1):
    @abstractmethod
    def method_b(self):
        pass

class Base3(ABC):
    @abstractmethod
    def method_c(self):
        pass

class Derived(Base2, Base3):
    def method_a(self):
        print("Implementation of method_a in Derived class")

    def method_b(self):
        print("Implementation of method_b in Derived class")

    def method_c(self):
        print("Implementation of method_c in Derived class")

# Instantiating Derived class
d = Derived()
d.method_a()
d.method_b()
d.method_c()
