from car import Car

car1 = Car("Toyota", "Camry", 2020) 
car2 = Car("Honda", "Accord", 2021) 

print(repr(car1))
print(repr(car2))

car1.set_all("Toyota", "Camry", 2022)
car2.set_all("Honda", "X", 2023)

print(repr(car1))
print(repr(car2))