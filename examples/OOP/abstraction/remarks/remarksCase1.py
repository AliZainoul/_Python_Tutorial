from abc import ABC, abstractmethod

class Base(ABC):
    @abstractmethod
    def abstract_method_1(self):
        pass

    @abstractmethod
    def abstract_method_2(self):
        pass

class Derived(Base):
    def abstract_method_1(self):
        print("Implementation of abstract method 1 in Derived class")

    # Because of the fact that abstract_method_2 is not overriden, 
    # so the class becomes abstract

# Attempting to instantiate Derived class
# This will raise an error since Derived is still abstract
try:
    d = Derived()
except Exception as e:
    print("Error:", e)
    
# Output: 
# Error: Can't instantiate abstract class Derived with abstract methods 
#       abstract_method_2