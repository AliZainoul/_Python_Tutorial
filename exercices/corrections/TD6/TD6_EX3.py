from random import randint, choice
from faker import Faker


class Course:
    def __init__(self, title: str, teacher: str):
        self._title = title
        self._teacher = teacher

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._title != new_value:
                self._title = new_value
        else:
            raise TypeError("The title must be a string.")

    @property
    def teacher(self) -> str:
        return self._teacher

    @teacher.setter
    def teacher(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._teacher != new_value:
                self._teacher = new_value
        else:
            raise TypeError("The teacher must be a string.")

    def to_dict(self) -> dict:
        """Returns a dictionary representation of the Course instance."""
        return {
            "title": self.title,
            "teacher": self.teacher
        }

    def __str__(self):
        return f"Informations about course: {id(self)} : {self.to_dict()}"
    

class Address:
    def __init__(self, street: str = "", city: str = "", postal_code: str = ""):
        if not isinstance(street, str):
            raise TypeError("The street must be a string str.")
        self._street = street
    
        if not isinstance(city, str):
            raise TypeError("The city must be a string str.")
        self._city = city
    
        if not isinstance(postal_code, str):
            raise TypeError("The postal_code must be a string str.")
        self._postal_code = postal_code
    

    @property
    def street(self) -> str:
        return self._street
    
    @street.setter
    def street(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._street == new_value:
                return
            else:
                self._street = new_value
        else: 
            TypeError("The new street must be a string.")

    @property
    def city(self) -> str:
        return self._city
    
    @city.setter
    def city(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._city == new_value:
                return
            else:
                self._city = new_value
        else: 
            TypeError("The new city must be a string.")

    @property
    def postal_code(self) -> str:
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._postal_code == new_value:
                return
            else:
                self._postal_code = new_value
        else: 
            TypeError("The new postal_code must be a string.")

    def __eq__(self, other):
        if not isinstance(other, Address):
            raise TypeError("The address must be of type Address.")
        
        return \
            self._street == other._street \
        and self._city == other._city \
        and self._postal_code == other._postal_code



    def to_dict(self) -> dict:
        return dict({
            "street": self._street, 
            "city": self._city, 
            "postal_code": self._postal_code})
    
    def __str__(self):
        return f"Informations about person {id(self)} are: {self.to_dict()}."

    def introduce_self(self):
        print(self)

class Person:
    def __init__(self, name: str, first_name: str, age: int):
        self._name = name
        self._first_name = first_name
        if age < 0:
            raise ValueError("The age cannot be negative.")
        self._age = age
        self._address = Address()

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

    @property
    def address(self) -> Address:
        return self._address
    
    @address.setter
    def address(self, new_value: Address) -> None:
        if isinstance(new_value, Address):
            if self._address != new_value:
                self._address = new_value
        else: 
            TypeError("The new age must be an int.")

    def to_dict(self) -> dict:
        result : dict = dict({
            "name": self.name, 
            "first_name": self.first_name, 
            "age": self.age,
            })

        if self.address.street or self.address.city or self.address.postal_code :
            result["address"] = self._address.to_dict()

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
        self._courses = []

    
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

    def add_course(self, course: Course) -> None:
        self._courses.append(course)

    def show_courses(self) -> list:
        for course in self._courses:
            print(course)

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
        [Person(f.name().split()[0], f.name().split()[1], randint(1,100)) for _ in range(15)]
    list_of_students : list[Student] = \
        [Student(f.name().split()[0], f.name().split()[1], randint(12,100), f"{str(f.city())} University") for _ in range(15)]
    list_of_addresses: list[Address] = \
        [Address(f.street_name(), f.city(), f.postcode()) for _ in range(36)]

    # https://faker.readthedocs.io/en/master/providers/faker.providers.address.html#faker.providers.address.Provider.postcode

    for p in list_of_persons + list_of_students:
        if randint(1, randint(1,4397453957)) %2 == 0:
            p.address = choice(list_of_addresses)

    for p in list_of_persons + list_of_students:
        if isinstance(p, Student):
            print("Student : ")
            p.introduce_self()
            print("\n")
        if isinstance(p, Person):
            print("Person : ")
            p.introduce_self()
            print("\n")