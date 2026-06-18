"""Section 2 - Operators, conditions and loops.

TD/TP Python - Basics & Best Practices - Client Abellis - Juin 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Reference solutions for exercises 2.1 to 2.5.
"""

from random import randint # for exercice 2.2

def fibonacci(n: int) -> list[int]:
    """Return the first n terms of the Fibonacci sequence (F0=0, F1=1).

    Args:
        n: Number of terms to generate (n >= 0).

    Returns:
        A list containing the first n Fibonacci numbers, in order.
    """
    sequence: list[int] = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def exercise_2_1() -> None:
    """Ex 2.1 - Parity, divisibility by 3/5 and FizzBuzz status of an integer."""
    n: int = int(input("Enter a positive integer n : "))

    print(f"{n} is {'even' if n % 2 == 0 else 'odd'}.")
    if n % 3 == 0:
        print(f"{n} is divisible by 3.")
    if n % 5 == 0:
        print(f"{n} is divisible by 5.")

    fizzbuzz: str = (
        "FizzBuzz" if n % 15 == 0
        else "Fizz" if n % 3 == 0
        else "Buzz" if n % 5 == 0
        else str(n)
    )
    print(f"FizzBuzz({n}) -> {fizzbuzz}")


def exercise_2_2() -> None:
    """Ex 2.2 - Guess a fixed secret number within a limited number of attempts."""
    SECRET: int = randint(1, 100)
    MAX_ATTEMPTS: int = 7

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess: int = int(input(f"Attempt {attempt}/{MAX_ATTEMPTS} : "))
        if guess == SECRET:
            print(f"Bravo ! Found in {attempt} attempt{'s' if attempt > 1 else ''}.")
            break
        print("Too large !" if guess > SECRET else "Too small !")
    else:
        print(f"Lost ! The number was {SECRET}.")


def exercise_2_3() -> None:
    """Ex 2.3 - Right triangle, centred isosceles triangle, and diamond, via for/print."""
    n: int = int(input("Height n : "))

    print("Rectangle Triangle :")
    for i in range(1, n + 1):
        print("*" * i)

    print("\nCentered Isosceles Triangle :")
    for i in range(1, n + 1):
        stars = '*' * (2 * i - 1)
        width = 2 * n - 1
        print(f"{stars:^{width}}") # See (*) below for explanation
        # Equivalent to this one-liner : 
        # print(f"{'*' * (2 * i - 1):^{2 * n - 1}}")
    """ (*) Explanation of the f-string format specifier used above:
    :      start of format specifier (see: https://docs.python.org/3/library/string.html#formatstrings)
    ^      center alignment
    {width} dynamic field width
    Example : 
        name = "Python"
        print(f"{name:^20}")
        >>  '       Python       '
        len('       Python       ') == 20
        'Python' is centered inside a field of 20 characters.
    """

    print("\nDiamond :")
    heights: list[int] = [*range(1, n + 1), *range(n - 1, 0, -1)]
    for i in heights:
        stars = '*' * (2 * i - 1)
        width = 2 * n - 1
        print(f"{stars:^{width}}")
        # Equivalent to this one-liner :
        # print(f"{'*' * (2 * i - 1):^{2 * n - 1}}")

def _password_errors(password: str) -> list[str]:
    """Return the list of broken rules for a candidate password, if any."""
    rules: list[tuple[bool, str]] = [
        (len(password) < 8, "at least 8 characters required"),
        (not any(c.isupper() for c in password), "at least one uppercase letter required"),
        (not any(c.islower() for c in password), "at least one lowercase letter required"),
        (not any(c.isdigit() for c in password), "at least one digit required"),
        (any(c.isspace() for c in password), "no spaces allowed"),
    ]
    return [message for broken, message in rules if broken]


def exercise_2_4() -> None:
    """Ex 2.4 - Re-prompt for a password until every security rule is satisfied."""
    while errors := _password_errors(input("Password : ")):
        for error in errors:
            print(f"  - {error}")
    print("Valid password.")


def exercise_2_5() -> None:
    """Ex 2.5 - Generate Fibonacci terms and report threshold statistics."""
    n: int = int(input("Number of terms : "))
    terms: list[int] = fibonacci(n)

    print(", ".join(str(t) for t in terms))
    print(f"Terms < 1000        : {sum(1 for t in terms if t < 1000)}")
    print(f"First term > 10^6 : {next((t for t in terms if t > 10 ** 6), 'none')}")


def main() -> None:
    """Run every Section 2 exercise sequentially with a clear header per exercise."""
    for exercise in (exercise_2_1, exercise_2_2, exercise_2_3, exercise_2_4, exercise_2_5):
        print(f"\n{'=' * 60}\n{exercise.__doc__}\n{'=' * 60}")
        exercise()


if __name__ == "__main__":
    main()