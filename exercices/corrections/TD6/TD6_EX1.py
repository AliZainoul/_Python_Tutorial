from random import randint
from faker import Faker

class Person:
    # def __init__(self, name: str, first_name: str, age: int, street: str = "", city: str = "", postal_code: str = ""):

    def __init__(self, name: str, first_name: str, age: int):
        self._name = name
        self._first_name = first_name
        if age < 0:
            raise ValueError("The age cannot be negative.")
        self._age = age

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._name != new_value:
                self._name = new_value
        else: 
            TypeError("The new name must be a string.")

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._first_name != new_value:
                self._first_name = new_value
        else: 
            TypeError("The new first_name must be a string.")

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_value: int) -> None:
        if isinstance(new_value, int):
            if self._age != new_value:
                if new_value < 0:
                    raise ValueError("The age cannot be negative.")
                self._age = new_value
        else: 
            TypeError("The new age must be an int.")

    def to_dict(self) -> dict:
        result = {
            "name": self.name, 
            "first_name": self.first_name, 
            "age": self.age
        }
        return result
    
    def __str__(self):
        return f"Informations about person {id(self)} are: {self.to_dict()}."

    def introduce_self(self):
        print(self)


class Student(Person):
    def __init__(self, name: str, first_name: str, age: int, school: str):
        MINIMUM_AGE = 12
        if age < MINIMUM_AGE:
            raise ValueError(f"A student must have at least {MINIMUM_AGE} years old.")
        super().__init__(name, first_name, age)
        self._school = school
    
    @property
    def school(self) -> str:
        return self._school
    
    @school.setter
    def school(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._school != new_value:
                self._school = new_value
        else:
            raise TypeError("The new school must be a string.")

    def to_dict(self):
        result: dict = dict(super().to_dict())
        result['school'] = self.school
        return result
    
    def __str__(self):
        return f"Information about person {id(self)}: {self.to_dict()}."

    def introduce_self(self):
        print(self)


# ---------------------- MAIN ---------------------- #
if __name__ == "__main__":

    f = Faker()

    list_of_persons : list[Person] = \
        [Person(f.name().split()[0], f.name().split()[1], randint(1,100)) for _ in range(36)]
    list_of_students : list[Student] = \
        [Student(f.name().split()[0], f.name().split()[1], randint(12,100), f"{str(f.city())} University") for _ in range(36)]

    for p in list_of_persons + list_of_students:
        p.introduce_self()