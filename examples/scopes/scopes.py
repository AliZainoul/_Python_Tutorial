"""
Illustrates the notion of logical scopes in Python using ANSI colors.
Each indentation level represents a conceptual scope depth.
"""

from typing import Optional, Any

# ==========================================================
# === ANSI color configuration =============================
# ==========================================================
RESET: str = "\033[0m"  # Reset color (return to default terminal color)

COLORS: dict[str, str] = {
    "MAGENTA": "\033[35m",   # Global (Scope 0)
    "BLUE": "\033[34m",      # Function (Scope 1)
    "GREEN": "\033[32m",     # If-block (Scope 2)
    "YELLOW": "\033[33m",    # Else-block (Scope 3)
    "RED": "\033[31m",       # Nested if (Scope 4)
}

TAB_SIZE = 4  # number of spaces per scope level

# ==========================================================
# === Utility for scope printing ===========================
# ==========================================================
def print_scope(scope: int, color: str, message: str) -> None:
    """Print a message with indentation and color based on scope depth."""
    indent = " " * (scope * TAB_SIZE)
    print(f"{indent}{COLORS[color]}{message}{RESET}")

def print_line(msg: str, color: str = 'GREEN') -> None:
    """Print a centered green separator line with a message."""
    width = 60
    formatted_msg = msg.center(width - 22)
    print(f"{COLORS[color]}{'-' * 10} {formatted_msg} {'-' * 10}{RESET}")


# ==========================================================
# === Global Scope (Scope 0) ===============================
# ==========================================================
GLOBAL_VAR: str = "I am a global variable (GLOBAL_VAR)"
print_scope(0, "MAGENTA", f"[Scope 0] GLOBAL_VAR: {GLOBAL_VAR}")


def my_square(x: Any) -> Optional[float]:
    """Demonstrates logical scope nesting while computing the square of a float."""
    print_line("Entering my_square()")
    print_scope(1, "BLUE", "[Scope 1] FUNCTION_VAR: I exist inside my_square")
    print_scope(1, "BLUE", f"[Scope 1] GLOBAL_VAR: {GLOBAL_VAR}")

    if x is None:
        print_scope(2, "GREEN", "[Scope 2] x is None")
        print_line("Exiting my_square()", "RED")
        return None

    if isinstance(x, float):
        print_scope(2, "GREEN", "[Scope 2] CONDITIONAL_VAR: I exist inside the if-block")
        print_scope(2, "GREEN", f"[Scope 2] x: {x}")

        if x > 0:
            print_scope(3, "GREEN", "[Scope 3] x is positive")
        else:
            print_scope(3, "GREEN", "[Scope 3] x is zero or negative")
        print_line("Exiting my_square()", "RED")
        return x ** 2

    print_scope(3, "YELLOW", "[Scope 3] ELSE_VAR: I exist inside the else-block")

    if isinstance(x, str):
        print_scope(4, "RED", f"[Scope 4] x is a string: '{x}'")
        print_scope(4, "RED", "[Scope 4] Strings cannot be squared.")
    else:
        print_scope(4, "RED", f"[Scope 4] x has type {type(x).__name__}, not float or string.")
        print_scope(4, "RED", "[Scope 4] Cannot compute square for this type.")
    print_line("Exiting my_square()", "RED")
    return None


def main() -> None:
    """Entry point for testing different logical scopes."""
    cases = [
        ("# Case 1: Passing a valid float : 3.0", 3.0),
        ("# Case 2: Passing a string : 'Hello'", "Hello"),
        ("# Case 3: Passing None : None", None),
        ("# Case 4: Passing a list : [1, 2, 3]", [1, 2, 3]),
    ]

    for label, value in cases:
        print_line(label)
        result = my_square(value)
        print(f"{COLORS['MAGENTA']}Result: {result}{RESET}\n")


if __name__ == "__main__":
    main()
