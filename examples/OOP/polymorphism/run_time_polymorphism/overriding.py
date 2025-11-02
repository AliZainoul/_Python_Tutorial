# =============================================
# Runtime Polymorphism via Method Overriding
# =============================================

from abc import ABC, abstractmethod

# Base class with abstract method
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

# Derived class that overrides the abstract method
class Dog(Animal):
    def sound(self):
        print("Woof!")

# Instantiation and test
dog = Dog()
dog.sound() # Outputs: Woof!

'''
    The pros of using abstraction and overriding are:
    - Extensible systems bringing consistence
    - Designing APIs in order to expose a clean interface with flexibility
    - Improving readability and maintainability 
'''
