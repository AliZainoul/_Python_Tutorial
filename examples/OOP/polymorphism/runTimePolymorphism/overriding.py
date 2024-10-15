import time


def printText(s):
    print("\n" + "--"*16 + s + "--"*16 + "\n")

printText("Without Abstraction")
# Start Timer
start_time_1 = time.perf_counter()

# Base class
class Animal_1():
    def sound_1(self):
        pass

# Derived class that overrides the abstract method
class Dog_1(Animal_1):
    def sound_1(self):
        print("Woof!")

# Instantiation and test
dog_1 = Dog_1()
dog_1.sound_1()

# End Timer
end_time_1 = time.perf_counter()

# Elapsed Time
elapsed_time_1 = end_time_1 - start_time_1
print(f"Elapsed time : {elapsed_time_1}.")





printText("With Abstraction")
from abc import ABC, abstractmethod

# Start Timer
start_time_2 = time.perf_counter()


# Base class with abstract method
class Animal_2(ABC):
    @abstractmethod
    def sound_2(self):
        pass

# Derived class that overrides the abstract method
class Dog_2(Animal_2):
    def sound_2(self):
        print("Woof!")

# Instantiation and test
dog_2 = Dog_2()
dog_2.sound_2()

# End Timer
end_time_2 = time.perf_counter()

# Elapsed Time
elapsed_time_2 = end_time_2 - start_time_2
print(f"Elapsed time : {elapsed_time_2}.")

# Time Ratio
print(f"Ratio of elapsed_time_2 / elapsed_time_1 = {elapsed_time_2/elapsed_time_1}")

'''
    If ratio <= 1 then abstraction is OK!
    otherwise usage of abstraction for overriding methods may seem useless,
    however the pros of using abstraction and overriding are:
    - Extensible systems bringing consistence
    - Designing APIs in order to expose a clean interface with flexibility
    - Improving readability and maintainability 
'''