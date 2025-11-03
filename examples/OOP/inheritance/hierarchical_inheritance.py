# ================================
# Hierarchical Inheritance Example
# ================================

class A:
    """Base class A representing the root of the hierarchy.

    Attributes:
        __member_a (int): Shared attribute across all subclasses.
    """

    def __init__(self, a_value: int):
        """Initialize class A with its core attribute."""
        self.__member_a = a_value

    def get_member_a(self) -> int:
        """Return the value of __member_a."""
        return self.__member_a

    def show_a(self) -> None:
        """Display the value of __member_a."""
        print(f"A: member_a = {self.__member_a}")


class B(A):
    """Class B inheriting from A (first branch).

    Attributes:
        __member_b (int): Attribute specific to B.
    """

    def __init__(self, a_value: int, b_value: int):
        """Initialize B and call A’s constructor."""
        super().__init__(a_value)
        self.__member_b = b_value

    def get_member_b(self) -> int:
        """Return the value of __member_b."""
        return self.__member_b

    def show_b(self) -> None:
        """Display both __member_a and __member_b."""
        print(f"B: member_a = {self.get_member_a()}, member_b = {self.__member_b}")


class E(A):
    """Class E inheriting from A (second branch).

    Attributes:
        __member_e (int): Attribute specific to E.
    """

    def __init__(self, a_value: int, e_value: int):
        """Initialize E and call A’s constructor."""
        super().__init__(a_value)
        self.__member_e = e_value

    def get_member_e(self) -> int:
        """Return the value of __member_e."""
        return self.__member_e

    def show_e(self) -> None:
        """Display both __member_a and __member_e."""
        print(f"E: member_a = {self.get_member_a()}, member_e = {self.__member_e}")


class C(B):
    """Class C inheriting from B (multilevel from A → B → C).

    Attributes:
        __member_c (int): Attribute specific to C.
    """

    def __init__(self, a_value: int, b_value: int, c_value: int):
        """Initialize C by chaining constructors from B and A."""
        super().__init__(a_value, b_value)
        self.__member_c = c_value

    def get_member_c(self) -> int:
        """Return the value of __member_c."""
        return self.__member_c

    def show_c(self) -> None:
        """Display the full inheritance chain for C."""
        print(
            f"C: member_a = {self.get_member_a()}, member_b = {self.get_member_b()}, member_c = {self.__member_c}"
        )


class D(B):
    """Class D inheriting from B (multilevel from A → B → D).

    Attributes:
        __member_d (int): Attribute specific to D.
    """

    def __init__(self, a_value: int, b_value: int, d_value: int):
        """Initialize D by chaining constructors from B and A."""
        super().__init__(a_value, b_value)
        self.__member_d = d_value

    def get_member_d(self) -> int:
        """Return the value of __member_d."""
        return self.__member_d

    def show_d(self) -> None:
        """Display the full inheritance chain for D."""
        print(
            f"D: member_a = {self.get_member_a()}, member_b = {self.get_member_b()}, member_d = {self.__member_d}"
        )


class F(E):
    """Class F inheriting from E (multilevel from A → E → F).

    Attributes:
        __member_f (int): Attribute specific to F.
    """

    def __init__(self, a_value: int, e_value: int, f_value: int):
        """Initialize F by chaining constructors from E and A."""
        super().__init__(a_value, e_value)
        self.__member_f = f_value

    def get_member_f(self) -> int:
        """Return the value of __member_f."""
        return self.__member_f

    def show_f(self) -> None:
        """Display the full inheritance chain for F."""
        print(
            f"F: member_a = {self.get_member_a()}, member_e = {self.get_member_e()}, member_f = {self.__member_f}"
        )


# ====================================================
# Hierarchical Inheritance Example (Real-World Version)
# ====================================================

class Vehicle:
    """Base class Vehicle representing the root of the hierarchy.

    Attributes:
        __brand (str): Manufacturer of the vehicle.
        __model (str): Model name or number.
    """

    def __init__(self, brand: str, model: str):
        """Initialize class Vehicle with its core attributes."""
        self.__brand = brand
        self.__model = model

    def get_brand(self) -> str:
        """Return the vehicle brand."""
        return self.__brand

    def get_model(self) -> str:
        """Return the vehicle model."""
        return self.__model

    def show_vehicle(self) -> None:
        """Display the vehicle's brand and model."""
        print(f"Vehicle: brand = {self.__brand}, model = {self.__model}")


class LandVehicle(Vehicle):
    """Class LandVehicle inheriting from Vehicle (first branch).

    Attributes:
        __wheels (int): Number of wheels.
    """

    def __init__(self, brand: str, model: str, wheels: int):
        """Initialize LandVehicle and call Vehicle’s constructor."""
        super().__init__(brand, model)
        self.__wheels = wheels

    def get_wheels(self) -> int:
        """Return the number of wheels."""
        return self.__wheels

    def show_land_vehicle(self) -> None:
        """Display brand, model, and number of wheels."""
        print(
            f"LandVehicle: brand = {self.get_brand()}, model = {self.get_model()}, wheels = {self.__wheels}"
        )


class WaterVehicle(Vehicle):
    """Class WaterVehicle inheriting from Vehicle (second branch).

    Attributes:
        __propulsion (str): Type of propulsion (e.g., motor, sail).
    """

    def __init__(self, brand: str, model: str, propulsion: str):
        """Initialize WaterVehicle and call Vehicle’s constructor."""
        super().__init__(brand, model)
        self.__propulsion = propulsion

    def get_propulsion(self) -> str:
        """Return the propulsion type."""
        return self.__propulsion

    def show_water_vehicle(self) -> None:
        """Display brand, model, and propulsion type."""
        print(
            f"WaterVehicle: brand = {self.get_brand()}, model = {self.get_model()}, propulsion = {self.__propulsion}"
        )


class Car(LandVehicle):
    """Class Car inheriting from LandVehicle (multilevel from Vehicle → LandVehicle → Car).

    Attributes:
        __seats (int): Number of seats in the car.
    """

    def __init__(self, brand: str, model: str, wheels: int, seats: int):
        """Initialize Car by chaining constructors from LandVehicle and Vehicle."""
        super().__init__(brand, model, wheels)
        self.__seats = seats

    def get_seats(self) -> int:
        """Return the number of seats."""
        return self.__seats

    def show_car(self) -> None:
        """Display the full inheritance chain for Car."""
        print(
            f"Car: brand = {self.get_brand()}, model = {self.get_model()}, wheels = {self.get_wheels()}, seats = {self.__seats}"
        )


class Truck(LandVehicle):
    """Class Truck inheriting from LandVehicle (multilevel from Vehicle → LandVehicle → Truck).

    Attributes:
        __capacity (int): Cargo capacity in kilograms.
    """

    def __init__(self, brand: str, model: str, wheels: int, capacity: int):
        """Initialize Truck by chaining constructors from LandVehicle and Vehicle."""
        super().__init__(brand, model, wheels)
        self.__capacity = capacity

    def get_capacity(self) -> int:
        """Return the truck's cargo capacity."""
        return self.__capacity

    def show_truck(self) -> None:
        """Display the full inheritance chain for Truck."""
        print(
            f"Truck: brand = {self.get_brand()}, model = {self.get_model()}, wheels = {self.get_wheels()}, capacity = {self.__capacity} kg"
        )


class Boat(WaterVehicle):
    """Class Boat inheriting from WaterVehicle (multilevel from Vehicle → WaterVehicle → Boat).

    Attributes:
        __length (float): Length of the boat in meters.
    """

    def __init__(self, brand: str, model: str, propulsion: str, length: float):
        """Initialize Boat by chaining constructors from WaterVehicle and Vehicle."""
        super().__init__(brand, model, propulsion)
        self.__length = length

    def get_length(self) -> float:
        """Return the boat's length."""
        return self.__length

    def show_boat(self) -> None:
        """Display the full inheritance chain for Boat."""
        print(
            f"Boat: brand = {self.get_brand()}, model = {self.get_model()}, propulsion = {self.get_propulsion()}, length = {self.__length} m"
        )


def main():
    """Demonstrate a hybrid inheritance structure combining hierarchical and multilevel patterns."""

    print("--- Hierarchical Inheritance (Generic) ---")
    print("Demonstrate hierarchical + multilevel inheritance (A → B → C / D and A → E → F).")

    c = C(10, 20, 30)
    c.show_a()
    c.show_b()
    c.show_c()

    d = D(40, 50, 60)
    d.show_a()
    d.show_b()
    d.show_d()

    f = F(70, 80, 90)
    f.show_a()
    f.show_e()
    f.show_f()

    print(f"\n{C.__mro__ = }")
    print(f"{D.__mro__ = }")
    print(f"{F.__mro__ = }\n")

    print("--- Hierarchical Inheritance (Real-World) ---")
    print("Demonstrate hierarchical + multilevel inheritance using vehicles.")

    car = Car("Toyota", "Corolla", wheels=4, seats=5)
    car.show_vehicle()
    car.show_land_vehicle()
    car.show_car()

    truck = Truck("Volvo", "FH16", wheels=18, capacity=25000)
    truck.show_vehicle()
    truck.show_land_vehicle()
    truck.show_truck()

    boat = Boat("Bayliner", "VR5", propulsion="motor", length=6.2)
    boat.show_vehicle()
    boat.show_water_vehicle()
    boat.show_boat()

    print(f"\n{Car.__mro__ = }")
    print(f"{Truck.__mro__ = }")
    print(f"{Boat.__mro__ = }")


if __name__ == "__main__":
    main()
