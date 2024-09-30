def printLine():
    """
    Prints a line of dashes as a separator.
    """
    print("--------------------------------------------------------")

END = 10
a, _, *_ = range(END)
print(f" -------- Example 1: a, _, *_ = range({END}) -------- \n")
printLine()
print(f"range({END}) have elements: ", *range(END))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (END-1)
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

a, _, b, *_ = range(END)
print(f" -------- Example 2: a, _, b, *_ = range({END}) -------- \n")
printLine()
print(f"range({END}) have elements: ", *range(END))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (END-1)
printLine()
print("b is : ", b)     # Will take the third element of range object : element @ position 3 = 
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

a, _, b, c, *_ = range(END)
print(f" -------- Example 3: a, _, b, c, *_ = range({END}) -------- \n")
printLine()
print(f"range({END}) have elements: ", *range(END))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (END-1)
printLine()
print("b is : ", b)     # Will take the third element of range object : element @ position 3
printLine()
print("c is : ", c)     # Will take the fourth element of range object : element @ position 4
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

# element @ position _ is ignored !!
# print(a, _, b, *_)