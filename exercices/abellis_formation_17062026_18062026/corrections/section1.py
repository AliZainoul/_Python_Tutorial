"""Section 1 - Prints and Inputs (print / input).

TD/TP Python - Basics & Best Practices - Client Abellis - Juin 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Reference solutions for exercises 1.1 to 1.4.
"""


def exercise_1_1() -> None:
    """Ex 1.1 - Greet the user with an f-string, all variables type-annotated."""
    first_name: str = input("What is your first name ? ").strip()
    print(f"Hello, {first_name} !")
    print("Hello and welcome to the Python world.")


def exercise_1_2() -> None:
    """Ex 1.2 - Basic calculator: sum, difference, product, safe quotient."""
    a: float = float(input("First number (a) : "))
    b: float = float(input("Second number (b) : "))

    print(f"Sum      : {round(a + b, 2)}")
    print(f"Difference : {round(a - b, 2)}")
    print(f"Product    : {round(a * b, 2)}")
    if b != 0:
        print(f"Quotient   : {round(a / b, 2)}")
    else:
        print("Quotient   : division by zero impossible")


def exercise_1_3() -> None:
    """Ex 1.3 - Identity card with f-string column alignment (:<, :>)."""
    first_name: str = input("First name : ").strip()
    last_name: str = input("Last name : ").strip()
    birth_year: int = int(input("Birth year : "))
    city: str = input("City : ").strip()

    age: int = 2026 - birth_year
    LABEL_WIDTH: int = 7
    SEPARATOR: str = "=" * 30

    print(SEPARATOR)
    print(f"{'Name:':<{LABEL_WIDTH}}{last_name}, {first_name}")
    print(f"{'Age:':<{LABEL_WIDTH}}{age} years")
    print(f"{'City:':<{LABEL_WIDTH}}{city}")
    print(SEPARATOR)


def exercise_1_4() -> None:
    """Ex 1.4 - Multiplication table of n, then all tables 1..n side by side."""
    n: int = int(input("n = "))

    print(f"\nTable of {n} :")
    for i in range(1, 11):
        print(f"{n} x {i:>2} = {n * i:>3}")

    print("\nTables 1 to n side by side:")
    for i in range(1, 11):
        row: str = "   ".join(f"{table} x {i:>2} = {table * i:>3}" for table in range(1, n + 1))
        print(row)


def main() -> None:
    """Run every Section 1 exercise sequentially with a clear header per exercise."""
    for exercise in (exercise_1_1, exercise_1_2, exercise_1_3, exercise_1_4):
        print(f"\n{'=' * 60}\n{exercise.__doc__}\n{'=' * 60}")
        exercise()


if __name__ == "__main__":
    main()
