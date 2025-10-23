# Example of bitwise operators in Python

# Definition of two variables
x = 5    # Binary: 0101
y = 3    # Binary: 0011

# Bitwise AND operator
result_and = x & y
print(f"Bitwise AND: {x} & {y} = {result_and}")

# Bitwise OR operator
result_or = x | y
print(f"Bitwise OR: {x} | {y} = {result_or}")

# Bitwise XOR operator
result_xor = x ^ y
print(f"Bitwise XOR: {x} ^ {y} = {result_xor}")

# Bitwise NOT operator
result_not_x = ~x
result_not_y = ~y
print(f"Bitwise NOT of {x}: {result_not_x}")
print(f"Bitwise NOT of {y}: {result_not_y}")

# Bitwise Left Shift operator
result_left_shift = x << 1
print(f"Bitwise Left Shift: {x} << 1 = {result_left_shift}")

# Bitwise Right Shift operator
result_right_shift = x >> 1
print(f"Bitwise Right Shift: {x} >> 1 = {result_right_shift}")
