class A:
    """Base class A representing the root of the hierarchy.

    Attributes:
        member_a (int): Shared attribute across all subclasses.
    """

    def __init__(self, a_value: int):
        """Initialize class A with its core attribute."""
        self.member_a = a_value

    def show_a(self) -> None:
        """Display the value of member_a."""
        print(f"A: member_a = {self.member_a}")


class B(A):
    """Class B inheriting from A (first branch).

    Attributes:
        member_b (int): Attribute specific to B.
    """

    def __init__(self, a_value: int, b_value: int):
        """Initialize B and call A’s constructor."""
        super().__init__(a_value)
        self.member_b = b_value

    def show_b(self) -> None:
        """Display both member_a and member_b."""
        print(f"B: member_a = {self.member_a}, member_b = {self.member_b}")


class E(A):
    """Class E inheriting from A (second branch).

    Attributes:
        member_e (int): Attribute specific to E.
    """

    def __init__(self, a_value: int, e_value: int):
        """Initialize E and call A’s constructor."""
        super().__init__(a_value)
        self.member_e = e_value

    def show_e(self) -> None:
        """Display both member_a and member_e."""
        print(f"E: member_a = {self.member_a}, member_e = {self.member_e}")


class C(B):
    """Class C inheriting from B (multilevel from A → B → C).

    Attributes:
        member_c (int): Attribute specific to C.
    """

    def __init__(self, a_value: int, b_value: int, c_value: int):
        """Initialize C by chaining constructors from B and A."""
        super().__init__(a_value, b_value)
        self.member_c = c_value

    def show_c(self) -> None:
        """Display the full inheritance chain for C."""
        print(f"C: member_a = {self.member_a}, member_b = {self.member_b}, member_c = {self.member_c}")


class D(B):
    """Class D inheriting from B (multilevel from A → B → D).

    Attributes:
        member_d (int): Attribute specific to D.
    """

    def __init__(self, a_value: int, b_value: int, d_value: int):
        """Initialize D by chaining constructors from B and A."""
        super().__init__(a_value, b_value)
        self.member_d = d_value

    def show_d(self) -> None:
        """Display the full inheritance chain for D."""
        print(f"D: member_a = {self.member_a}, member_b = {self.member_b}, member_d = {self.member_d}")


class F(E):
    """Class F inheriting from E (multilevel from A → E → F).

    Attributes:
        member_f (int): Attribute specific to F.
    """

    def __init__(self, a_value: int, e_value: int, f_value: int):
        """Initialize F by chaining constructors from E and A."""
        super().__init__(a_value, e_value)
        self.member_f = f_value

    def show_f(self) -> None:
        """Display the full inheritance chain for F."""
        print(f"F: member_a = {self.member_a}, member_e = {self.member_e}, member_f = {self.member_f}")


def main():
    """Demonstrate a hybrid inheritance structure combining hierarchical and multilevel patterns."""

    print("=== Instantiating C (A → B → C) ===")
    c = C(10, 20, 30)
    c.show_a()
    c.show_b()
    c.show_c()

    print("\n=== Instantiating D (A → B → D) ===")
    d = D(40, 50, 60)
    d.show_a()
    d.show_b()
    d.show_d()

    print("\n=== Instantiating F (A → E → F) ===")
    f = F(70, 80, 90)
    f.show_a()
    f.show_e()
    f.show_f()


if __name__ == "__main__":
    main()
