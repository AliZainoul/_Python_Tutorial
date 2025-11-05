# File / script / module : math_utils.py
def add(num_1: int, num_2: int) -> int:
    """
    Add two numbers.

    Parameters:
    num_1 (int): The first number.
    num_2 (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return num_1 + num_2

def main() -> None:
    # Example usage
    result : int = add(5, 7)
    print(f"The sum of 5 and 7 is: {result}")

if __name__ == "__main__":
    main()

# https://fr.wikipedia.org/wiki/Mach_(informatique)
# https://fr.wikipedia.org/wiki/Berkeley_Software_Distribution
# https://fr.wikipedia.org/wiki/Unix