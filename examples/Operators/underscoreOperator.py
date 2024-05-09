def printLine():
    """
    Prints a line of dashes as a separator.
    """
    print("--------------------------------------------------------")

end = 10
a, _, *_ = range(end)
print(f" -------- Example 1: a, _, *_ = range({end}) -------- \n")
printLine()
print(f"range({end}) have elements: ", *range(end))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (end-1)
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

a, _, b, *_ = range(end)
print(f" -------- Example 2: a, _, b, *_ = range({end}) -------- \n")
printLine()
print(f"range({end}) have elements: ", *range(end))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (end-1)
printLine()
print("b is : ", b)     # Will take the third element of range object : element @ position 3 = 
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

a, _, b, c, *_ = range(end)
print(f" -------- Example 3: a, _, b, c, *_ = range({end}) -------- \n")
printLine()
print(f"range({end}) have elements: ", *range(end))
printLine()
print("a is : ", a)     # Will take the first element of range object : element @ position 1 = start
printLine()
print("_ is : ", _)     # Will create a list of elements starting @ start = ((#number of variables) + 1) to (end-1)
printLine()
print("b is : ", b)     # Will take the third element of range object : element @ position 3
printLine()
print("c is : ", c)     # Will take the third element of range object : element @ position 4
printLine()
print("*_ is : ", *_)   # Depacking the list with the * operator
printLine()
print('\n')

# element @ position _ is ignored !!
# print(a, _, b, *_)