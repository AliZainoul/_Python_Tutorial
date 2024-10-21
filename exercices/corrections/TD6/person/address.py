from faker import Faker

class Address:
    def __init__(self, street: str = None, city: str = None, postalCode: str = None):
        self.street = street
        self.city = city
        self.postalCode = postalCode

    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.postalCode}"
    
    # TODO:
    # Adding setters for address. 
    