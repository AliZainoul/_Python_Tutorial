"""
This script summarizes the properties of Python's built-in data structures:
strings, lists, tuples, sets, frozensets, and dictionaries.
It analyzes each structure for uniqueness, assignability, order, mutability,
hashability, and copiableness, and prints a formatted comparison table.
"""

from typing import Any, Dict, List


def print_line(title: str) -> None:
    """
    Print a formatted title line centered and flanked by dashes.
    """
    print("\n" + "-" * 25 + f" {title.upper()} " + "-" * 25)


def is_mutable(obj: Any) -> bool:
    """
    Determine mutability by attempting to modify a copy of the object.
    Uses structural pattern matching (match-case).

    Parameters
    ----------
    obj : Any
        The object to test.

    Returns
    -------
    bool
        True if the object can be modified, False otherwise.
    """
    try:
        match obj:
            case list() as lst:
                lst_copy = lst.copy()
                lst_copy[0] = lst_copy[0]
            case dict() as dct:
                dct_copy = dct.copy()
                key = next(iter(dct_copy)) if dct_copy else "test"
                dct_copy[key] = dct_copy.get(key, 1)
            case set() as st:
                st_copy = st.copy()
                st_copy.add(None)
                st_copy.remove(None)
            # case str():
            #     obj[0] = "X"  # Immutable → will raise
            # case tuple():
            #     obj[0] = obj[0]  # Immutable → will raise
            # case frozenset():
            #     obj.add(None)  # Immutable → will raise
            case _:
                return False
        return True
    except Exception:
        return False


def get_structure_properties(container: Any) -> Dict[str, str | bool]:
    """
    Analyze Python built-in data structures for their core properties.

    Parameters
    ----------
    container : Any
        The container to analyze.

    Returns
    -------
    Dict[str, str | bool]
        A dictionary describing the structure properties.
    """
    cls_name = type(container).__name__

    match container:
        case str() | list() | tuple() | dict():
            ordered = True
        case _:
            ordered = False

    match container:
        case set() | frozenset():
            unique = True
        case _:
            unique = False

    assignable = hasattr(container, "__setitem__")
    mutable = is_mutable(container)
    hashable = not mutable and hasattr(container, "__hash__") and container.__hash__ is not None
    copiable = hasattr(container, "copy")

    return {
        "Data Structure": cls_name.upper(),
        "Unique": unique,
        "Assignable": assignable,
        "Ordered": ordered,
        "Mutable": mutable,
        "Hashable": hashable,
        "Copiable": copiable,
    }


def get_structures() -> List[Any]:
    """
    Get a list of Python built-in data structures for analysis.

    Returns
    -------
    List[Any]
        A list containing instances of various data structures.
    """
    return [
        "hello",
        (1, 2, 3),
        frozenset({1, 2, 3}),
        [1, 2, 3],
        {1, 2, 3},
        {"a": 1, "b": 2, "c": 3},
    ]

def print_struct_table() -> None:
    """
    Print a formatted table comparing Python data structures.
    """
    structures: List[Any] = get_structures()

    headers = ["Data Structure", "Unique", "Assignable", "Ordered", "Mutable", "Hashable", "Copiable"]
    print("-" * 90)
    print("{:<15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(*headers))
    print("-" * 90)

    for obj in structures:
        info = get_structure_properties(obj)
        print(
            "{:<15} {:<12} {:<12} {:<12} {:<12} {:<12} {:<12}".format(
                info["Data Structure"],
                "✅" if info["Unique"] else "❌",
                "✅" if info["Assignable"] else "❌",
                "✅" if info["Ordered"] else "❌",
                "✅" if info["Mutable"] else "❌",
                "✅" if info["Hashable"] else "❌",
                "✅" if info["Copiable"] else "❌",
            )
        )
    print("-" * 90)

def describe_properties(container: Any) -> None:
    """
    Print textual descriptions for each property of a Python data structure.

    Parameters
    ----------
    container : Any
        The container to describe.
    """
    cls_name = type(container).__name__
    print_line(f"{cls_name} Description")

    # Ordered
    if isinstance(container, (list, tuple, str, dict)):
        print("ORDERED: Elements (or keys) have a defined order; iteration preserves it.")
    else:
        print("ORDERED: ❌ No guaranteed order in iteration.")

    # Unique
    if isinstance(container, (set, frozenset)):
        print("UNIQUE: Only distinct elements are allowed; duplicates are removed automatically.")
    elif isinstance(container, dict):
        print("UNIQUE: Keys must be unique; values can be duplicated.")
    else:
        print("UNIQUE: Elements or characters can be duplicated.")

    # Assignable
    if hasattr(container, "__setitem__"):
        print("ASSIGNABLE: Supports item assignment using indexing or keys.")
    else:
        print("ASSIGNABLE: ❌ Cannot directly assign to elements via indexing or keys.")

    # Mutable
    print(f"MUTABLE: {'✅ Can be changed after creation.' if is_mutable(container) else '❌ Immutable; cannot change elements after creation.'}")

    # Hashable
    if not is_mutable(container) and hasattr(container, "__hash__") and container.__hash__ is not None:
        print("HASHABLE: Can be used as a dictionary key or added to a set.")
    else:
        print("HASHABLE: ❌ Cannot be used as a dictionary key or added to a set.")

    # Copiable
    if hasattr(container, "copy"):
        print("COPIABLE: Provides a copy() method for creating shallow copies.")
    else:
        print("COPIABLE: ❌ No copy() method available; manual copying required.")

def main() -> None:
    """
    Main entry point: display a formatted summary table of data structure properties.
    """
    print(" ########## Python Data Structures Properties Table ########## \n")
    print_struct_table()

    for struct in get_structures():
        describe_properties(struct)

if __name__ == "__main__":
    main()
