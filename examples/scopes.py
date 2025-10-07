# ANSI color codes
RESET = "\033[0m"
COLORS = {
    0: "\033[35m",  # Dark Magenta - global
    1: "\033[34m",  # Dark Blue - function
    2: "\033[32m",  # Dark Green - if-block
    3: "\033[33m",  # Dark Yellow - else-block
    4: "\033[31m",  # Dark Red - nested if
}

# Global scope (Scope 0)
GLOBAL_VAR = "I am global"
print(f"{COLORS[0]}[Scope 0] GLOBAL_VAR: {GLOBAL_VAR}{RESET}")

def my_square(x: float) -> float:
    """
    Illustrates nested scopes while computing the square of a float.
    """
    # Function scope (Scope 1)
    FUNCTION_VAR = "I exist inside my_square"
    print(f"{COLORS[1]}[Scope 1] FUNCTION_VAR: {FUNCTION_VAR}{RESET}")
    print(f"{COLORS[1]}[Scope 1] GLOBAL_VAR: {GLOBAL_VAR}{RESET}")

    if isinstance(x, float):
        # Conditional scope (Scope 2)
        CONDITIONAL_VAR = "I exist inside the if-block"
        print(f"{COLORS[2]}[Scope 2] CONDITIONAL_VAR: {CONDITIONAL_VAR}{RESET}")
        print(f"{COLORS[2]}[Scope 2] x: {x}{RESET}")
        return x ** 2
    else:
        # Else scope (Scope 3)
        ELSE_VAR = "I exist inside the else-block"
        print(f"{COLORS[3]}[Scope 3] ELSE_VAR: {ELSE_VAR}{RESET}")
        if x is None:
            # Nested if scope (Scope 4)
            NESTED_VAR = "I exist inside nested if-block"
            print(f"{COLORS[4]}[Scope 4] NESTED_VAR: {NESTED_VAR}{RESET}")
        print(f"'{x}' must be a float")


if __name__ == "__main__":
    # Calling function with float
    result = my_square(3.0)
    print(f"{COLORS[0]}Result: {result}{RESET}")

    # Calling function with non-float
    my_square("hello")
