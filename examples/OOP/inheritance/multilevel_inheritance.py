# ==============================
# Multilevel Inheritance Example
# ==============================
class A:
    """Base class A representing the root of a multilevel inheritance chain.

    Attributes:
        member_a (int): A value specific to class A.
    """

    def __init__(self, a_value: int):
        """Initialize class A with its specific value.

        Args:
            a_value (int): Value assigned to `member_a`.
        """
        self.member_a = a_value

    def show_a(self) -> None:
        """Display the value of member_a."""
        print(f"A: member_a = {self.member_a}")


class B(A):
    """Intermediate class B inheriting from class A.

    Adds its own attribute `member_b` while still maintaining
    access to all attributes and methods of A.
    """

    def __init__(self, a_value: int, b_value: int):
        """Initialize class B with values for both A and B.

        Args:
            a_value (int): Value for `member_a` from class A.
            b_value (int): Value for `member_b` specific to B.
        """
        super().__init__(a_value)
        self.member_b = b_value

    def show_b(self) -> None:
        """Display the values of member_a and member_b."""
        print(f"B: member_a = {self.member_a}, member_b = {self.member_b}")


class C(B):
    """Derived class C demonstrating multilevel inheritance (A → B → C).

    Inherits from B (and transitively from A), adding `member_c`.
    """

    def __init__(self, a_value: int, b_value: int, c_value: int):
        """Initialize class C with values for A, B, and C.

        Args:
            a_value (int): Value for `member_a` (from A).
            b_value (int): Value for `member_b` (from B).
            c_value (int): Value for `member_c` (specific to C).
        """
        super().__init__(a_value, b_value)
        self.member_c = c_value

    def show_c(self) -> None:
        """Display all inherited and specific members."""
        print(
            f"C: member_a = {self.member_a}, member_b = {self.member_b}, member_c = {self.member_c}"
        )

# Real example:
class Vehicle:
    """Class Vehicle represents a generic vehicle with a make."""
    def __init__(self, make):
        """Initialize an instance of class Vehicle.

        Args:
            make: The make of the vehicle.
        """
        self.__make = make

    def get_make(self):
        """Get the make of the vehicle."""
        return self.__make
    
class Car(Vehicle):
    """Class Car represents a Car, inheriting from Vehicle."""
    def __init__(self, make, model):
        """Initialize an instance of class Car.
        Args:
            model: The model of the car.
        """
        super().__init__(make)
        self.__model = model
    
    def get_model(self):
        """Get the model of the car."""
        return self.__model
    
class ElectricCar(Car):
    """Class ElectricCar represents an Electric Car, inheriting from Car."""
    def __init__(self, make, model, battery_capacity):
        """Initialize an instance of class ElectricCar.
        Args:
            battery_capacity: The battery capacity of the electric car.
        """
        super().__init__(make, model)
        self.__battery_capacity = battery_capacity
    
    def get_battery_capacity(self):
        """Get the battery capacity of the electric car."""
        return self.__battery_capacity

def main():
    """Demonstrate multilevel inheritance (C → B → A)."""
    print()
    print("--- Multilevel Inheritance Example ---") 
    print("Demonstrate multilevel inheritance (C → B → A).")
    c = C(1, 2, 3)
    c.show_a()
    c.show_b()
    c.show_c()
    print(f"{C.__mro__ = }")
    print()

    # Real example :
    print("--- Multilevel Inheritance (Real) Example ---")
    print("Demonstrate multilevel inheritance using classes (ElectricCar → Car → Vehicle).")
    electric_car = ElectricCar("Tesla", "Model S", "100 kWh")
    print(f"{electric_car.get_make()= }")
    print(f"{electric_car.get_model()= }")
    print(f"{electric_car.get_battery_capacity()= }")
    print(f"{ElectricCar.__mro__ = }")
    print()

if __name__ == "__main__":
    main()
