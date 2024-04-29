def printLine():
    """
    Prints a line of dashes as a separator.
    """
    print("----------------------------")

# Example using the range() function to generate a sequence of numbers
for _ in range(4):
    print("Hello")
printLine()

# Example using the range() function with specified start and step parameters
for _ in range(1, 6, 2):
    print("Ignored")
printLine()

# Example using the range() function with only the stop parameter specified
for _ in range(5):
    print("Skipped")
printLine()

# Example using the range() function to generate an empty sequence
for _ in range(0):
    print("No output")
printLine()
