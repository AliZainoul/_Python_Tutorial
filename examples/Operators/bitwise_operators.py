# Example of bitwise operators in Python

"""
    1 BYTE (Octet) := 8 bits = [xxxx xxxx]
    32 bits | 64 bits 
    [0000 0000 0000 0000 0000 0000 0000 0101] sur 32 bits
    [0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0000 0101] sur 64 bits
"""

# Definition of two variables
x = 5    # Binary: 0101
y = 3    # Binary: 0011

# Bitwise AND operator
result_and = x & y # Binary : 0001 --> Decimal : 1
print(f"Bitwise AND: {x} & {y} = {result_and}") 

# Bitwise OR operator
result_or = x | y # Binary : 0111 --> Decimal : 7
print(f"Bitwise OR: {x} | {y} = {result_or}")

# Bitwise XOR operator
result_xor = x ^ y # Binary : 0110 --> Decimal : 6
print(f"Bitwise XOR: {x} ^ {y} = {result_xor}")

# Bitwise NOT operator
result_not_x = ~x # Decimal : -(x+1)
result_not_y = ~y # Decimal : -(y+1)
print(f"Bitwise NOT of {x}: {result_not_x}")
print(f"Bitwise NOT of {y}: {result_not_y}")

# Bitwise Left Shift operator
result_left_shift = x << 1 # Binary: [0000 0000 0000 0000 0000 0000 0000 0101] in 32 bits arch. ; [0000 0000 0000 0000 0000 0000 0000 1010] -> Decimal : 10
print(f"Bitwise Left Shift: {x} << 1 = {result_left_shift}")

# Bitwise Right Shift operator
result_right_shift = x >> 1 # Binary: [0000 0000 0000 0000 0000 0000 0000 0101] in 32 bits arch. ; [0000 0000 0000 0000 0000 0000 0000 0010] -> Decimal : 2
print(f"Bitwise Right Shift: {x} >> 1 = {result_right_shift}")
