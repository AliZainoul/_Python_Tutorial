from random import randint
from faker import Faker


class Company:
    def __init__(self, name: str, industry: str):
        self.name = name
        self.industry = industry

    def __str__(self):
        return f"Company: {self.name}, Industry: {self.industry}"


class Course:
    def __init__(self, title: str, teacher: str):
        self.title = title
        self.teacher = teacher

    def __str__(self):
        return f"Course: {self.title}, Teacher: {self.teacher}"


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
    # def __init__(self, name: str, first_name: str, age: int, street: str = "", city: str = "", postal_code: str = ""):

    def __init__(self, name: str, first_name: str, age: int):
        self._name = name
        self._first_name = first_name
        if age < 0:
            raise ValueError("The age cannot be negative.")
        self._age = age
        # self._address = Address(street, city, postal_code)
        self._company = None  # Initialize with no company association


    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._name == new_value:
                return
            else:
                self._name = new_value
        else: 
            TypeError("The new name must be a string.")

    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, new_value: str) -> None:
        if isinstance(new_value, str):
            if self._first_name == new_value:
                return
            else:
                self._first_name = new_value
        else: 
            TypeError("The new first_name must be a string.")

    @property
    def age(self) -> int:
        return self._age
    
    @age.setter
    def age(self, new_value: int) -> None:
        if isinstance(new_value, int):
            if self._age == new_value:
                return
            else:
                if new_value < 0:
                    raise ValueError("The age cannot be negative.")
                self._age = new_value
        else: 
            TypeError("The new age must be an int.")

    @property
    def company(self):
        return self._company
    
    def change_company(self, company: Company):
        """Change the company associated with the person."""
        if isinstance(company, Company):
            self._company = company
        else:
            raise TypeError("The company must be an instance of the Company class.")
    
    def to_dict(self) -> dict:
        result = {
            "name": self.name, 
            "first_name": self.first_name, 
            "age": self.age
        }
        # "age": self.age,
        # # TODO: property address
        # "address": self._address.to_dict()})
        # Include company information if associated
        if self.company:
            result['company'] = str(self.company)
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
        self._courses = []  # List to store instances of Course
    
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

    def add_course(self, course: Course):
        """Add a course to the student's list of courses."""
        self._courses.append(course)

    def show_courses(self):
        """Display all the courses of the student."""
        if not self._courses:
            print(f"Student {self.first_name} {self.name} is not enrolled in any courses.")
        else:
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



f = Faker()
list_of_persons : list[Person] = \
    [Person(f.name().split()[0], f.name().split()[1], randint(1,100)) for _ in range(36)]
list_of_students : list[Student] = \
    [Student(f.name().split()[0], f.name().split()[1], randint(12,100), f"{str(f.city())} University") for _ in range(36)]


for p in list_of_persons + list_of_students:
    p.introduce_self()
