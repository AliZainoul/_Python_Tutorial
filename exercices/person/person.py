from address import Address
from company import Company


class Person:
    def __init__(self, name: str, firstName: str, age: int, company: Company):
        self.name = name
        self.firstName = firstName
        self.age = age
        self.address = Address()
        self.company = company

    def changeCompany(self, company: Company) -> None:
        self.company = company

    def introduceSelf(self) -> None:
        print(f"Name: {self.name}, First Name: {self.firstName}, Age: {self.age}, Address: {self.address}, Company = {self.company} \n")
