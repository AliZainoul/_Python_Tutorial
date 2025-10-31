"""
Comprehensive comparison between using `args` and `*args`
in Python function definitions.

Each function demonstrates a different combination of:
- Argument definition (`args` vs `*args`)
- Print behavior (`args` vs `*args`)

The same set of test inputs (`elements`) is applied to all functions
to highlight their differences in behavior and output.

"""

# ============================================================
# 🎨 COLORS — ANSI escape codes for pretty printing
# ============================================================
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
MAGENTA = "\033[95m"
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"


# ============================================================
# Definition 1 — Single parameter, no unpacking in print
# ============================================================
def print_infos_case1(args):
    """
    Receives a single argument and prints it directly.

    Parameters
    ----------
    args : any
        Any single argument (e.g., list, tuple, int, str, etc.)

    Example
    -------
    >>> print_infos_case1([1, 2, 3])
    [1, 2, 3]
    """
    print(args)


# ============================================================
# Definition 2 — *args in definition, *args in print
# ============================================================
def print_infos_case2(*args):
    """
    Receives multiple positional arguments and unpacks them when printing.

    Parameters
    ----------
    *args : tuple
        A variable number of positional arguments.

    Example
    -------
    >>> print_infos_case2(1, 2, 3)
    1 2 3
    """
    print(*args)


# ============================================================
# Definition 3 — Single parameter, unpacked in print
# ============================================================
def print_infos_case3(args):
    """
    Receives a single iterable argument and unpacks it when printing.

    Parameters
    ----------
    args : iterable
        A single iterable (e.g., list, tuple, set) whose elements will be unpacked.

    Example
    -------
    >>> print_infos_case3([1, 2, 3])
    1 2 3
    """
    print(*args)


# ============================================================
# Definition 4 — *args in definition, printed as tuple
# ============================================================
def print_infos_case4(*args):
    """
    Receives multiple positional arguments and prints the tuple directly.

    Parameters
    ----------
    *args : tuple
        A variable number of positional arguments grouped into a tuple.

    Example
    -------
    >>> print_infos_case4(1, 2, 3)
    (1, 2, 3)
    """
    print(args)


# ============================================================
# TESTS — same dataset for all functions
# ============================================================
if __name__ == "__main__":
    # --------------------------------------------------------
    # 🔹 Categorized test data
    # --------------------------------------------------------
    elements = [
        # --- Sequences ---
        [1, 2, 3],          # List
        (4, 5),             # Tuple
        "Python",           # String
        "1 2 3",            # String with spaces

        # --- Mappings ---
        {"a": 1, "b": 2},   # Dictionary

        # --- Sets ---
        {"x", "y", "z"},    # Set

        # --- Scalars ---
        42,                 # Integer
        3.14,               # Float

        # --- Empty Sequences ---
        [],                 # Empty list
        (),                 # Empty tuple

        # Generator of floats
        (float(el) for el in input("Pleaser enter numbers separated by spaces: ").split()),  
        # User input as floats
        *(float(el) for el in input("Pleaser enter numbers separated by spaces: ").split()),  

    ]

    # ============================================================
    # CASE 1 — def print_infos(args): print(args)
    # ============================================================
    print(f"\n{BOLD}{CYAN}=== Case 1 — Single parameter, no unpacking in print ==={RESET}")
    for el in elements:
        try:
            print(f"{BLUE}Input:{RESET} {repr(el)} → {BLUE}Output:{RESET} ", end="")
            print_infos_case1(el)
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    # ============================================================
    # CASE 2 — def print_infos(*args): print(*args)
    # ============================================================
    print(f"\n{BOLD}{GREEN}=== Case 2 — *args in definition, *args in print ==={RESET}")
    for el in elements:
        try:
            print(f"{BLUE}Input:{RESET} {repr(el)} → {BLUE}Output:{RESET} ", end="")
            print_infos_case2(el)
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    # ============================================================
    # CASE 3 — def print_infos(args): print(*args)
    # ============================================================
    print(f"\n{BOLD}{BLUE}=== Case 3 — Single parameter, unpacked in print ==={RESET}")
    for el in elements:
        try:
            print(f"{BLUE}Input:{RESET} {repr(el)} → {BLUE}Output:{RESET} ", end="")
            print_infos_case3(el)
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    # ============================================================
    # CASE 4 — def print_infos(*args): print(args)
    # ============================================================
    print(f"\n{BOLD}{MAGENTA}=== Case 4 — *args in definition, printed as tuple ==={RESET}")
    for el in elements:
        try:
            print(f"{BLUE}Input:{RESET} {repr(el)} → {BLUE}Output:{RESET} ", end="")
            print_infos_case4(el)
        except Exception as e:
            print(f"{RED}Error: {e}{RESET}")

    # ============================================================
    # END
    # ============================================================
    print(f"\n{BOLD}{GREEN} Comparison complete! Explore the patterns above to master *args behavior.{RESET}\n")
