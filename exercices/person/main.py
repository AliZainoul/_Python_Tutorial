from random import randint
from faker import Faker
from person import Person
from student import Student
from company import Company
from course import Course


def main():
    f = Faker()
    company = Company(str(f.company()), "")

    course1 = Course("Math 101", 3)
    course2 = Course("History 201", 4)
    
    list_persons = [
        Person(f.name(), f.name(), randint(18, 70), company) if randint(0, 1) == 0 
        else Student(f.name(), f.name(), randint(18, 70), f"{str(f.city())} University", company) 
        for _ in range(36)
    ]

    for student in list_persons:
        if isinstance(student, Student):
            student.addCourse(course1 if randint(0,1) == 0 else course2)

    for person in list_persons:
        if not isinstance(person, Student):
            person.introduceSelf()
        else:
            person.introduceSelf()
            person.displayCourses()




if __name__ == "__main__":
    main()
