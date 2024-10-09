class Person:
    def __init__(self, name: str, age: int):
        if age < 0 :
            raise ValueError("Age cannot be negative")
        else:
            self.name = name
            self.age = age

    def display(self):
        print(f"Hello! your name is {self.name}, and you are {self.age} years old")

person_1 = Person("Brad Pitt", 60)
person_1.display()

# This line will generate the exception: ValueError("Age cannot be negative")
# person_2 = Person("Brad Pitt", -60)