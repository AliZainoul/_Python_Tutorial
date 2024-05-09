# Example of various operators in Python

# Arithmetic Operators
x = 10
y = 3
print(f"x + y = {x + y}")  # Addition
print(f"x - y = {x - y}")  # Subtraction
print(f"x * y = {x * y}")  # Multiplication
print(f"x / y = {x / y}")  # Division
print(f"x // y = {x // y}")  # Entire Division (Floor Division)
print(f"x % y = {x % y}")  # Modulus
print(f"x ** y = {x ** y}")  # Exponentiation

# Assignment Operators
a = 5
b = 2
a += b  # Addition Assignment
print(f"After a += b: a = {a}")
a -= b  # Subtraction Assignment
print(f"After a -= b: a = {a}")
a *= b  # Multiplication Assignment
print(f"After a *= b: a = {a}")
a /= b  # Division Assignment
print(f"After a /= b: a = {a}")

# Comparison Operators
print(f"x == y: {x == y}")  # Equal to
print(f"x != y: {x != y}")  # Not equal to
print(f"x > y: {x > y}")  # Greater than
print(f"x < y: {x < y}")  # Less than
print(f"x >= y: {x >= y}")  # Greater than or equal to
print(f"x <= y: {x <= y}")  # Less than or equal to

# Logical Operators
p = True
q = False
print(f"p and q: {p and q}")  # Logical AND
print(f"p or q: {p or q}")  # Logical OR
print(f"not p: {not p}")  # Logical NOT

# Ternary Operator
max_value = x if x > y else y
print(f"Max value between x and y: {max_value}")

# Membership Operators
list_a = [1, 2, 3, 4, 5]
print(f"2 in list_a: {2 in list_a}")  # True if 2 is in list_a
print(f"6 not in list_a: {6 not in list_a}")  # True if 6 is not in list_a

# Identity Operators
z = 10
print(f"x is z: {x is z}")  # True if x and z reference the same object
print(f"x is not z: {x is not z}")  # True if x and z reference different objects
