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


def main():
    """Demonstrate multilevel inheritance (A → B → C)."""
    c = C(1, 2, 3)
    c.show_a()
    c.show_b()
    c.show_c()


if __name__ == "__main__":
    main()
