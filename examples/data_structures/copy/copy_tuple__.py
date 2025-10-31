"""
copy_tuple__.py
=================

Demonstrates the difference between:
- Assignment copy
- Operator copy ([:])
- Shallow copy (.copy()) ❌ Not applicable for tuples
- Deep copy (copy.deepcopy())

It prints clear, aligned tables showing how changes in the original tuple
affect each type of copy, using pprint for neat multi-line formatting.
"""

import copy
import pprint

# ============================================================
# CONSTANTS
# ============================================================

COLUMN_TITLES = [
    "Original tuple",
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
    print(char * LINE_LENGTH)


def format_obj(obj) -> str:
    if isinstance(obj, (tuple, list)):
        return PP.pformat(obj)
    return str(obj)


def print_table_row(*cols) -> None:
    formatted_cols = [format_obj(c) for c in cols]
    print(TABLE_FORMAT.format(*formatted_cols))


def print_table_header() -> None:
    print_separator(CHAR_MAIN_SEP)
    print_table_row(*COLUMN_TITLES)
    print_separator(CHAR_MAIN_SEP)


def print_section(title: str) -> None:
    print(f"\n{CHAR_MAIN_SEP_ * 20} {title} {CHAR_MAIN_SEP_ * 20}")


# ============================================================
# COPY LOGIC
# ============================================================

def create_all_copies():
    """
    Create the original tuple and its various copy forms.

    Returns
    -------
    tuple : (original, assigning, operator_copy, shallow_copy, deep_copy)
    """
    original        : tuple = (1, [2, 3], 4)
    assigning       : tuple = original                # same object
    operator_copy   : tuple = original[:]            # shallow copy via slicing
    shallow_copy    = "❌ Not supported for tuples"  # .copy() not available
    deep_copy       : tuple = copy.deepcopy(original)

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
    print_section("REFERENCE TESTS (Top-level)")
    print(f"id(original) == id(assigning):     {id(original) == id(assigning)}")
    print(f"id(original) == id(operator_copy): {id(original) == id(operator_copy)}")
    print(f"id(original) == id(shallow_copy):  ❌ Not applicable")
    print(f"id(original) == id(deep_copy):     {id(original) == id(deep_copy)}")

    print_section("REFERENCE TESTS (Nested key [1])")
    # element [1] is a mutable list inside the tuple
    print(f"id(original[1]) == id(assigning[1]):     {id(original[1]) == id(assigning[1])}")
    print(f"id(original[1]) == id(operator_copy[1]): {id(original[1]) == id(operator_copy[1])}")
    print(f"id(original[1]) == id(shallow_copy[1]):  ❌ Not applicable")
    print(f"id(original[1]) == id(deep_copy[1]):     {id(original[1]) == id(deep_copy[1])}")


def show_object_ids(original, assigning, operator_copy, shallow_copy, deep_copy) -> None:
    print_section("OBJECT IDS (Top-level)")
    for name, obj in zip(COLUMN_TITLES, [original, assigning, operator_copy, shallow_copy, deep_copy]):
        if isinstance(obj, tuple):
            print(f"{name:<20}: {id(obj)}")
        else:
            print(f"{name:<20}: {obj}")

    print_section("OBJECT IDS (Nested element [1])")
    for name, obj in zip(COLUMN_TITLES, [original, assigning, operator_copy, shallow_copy, deep_copy]):
        if isinstance(obj, tuple):
            print(f"{name:<20}: {id(obj[1])}")
        else:
            print(f"{name:<20}: ❌ Not applicable")


# ============================================================
# TABLE DISPLAY
# ============================================================

def show_table_state(label: str, tuples_tuple: tuple) -> None:
    print(label)
    print_table_row(*tuples_tuple)
    print_separator(CHAR_SUB_SEP)


# ============================================================
# MAIN DEMONSTRATION LOGIC
# ============================================================

def demonstrate_copy_behavior() -> None:
    original, assigning, operator_copy, shallow_copy, deep_copy = create_all_copies()

    show_reference_tests(original, assigning, operator_copy, shallow_copy, deep_copy)
    show_object_ids(original, assigning, operator_copy, shallow_copy, deep_copy)

    print_section("TABLE OF VALUES")
    print_table_header()

    def show_state(msg: str) -> None:
        show_table_state(msg, (original, assigning, operator_copy, shallow_copy, deep_copy))

    # Attempt modifications
    show_state("# Before modification original[0] = 99 (immutable, will fail)")
    try:
        original[0] = 99
    except TypeError as e:
        print(f"Cannot modify tuple element: {e}")
    show_state("# After attempted modification original[0]")

    # Nested mutable element modification
    show_state("# Before modification original[1][0] = 69")
    original[1][0] = 69
    show_state("# After modification original[1][0] = 69")


# ============================================================
# ENTRY POINT
# ============================================================

def main() -> None:
    demonstrate_copy_behavior()


if __name__ == "__main__":
    main()
