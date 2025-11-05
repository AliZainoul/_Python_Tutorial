"""
copy_list__.py
=================

Demonstrates the difference between:
- Assignment copy
- Operator copy ([:])
- Shallow copy (.copy())
- Deep copy (copy.deepcopy())

It prints clear, aligned tables showing how changes in the original list
affect each type of copy at both the top level and nested levels.
"""

import copy
import pprint

# ============================================================
# CONSTANTS
# ============================================================

# Column configuration
COLUMN_TITLES = [
    "Original list",
    "Assigning Copy",
    "Operator Copy",
    "Shallow Copy",
    "Deep Copy",
]
COLUMN_WIDTHS = [35, 35, 35, 35, 35]

TABLE_FORMAT = " ".join(f"{{:<{w}}}" for w in COLUMN_WIDTHS)

CHAR_MAIN_SEP_ = "#"
CHAR_MAIN_SEP = "="
CHAR_SUB_SEP = "-"
LINE_LENGTH = sum(COLUMN_WIDTHS) + len(COLUMN_WIDTHS) - 1

PP = pprint.PrettyPrinter(width=30, compact=True)


# ============================================================
# GENERIC UTILITIES
# ============================================================

def print_separator(char: str = CHAR_SUB_SEP) -> None:
    """Print a horizontal separator line."""
    print(char * LINE_LENGTH)


def format_obj(obj) -> str:
    """Format any Python object for table display using pprint."""
    if isinstance(obj, (dict, list)):
        return PP.pformat(obj)
    return str(obj)


def print_table_row(*cols) -> None:
    """Print a formatted table row aligned according to TABLE_FORMAT."""
    formatted_cols = [format_obj(c) for c in cols]
    print(TABLE_FORMAT.format(*formatted_cols))


def print_table_header() -> None:
    """Print the table header and a main separator."""
    print_separator(CHAR_MAIN_SEP)
    print_table_row(*COLUMN_TITLES)
    print_separator(CHAR_MAIN_SEP)


def print_section(title: str) -> None:
    """Print a titled section divider."""
    print(f"\n{CHAR_MAIN_SEP_ * 20} {title} {CHAR_MAIN_SEP_ * 20}")


# ============================================================
# COPY LOGIC
# ============================================================

def create_all_copies():
    """
    Create the original list and its various copy forms.

    Returns
    -------
    tuple : (original, assigning, operator_copy, shallow_copy, deep_copy)
    """
    original        : list = [1, [2, 3], 4]           # original list
    assigning       : list = original                 # assigning copy (same object)
    operator_copy   : list = original[:]              # slicing (operator) copy
    shallow_copy    : list = original.copy()          # shallow copy
    deep_copy       : list = copy.deepcopy(original)  # deep copy
    return (
        original, 
        assigning,
        operator_copy,
        shallow_copy,
        deep_copy
    )


# ============================================================
# INSPECTION UTILITIES
# ============================================================

def show_reference_tests(original, assigning, operator_copy, shallow_copy, deep_copy) -> None:
    """Print top-level and nested reference identity tests."""
    print_section("REFERENCE TESTS (Top-level)")
    print(f"id(original) == id(assigning):     {id(original) == id(assigning)}")
    print(f"id(original) == id(operator_copy): {id(original) == id(operator_copy)}")
    print(f"id(original) == id(shallow_copy):  {id(original) == id(shallow_copy)}")
    print(f"id(original) == id(deep_copy):     {id(original) == id(deep_copy)}")

    print_section("REFERENCE TESTS (Nested level)")
    print(f"id(original[1]) == id(assigning[1]):     {id(original[1]) == id(assigning[1])}")
    print(f"id(original[1]) == id(operator_copy[1]): {id(original[1]) == id(operator_copy[1])}")
    print(f"id(original[1]) == id(shallow_copy[1]):  {id(original[1]) == id(shallow_copy[1])}")
    print(f"id(original[1]) == id(deep_copy[1]):     {id(original[1]) == id(deep_copy[1])}")


def show_object_ids(original, assigning, operator_copy, shallow_copy, deep_copy) -> None:
    """Print IDs of top-level and nested lists for inspection."""
    print_section("OBJECT IDS (Top-level)")
    for name, obj in zip(COLUMN_TITLES, [original, assigning, operator_copy, shallow_copy, deep_copy]):
        print(f"{name:<20}: {id(obj)}")

    print_section("OBJECT IDS (Nested index [1])")
    for name, obj in zip(COLUMN_TITLES, [original, assigning, operator_copy, shallow_copy, deep_copy]):
        print(f"{name:<20}: {id(obj[1])}")


# ============================================================
# TABLE DISPLAY
# ============================================================

def show_table_state(label: str, lists_tuple: tuple) -> None:
    """Print a labeled state of all copies in a single aligned table row."""
    print(label)
    print_table_row(*lists_tuple)
    print_separator(CHAR_SUB_SEP)


# ============================================================
# MAIN DEMONSTRATION LOGIC
# ============================================================

def demonstrate_copy_behavior() -> None:
    """Run the full demonstration comparing list copy behaviors."""
    # Create all lists
    original, assigning, operator_copy, shallow_copy, deep_copy = create_all_copies()

    # Show object identities and reference behavior
    show_reference_tests(original, assigning, operator_copy, shallow_copy, deep_copy)
    show_object_ids(original, assigning, operator_copy, shallow_copy, deep_copy)

    # Print the main table of values
    print_section("TABLE OF VALUES")
    print_table_header()

    def show_state(msg: str) -> None:
        show_table_state(msg, (original, assigning, operator_copy, shallow_copy, deep_copy))

    # Top-level element modification
    show_state("# Before modification original_list[0] = 5")
    original[0] = 5
    show_state("# After modification original_list[0] = 5")

    # Nested list element modification
    show_state("# Before modification original_list[1][0] = 69")
    original[1][0] = 69
    show_state("# After modification original_list[1][0] = 69")


# ============================================================
# ENTRY POINT
# ============================================================

def main() -> None:
    """Main entry point."""
    demonstrate_copy_behavior()


if __name__ == "__main__":
    main()
