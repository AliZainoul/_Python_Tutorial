"""
copy_set__.py
=================

Demonstrates the difference between:
- Assignment copy
- Operator copy ([:]) ❌ Not applicable for sets
- Shallow copy (.copy())
- Deep copy (copy.deepcopy())

It prints clear tables showing how changes in the original set
affect each type of copy.

Note:
    Sets require their elements to be hashable (immutable). 
    Therefore, nested mutable elements like lists, sets, or dicts cannot be included.
    We can include immutable nested objects like tuples.
"""

import copy
import pprint

# ============================================================
# CONSTANTS
# ============================================================

COLUMN_TITLES = [
    "Original set",
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
    if isinstance(obj, (set, list, tuple)):
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
    Create the original set and its various copy forms.

    Returns
    -------
    tuple : (original, assigning, operator_copy, shallow_copy, deep_copy)
    """
    # Sets require elements to be hashable, so we can include a nested tuple
    original        : set = {1, (2, 3), 4}  
    assigning       : set = original                # same object
    operator_copy   = "❌ Not supported for sets"  # slicing [:] invalid
    shallow_copy    : set = original.copy()        # shallow copy
    deep_copy       : set = copy.deepcopy(original)

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
    print(f"id(original) == id(operator_copy): ❌ Not applicable")
    print(f"id(original) == id(shallow_copy):  {id(original) == id(shallow_copy)}")
    print(f"id(original) == id(deep_copy):     {id(original) == id(deep_copy)}")


def show_object_ids(original, assigning, operator_copy, shallow_copy, deep_copy) -> None:
    print_section("OBJECT IDS (Top-level)")
    for name, obj in zip(COLUMN_TITLES, [original, assigning, operator_copy, shallow_copy, deep_copy]):
        if isinstance(obj, set):
            print(f"{name:<20}: {id(obj)}")
        else:
            print(f"{name:<20}: {obj}")


# ============================================================
# TABLE DISPLAY
# ============================================================

def show_table_state(label: str, sets_tuple: tuple) -> None:
    print(label)
    print_table_row(*sets_tuple)
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

    # Modify the set by adding an element
    show_state("# Before adding 69 to original")
    original.add(69)
    show_state("# After adding 69 to original")

    # Modify the set by removing an element
    show_state("# Before removing 1 from original")
    original.remove(1)
    show_state("# After removing 1 from original")


# ============================================================
# ENTRY POINT
# ============================================================

def main() -> None:
    demonstrate_copy_behavior()


if __name__ == "__main__":
    main()

"""
Set Objects in Python
=====================

Sets are mutable collections of **unique elements**. However, there are specific rules
about what can be included in a set due to the requirement that all elements must be hashable.

Key Characteristics:
--------------------
- **Not subscriptable:** You cannot access elements by index, e.g., `s[0]` raises TypeError.
- **Not assignable by index:** You cannot directly replace elements by position.
- **Mutable via methods:** Sets can be modified using methods like `add()`, `remove()`, or `discard()`.
  Therefore, sets themselves are mutable.

Restrictions on Nested Elements:
-------------------------------
- Sets require **elements to be hashable**. Hashable types include:
    - Immutable built-in types: `int`, `float`, `str`, `tuple` (if all elements are hashable)
    - Custom objects implementing `__hash__` and `__eq__`
- **Mutable types** such as `list`, `dict`, and `set` are **not hashable** and cannot be elements of a set.
- Examples of invalid nested elements:

    ```python
    t = (2, [3, 4])
    original_set = {1, t}  
    # TypeError: unhashable type: 'list'

    l = [2, 3]
    original_set = {1, l, 4}  
    # TypeError: unhashable type: 'list'

    s = {2, 3}
    original_set = {1, s, 4}  
    # TypeError: unhashable type: 'set'

    d = {'a': 2, 'b': 3}
    original_set = {1, d, 4}  
    # TypeError: unhashable type: 'dict'
    ```

Why Tuples Are Allowed:
-----------------------
- Tuples are immutable and hashable **if all their elements are hashable**.
- This means you can include a tuple inside a set, e.g., `{1, (2, 3), 4}`.
- Tuples act as a fixed, hashable container, unlike lists or dicts, whose contents can change and thus cannot guarantee a consistent hash value.

Summary of Hashability Errors:
------------------------------
- `TypeError: unhashable type: 'list'` occurs when a list is used as an element.
- `TypeError: unhashable type: 'set'` occurs when a set is nested inside another set.
- `TypeError: unhashable type: 'dict'` occurs when trying to include a dictionary.
- `TypeError: unhashable type: 'list'` also occurs if a tuple contains a list, since the tuple itself becomes unhashable.

Conclusion:
-----------
- Sets themselves are mutable but their elements must be immutable (hashable).
- Nested immutable objects like tuples are allowed.
- Nested mutable objects like lists, dicts, or sets are not allowed.
"""
