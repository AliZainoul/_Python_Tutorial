"""Section 3 - Functions, *args et **kwargs.

TD/TP Python - Basics & Best Practices - Client Abellis - Juin 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Reference solutions for exercises 3.1 to 3.5.
"""

import functools
import math

from collections.abc import Callable

# --------------------------------------------------------------------------- #
# Exercise 3.1 - Arithmetic functions with operator dispatch
# --------------------------------------------------------------------------- #


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference a - b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return the quotient a / b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("division by zero is not allowed")
    return a / b


_OPERATIONS: dict[str, Callable[[float, float], float]] = {
    "+": add, "-": subtract, "*": multiply, "/": divide,
}


def calculate(a: float, b: float, op: str) -> float:
    """Dispatch to the arithmetic function matching the given operator.

    Args:
        a: Left operand.
        b: Right operand.
        op: One of '+', '-', '*', '/'.

    Returns:
        The result of applying op to a and b.

    Raises:
        ValueError: If op is not a supported operator.
    """
    try:
        return _OPERATIONS[op](a, b)
    except KeyError:
        raise ValueError(f"unsupported operator: {op!r}") from None


# --------------------------------------------------------------------------- #
# Exercise 3.2 - Descriptive statistics with *args
# --------------------------------------------------------------------------- #


def describe(*values: float) -> dict[str, float | int]:
    """Compute basic descriptive statistics for a variable number of values.

    Median is computed manually, without the 'statistics' module.

    Args:
        *values: One or more numeric values.

    Returns:
        A dict with 'min', 'max', 'mean', 'median' and 'count' keys.

    Raises:
        ValueError: If no value is provided.
    """
    if not values:
        raise ValueError("describe() requires at least one value")

    sorted_values: list[float] = sorted(values)
    count: int = len(sorted_values)
    mid: int = count // 2
    median: float = (
        sorted_values[mid] if count % 2
        else (sorted_values[mid - 1] + sorted_values[mid]) / 2
    )

    return {
        "min": min(values),
        "max": max(values),
        "mean": sum(values) / count,
        "median": median,
        "count": count,
    }


# --------------------------------------------------------------------------- #
# Exercise 3.3 - Report formatter with **kwargs
# --------------------------------------------------------------------------- #


def format_report(title: str, **fields: object) -> str:
    """Format a labelled report: keys left-aligned, values right-aligned.

    Args:
        title: Report title, printed as a header.
        **fields: Arbitrary named fields to display.

    Returns:
        The formatted multi-line report as a single string.
    """
    if not fields:
        return title

    key_width:   int = max(len(key) for key in fields)
    value_width: int = max(len(str(value)) for value in fields.values())

    lines: list[str] = [title, "-" * len(title)]
    lines += [
        f"{key:<{key_width}} : {str(value):>{value_width}}"
        for key, value in fields.items()
    ]
    return "\n".join(lines)


# --------------------------------------------------------------------------- #
# Exercise 3.4 - Recursive factorial and power
# --------------------------------------------------------------------------- #


def factorial(n: int) -> int:
    """Compute n! recursively.

    Args:
        n: A non-negative integer.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("factorial is undefined for negative numbers")
    return 1 if n in (0, 1) else n * factorial(n - 1)


def power(base: float, exp: int) -> float:
    """Compute base ** exp recursively, supporting negative exponents."""
    if exp < 0:
        return 1 / power(base, -exp)
    return 1 if exp == 0 else base * power(base, exp - 1)


# --------------------------------------------------------------------------- #
# Exercise 3.5 - Logging decorator
# --------------------------------------------------------------------------- #


def log_call(func: Callable[..., object]) -> Callable[..., object]:
    """Decorator that logs a function's name, arguments and return value.

    Works for any callable thanks to *args/**kwargs, and preserves the
    wrapped function's metadata via functools.wraps.

    Args:
        func: The function to wrap.

    Returns:
        A wrapped version of func with identical signature and metadata.
    """
    @functools.wraps(func)
    def wrapper(*args: object, **kwargs: object) -> object:
        result = func(*args, **kwargs)
        args_repr: str = ", ".join(repr(a) for a in args)
        kwargs_repr: str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        # {v!r} above is equivalent to {repr(v)}
        signature: str = ", ".join(filter(None, [args_repr, kwargs_repr]))
        print(f"{func.__name__}({signature}) -> {result!r}")
        return result
    return wrapper


def main() -> None:
    """Demonstrate every Section 3 exercise with sample data (non-interactive)."""
    print("Ex 3.1 - calculate(6, 3, '/') =", calculate(6, 3, "/"))

    print("Ex 3.2 - describe(*[2, 4, 4, 4, 5, 5, 7, 9]) =", describe(2, 4, 4, 4, 5, 5, 7, 9))

    print("\nEx 3.3 -")
    print(format_report("Sensor Data", temperature=23.5, pression=1013.25, humidity=62))

    print(f"\nEx 3.4 - factorial(6) = {factorial(6)} (math.factorial: {math.factorial(6)})")
    print(f"Ex 3.4 - power(2, -3) = {power(2, -3)} (** operator: {2 ** -3})")

    print("\nEx 3.5 -")
    logged_add = log_call(add)
    logged_add(2, 3)

    logged_product = log_call(math.prod)
    logged_product([1,2,3])

    # dict example :
    logged_format_report = log_call(format_report)
    logged_format_report("Report", name="Ali", age=32, city="Montpellier")

if __name__ == "__main__":
    main()