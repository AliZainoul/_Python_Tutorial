def printLine():
    """
    Prints a line of dashes as a separator.
    """
    print("----------------------------")

# Usage with the * operator
n = 5
for i in range(*[n]):
    print(i)
printLine()
# range(n)

# Usage with the * operator to unpack a list
start_stop = [1, 5]
for j in range(*start_stop):
    print(j)
printLine()
# range(start = 1, stop = 5)

# Usage with the * operator to unpack a tuple
params = (10, 20, 2)
for k in range(*params):
    print(k)
printLine()
# range(start = 10, stop = 20, step = 2)

# Usage with the _ operator to ignore a value
for _ in range(3):
    print("Hello")
printLine()