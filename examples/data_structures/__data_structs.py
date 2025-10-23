def printLine(s: str) -> None:
    """
    Prints a line with a title centered and flanked by dashes.

    Parameters
    ----------
    s : str
        The title to display in the middle of the line.
    """
    print("-" * 32 + s + "-" * 32)


def is_mutable(obj: object) -> bool:
    """
    Determines if a built-in container object is mutable.

    Parameters
    ----------
    obj : object
        The object to check.

    Returns
    -------
    bool
        True if the object is mutable, False otherwise.
    """
    dict_mutable = {
        'str': False,
        'tuple': False,
        'list': True,
        'set': True,
        'frozenset': False,
        'dict': True,
    }
    return dict_mutable.get(type(obj).__name__, False)


def printStructInfos(container: object) -> None:
    """
    Prints structural information about a container object.

    Parameters
    ----------
    container : object
        The container to analyze.
    
    Prints
    ------
    Assignable: True if __setitem__ is present (supports item assignment)
    Subscriptable or Ordered: True if __getitem__ is present (supports indexing/iteration)
    Mutable: True if the object type is considered mutable
    Hashable: True if the object can be used as a dict key or set element
    Copiable: True if the object has a copy() method
    """
    assignable = '__setitem__' in dir(container)
    subscriptable = '__getitem__' in dir(container)
    mutable = is_mutable(container)
    hashable = not mutable and hasattr(container, '__hash__') and container.__hash__ is not None
    copiable = 'copy' in dir(container)

    print(f"Assignable                   : {assignable}")
    print(f"Subscriptable or Ordered      : {subscriptable}")
    print(f"Mutable                       : {mutable}")
    print(f"Hashable                      : {hashable}")
    print(f"Copiable                      : {copiable}")


# ---------------- Example Usage ---------------- #
printLine("# Example of a string")
my_string = "hello"
printStructInfos(my_string)
# Output: False, True, True, False, True, False

printLine("# Example of a tuple")
my_tuple = (1, 2, 3)
printStructInfos(my_tuple)
# Output: False, True, True, False, True, False

printLine("# Example of a list")
my_list = [1, 2, 3]
printStructInfos(my_list)
# Output: True, True, True, True, False, True

printLine("# Example of a set")
my_set = {1, 2, 3}
printStructInfos(my_set)
# Output: False, False, False, True, False, True

printLine("# Example of a frozenset")
my_frznset = frozenset([1, 2, 3])
printStructInfos(my_frznset)
# Output: False, False, False, False, True, True

printLine("# Example of a dictionary")
my_dict = {'a': 1, 'b': 2, 'c': 3}
printStructInfos(my_dict)
# Output: True, True, True, True, False, True