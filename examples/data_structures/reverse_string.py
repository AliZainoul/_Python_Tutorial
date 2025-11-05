def reverse_string(s: str) -> str:
    """
    Reverses a string using the built-in `reversed()` function and `str.join()`.

    Parameters
    ----------
    s : str
        The input string to reverse.

    Returns
    -------
    str
        The reversed string.
    """
    return ''.join(reversed(s))


def reverse_string_with_slicing(s: str) -> str:
    """
    Reverses a string using Python slicing syntax.

    Parameters
    ----------
    s : str
        The input string to reverse.

    Returns
    -------
    str
        The reversed string.

    Detailed Explanation
    --------------------
    Python slicing syntax is:
        s[start:stop:step]

    - **start**: The index where the slice begins (inclusive).
    - **stop**:  The index where the slice ends (exclusive).
    - **step**:  The increment (positive or negative) between indices.

    Example: 
        s = "Hello"
        s[0]  -> 'H'
        s[1]  -> 'e'
        s[2]  -> 'l'
        s[3]  -> 'l'
        s[4]  -> 'o'

    When we write `s[::-1]`, it means:
        - start: omitted → Python assumes the end of the string.
        - stop:  omitted → Python assumes the beginning of the string (index 0).
        - step:  -1 → move one step backward each time.

    Thus, the slicing process goes like this:
        Step 1: Start from index -1 (last element: 'o')
        Step 2: Move backward one step at a time
        Step 3: Collect characters in reverse order
        Step 4: Stop before going past the start of the string

    Therefore:
        s[::-1] → "olleH"

    Equivalent expressions:
        s[::-1]
        s[len(s)-1::-1]
        s[-1::-1]
        s[stArt := 0: stOp: stEp := 1]
        # [ range(stArt := 0, stOp, stEp := 1) ]

    Example
    -------
    >>> reverse_string_with_slicing("Python")
    'nohtyP'
    """
    return s[::-1]  # or equivalently: s[len(s)-1::-1]


def reverse_string_iterative(s: str) -> str:
    """Reverses a string using a for-loop (iterative approach)."""
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str


def reverse_string_recursive(s: str) -> str:
    """Reverses a string using recursion."""
    if len(s) <= 1:
        return s
    return reverse_string_recursive(s[1:]) + s[0]


def reverse_string_using_stack(s: str) -> str:
    """Reverses a string using a stack (list)."""
    stack = list(s)
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    return reversed_str


# ---------------- Example Usage ---------------- #

def main() -> None:
    original_string = "Hello, World!"
    
    print("Original String:", original_string)
    print("Reversed (using reversed):", reverse_string(original_string))
    print("Reversed (using slicing):", reverse_string_with_slicing(original_string))
    print("Reversed (using iterative):", reverse_string_iterative(original_string))
    print("Reversed (using recursion):", reverse_string_recursive(original_string))
    print("Reversed (using stack):", reverse_string_using_stack(original_string))

if __name__ == "__main__":
    main()
