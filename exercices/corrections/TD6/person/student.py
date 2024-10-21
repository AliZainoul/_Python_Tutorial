from person import Person
from company import Company
from course import Course


class Student(Person):
    def __init__(self, name: str, firstName: str, age: int, school: str, company: Company):
        super().__init__(name, firstName, age, company)
        self.school = school
        self.courses = []


    def addCourse(self, course: Course) -> None:
        self.courses.append(course)

    def removeCourse(self, course: Course) -> None:
        if course in self.courses:
            self.courses.remove(course)

    def displayCourses(self) -> None:
        for course in self.courses:
            print(course)

    def introduceSelf(self) -> None:
        print(f"Name: {self.name}, First Name: {self.firstName}, Age: {self.age}, School: {self.school}, Address: {self.address}, Company = {self.company} \n")
