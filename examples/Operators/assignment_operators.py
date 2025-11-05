# Example of assignment operators in Python

# Definition of two variables
x = 5    # Binary: 0101
y = 3    # Binary: 0011

# Addition assignment
x += y # <==> x = x + y 
print(f"After addition assignment: x = {x}")  # Displays: After addition assignment: x = 8

# Subtraction assignment
x -= y # <==> x = x - y 
print(f"After subtraction assignment: x = {x}")  # Displays: After subtraction assignment: x = 5

# Multiplication assignment
x *= y # <==> x = x * y 
print(f"After multiplication assignment: x = {x}")  # Displays: After multiplication assignment: x = 15

# Division assignment
x /= y # <==> x = x / y 
print(f"After division assignment: x = {x}")  # Displays: After division assignment: x = 5.0

# Modulus assignment
x %= y # <==> x = x % y 
print(f"After modulus assignment: x = {x}")  # Displays: After modulus assignment: x = 2.0

# Exponentiation assignment
x **= y # <==> x = x ** y 
print(f"After exponentiation assignment: x = {x}")  # Displays: After exponentiation assignment: x = 8.0

# Floor division assignment
x //= y # <==> x = x // y 
print(f"After floor division assignment: x = {x}")  # Displays: After floor division assignment: x = 2.0

# Back to the int type
x = int(x) # x = 2 now, in binary: 0010

# Bitwise AND assignment
x &= y
print(f"After bitwise AND assignment: x = {x}")  # Displays: After bitwise AND assignment: x = 2

# Bitwise OR assignment
x |= y
print(f"After bitwise OR assignment: x = {x}")  # Displays: After bitwise OR assignment: x = 3

# Bitwise XOR assignment
x ^= y
print(f"After bitwise XOR assignment: x = {x}")  # Displays: After bitwise XOR assignment: x = 0

# Bitwise left shift assignment
x <<= y
print(f"After bitwise left shift assignment: x = {x}")  # Displays: After bitwise left shift assignment: x = 0

# Bitwise right shift assignment
x >>= y
print(f"After bitwise right shift assignment: x = {x}")  # Displays: After bitwise right shift assignment: x = 0
