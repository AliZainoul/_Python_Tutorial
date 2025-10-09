class A:
    """Class A demonstrates a simple class with one member variable.

    This class serves as a base class for demonstrating multiple inheritance.
    It defines a single attribute initialized at object creation.
    """

    def __init__(self, a_value):
        """Initialize an instance of class A.

        Args:
            a_value: The value to assign to `member_a`.
        """
        self.member_a = a_value


class B(A):

    def __init__(self, a_value, b_value):
        """Initialize an instance of class B.

        Args:
            b_value: The value to assign to `member_b`.
        """
        super().__init__(a_value)
        self.member_b = b_value

def main():
    """
    Demonstrate single inheritance using classes A and B.
    """
    b = B(1, 2)
    print(f"{b.member_a = }")
    print(f"{b.member_b = }")


if __name__ == "__main__":
    main()