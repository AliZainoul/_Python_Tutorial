"""Section 5 - Exception handling.

Python TD/TP - Basics & Best Practices - Abellis Client - June 2026
Trainer : Mr. Ali ZAINOUL - CrystalClearCode (https://clearcode.fr)

Reference solutions for exercises 5.1 to 5.4.
"""

# --------------------------------------------------------------------------- #
# Exercise 5.1 - Robust converter
# --------------------------------------------------------------------------- #


def safe_int(value: str | None) -> int | None:
    """Convert a value to int, returning None instead of raising an error on failure.

    Args:
        value: The candidate value (typically a string, but None is accepted).

    Returns:
        The converted integer, or None if conversion is not possible.
    """
    try:
        return int(value)  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return None


# --------------------------------------------------------------------------- #
# Exercise 5.2 - Safe file reader
# --------------------------------------------------------------------------- #


def read_file(path: str) -> list[str]:
    """Read a text file line by line without raising errors for missing or inaccessible files.

    Uses a 'with' block, which ensures the file is properly closed even if an
    exception occurs during reading.

    Args:
        path: Path to the file to read.

    Returns:
        A list of lines (without trailing newline characters), or an empty list
        if the file does not exist or cannot be accessed.
    """
    try:
        with open(path, encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        print(f"File not found: {path}")
        return []
    except PermissionError:
        print(f"Permission denied: {path}")
        return []


# --------------------------------------------------------------------------- #
# Exercise 5.3 - Custom exceptions: bank account
# --------------------------------------------------------------------------- #


class InsufficientFundsError(ValueError):
    """Raised when a withdrawal exceeds the available account balance."""

    def __init__(self, amount: float) -> None:
        """Store the overdraft amount that triggered the exception."""
        self.amount = amount
        super().__init__(f"insufficient funds: overdraft of {amount:.2f}")


def withdraw(balance: float, amount: float) -> float:
    """Withdraw an amount from the balance while enforcing business rules.

    Args:
        balance: Current account balance.
        amount: Amount to withdraw; must be strictly positive.

    Returns:
        The new balance after withdrawal.

    Raises:
        ValueError: If the amount is zero or negative.
        InsufficientFundsError: If the amount exceeds the available balance.
    """
    if amount <= 0:
        raise ValueError("withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientFundsError(amount - balance)
    return balance - amount


# --------------------------------------------------------------------------- #
# Exercise 5.4 - Email validation chain
# --------------------------------------------------------------------------- #


def validate_email(email: str) -> str:
    """Validate an email address using three simple structural rules.

    Rules are checked independently (no nested conditions):
    - exactly one '@'
    - a domain containing at least one '.'
    - total length between 6 and 254 characters

    Args:
        email: The email address to validate.

    Returns:
        The same email, unchanged, if it is valid.

    Raises:
        ValueError: If any validation rule is violated.
    """
    if not 6 <= len(email) <= 254:
        raise ValueError("email length must be between 6 and 254 characters")
    if email.count("@") != 1:
        raise ValueError("email must contain exactly one '@'")
    if "." not in email.split("@", 1)[1]:
        raise ValueError("email domain must contain at least one '.'")
    return email


# --------------------------------------------------------------------------- #
# Exercise runners
# --------------------------------------------------------------------------- #


def exercise_5_1() -> None:
    """Ex 5.1 - safe_int never raises, even on invalid input."""
    for sample in ("42", "3.14", "abc", "", None):
        print(f"safe_int({sample!r}) -> {safe_int(sample)}")


def exercise_5_2() -> None:
    """Ex 5.2 - read_file fails gracefully on missing or forbidden paths."""
    print(f"read_file('/nonexistent.txt') -> {read_file('/nonexistent.txt')}")


def exercise_5_3() -> None:
    """Ex 5.3 - Interactive console menu: deposit, withdraw, show balance."""
    balance: float = 0.0

    while True:
        choice: str = input("\n1) Deposit  2) Withdraw  3) Balance  4) Quit\n> ").strip()

        match choice:
            case "1":
                balance += float(input("Deposit amount: "))

            case "2":
                try:
                    balance = withdraw(balance, float(input("Withdrawal amount: ")))
                except InsufficientFundsError as e:
                    print(f"Insufficient balance (overdraft of {e.amount:.2f}).")
                except ValueError as e:
                    print(f"Invalid amount: {e}")

            case "3":
                print(f"Current balance: {balance:.2f}")

            case "4":
                break

            case _:
                print("Invalid choice.")


def exercise_5_4() -> None:
    """Ex 5.4 - Validate an email address entered from the console."""
    email: str = input("Email to validate: ")
    try:
        validate_email(email)
        print("Valid email.")
    except ValueError as e:
        print(f"Invalid email: {e}")


def main() -> None:
    """Run all Section 5 exercises sequentially with clear headers."""
    for exercise in (exercise_5_1, exercise_5_2, exercise_5_3, exercise_5_4):
        print(f"\n{'=' * 60}\n{exercise.__doc__}\n{'=' * 60}")
        exercise()


if __name__ == "__main__":
    main()