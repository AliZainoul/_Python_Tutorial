'''

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


class B:
    """Class B demonstrates a simple class with one member variable.

    Like class A, it will be used as a parent class in a multiple inheritance example.
    """

    def __init__(self, b_value):
        """Initialize an instance of class B.

        Args:
            b_value: The value to assign to `member_b`.
        """
        self.member_b = b_value


class C(B, A):
    """Class C inherits from both A and B to demonstrate multiple inheritance.

    This class explicitly initializes both parent classes (`A` and `B`)
    using their constructors, rather than relying on `super()`. This approach
    gives explicit control over initialization order and arguments.

    Note:
        This is an example of **non-cooperative multiple inheritance**,
        where each parent class is initialized manually.
    """

    def __init__(self, x, y):
        """Initialize an instance of class C.

        Args:
            x: The value passed to class A's constructor.
            y: The value passed to class B's constructor.
        """
        A.__init__(self, x)
        B.__init__(self, y)
        


def main():
    """Demonstrate multiple inheritance using classes A, B, and C.

    This function creates an instance of class C, which inherits
    from both A and B, and prints its initialized attributes.

    Example:
        >>> c = C(1, 2)
        >>> print(c.member_a)
        1
        >>> print(c.member_b)
        2
    """
    c = C(1, 2)
    print(f"{c.member_a = }")
    print(f"{c.member_b = }")


if __name__ == "__main__":
    main()

'''

'''
class A:
    """Base class A demonstrating cooperative multiple inheritance.

    This class defines a member variable `member_a` and uses `super().__init__(**kwargs)`
    to ensure that other parent classes in the inheritance chain are properly initialized.

    By using `**kwargs`, it can accept and forward additional arguments
    without breaking the constructor chain.
    """

    def __init__(self, **kwargs):
        """Initialize class A.

        Args:
            **kwargs: Arbitrary keyword arguments that may include `a_value`.
                - `a_value` (optional): Value to assign to `member_a`.
        """
        self.member_a = kwargs.pop("a_value", None)
        super().__init__(**kwargs)


class B:
    """Base class B demonstrating cooperative multiple inheritance.

    Like class A, it uses `super()` to call the next constructor in the
    Method Resolution Order (MRO), ensuring consistent initialization across all bases.
    """

    def __init__(self, **kwargs):
        """Initialize class B.

        Args:
            **kwargs: Arbitrary keyword arguments that may include `b_value`.
                - `b_value` (optional): Value to assign to `member_b`.
        """
        self.member_b = kwargs.pop("b_value", None)
        super().__init__(**kwargs)


class C(B, A):
    """Class C inheriting from both B and A using cooperative multiple inheritance.

    This class does not need to manually call each parent constructor.
    Instead, `super()` ensures that both A and B are initialized in the correct order
    according to the Method Resolution Order (MRO).

    Note:
        This design pattern ensures clean, extensible, and predictable initialization.
    """

    def __init__(self, **kwargs):
        """Initialize class C.

        Args:
            **kwargs: Arbitrary keyword arguments forwarded to parent constructors.
        """
        super().__init__(**kwargs)


def main():
    """Demonstrate cooperative multiple inheritance with `super()` and `**kwargs`.

    This function creates an instance of `C` by passing values for both A and B.
    The initialization chain automatically handles argument dispatching
    through `**kwargs`.

    Example:
        >>> c = C(a_value=1, b_value=2)
        >>> print(c.member_a)
        1
        >>> print(c.member_b)
        2
    """
    c = C(a_value=1, b_value=2)
    print(f"{c.member_a = }")
    print(f"{c.member_b = }")


if __name__ == "__main__":
    main()
'''

class A:
    """Base class A demonstrating cooperative multiple inheritance.

    This class defines a member variable `member_a`.

    By using `*args`, it can accept and forward additional arguments
    without breaking the constructor chain.
    """

    def __init__(self, *args):
        """Initialize class A.

        Args:
            **kwargs: Arbitrary keyword arguments that may include `a_value`.
                - `a_value` (optional): Value to assign to `member_a`.
        """
        self.member_a = args[1]

class B:
    """Base class B demonstrating cooperative multiple inheritance.

    Like class A, it uses `super()` to call the next constructor in the
    Method Resolution Order (MRO), ensuring consistent initialization across all bases.
    """

    def __init__(self, *args):
        """Initialize class B.

        Args:
            *args: Arbitrary keyword arguments that may include `b_value`.
                - `b_value` (optional): Value to assign to `member_b`.
        """
        self.member_b = args[0]
        super().__init__(*args)


class C(B, A):
    """Class C inheriting from both B and A using cooperative multiple inheritance.

    This class does not need to manually call each parent constructor.
    Instead, `super()` ensures that both A and B are initialized in the correct order
    according to the Method Resolution Order (MRO).

    Note:
        This design pattern ensures clean, extensible, and predictable initialization.
    """

    def __init__(self, *args):
        """Initialize class C.

        Args:
            *args: Arbitrary keyword arguments forwarded to parent constructors.
        """
        super().__init__(*args)


def main():
    """Demonstrate cooperative multiple inheritance with `super()` and `*args`.

    This function creates an instance of `C` by passing values for both A and B.
    The initialization chain automatically handles argument dispatching
    through `*args`.

    Example:
        >>> c = C(1, 2)
        >>> print(c.member_a)
        1
        >>> print(c.member_b)
        2
    """
    c = C(2, 1)
    print(f"{c.member_a = }")
    print(f"{c.member_b = }")


if __name__ == "__main__":
    main()

