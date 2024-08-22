import numpy as np

# Create a 3x4x5 tensor
tensor = np.arange(3 * 4 * 5).reshape(3, 4, 5)

# Original tensor
print("\nOriginal Tensor tensor :\n", tensor)

# Slicing along all dimensions (equivalent to: tensor)
print("\nOriginal Tensor tensor[:] :\n", tensor[:])

# First Matrix
print("\nSlice (first matrix) tensor[0] :\n", tensor[0])

# Second Matrix
print("\nSlice (second matrix) tensor[1] :\n", tensor[1])

# Third Matrix
print("\nSlice (third matrix) tensor[2] :\n", tensor[2])

# Slicing a specific element
print("\nSpecific element (second matrix, third row, fourth column) tensor[1, 2, 3] :\n", tensor[1, 2, 3])

# Slicing using negative indices
print("\nSlice using negative indices (last matrix) tensor[-1] :\n", tensor[-1])

# Slicing with reverse order along all dimensions
print("\nReverse slicing along all dimensions tensor[::-1, ::-1, ::-1] :\n", tensor[::-1, ::-1, ::-1])

# Reverse slicing along the second dimension
print("\nReverse slicing along the second dimension (rows in reverse order) tensor[:, ::-1, :] :\n", tensor[:, ::-1, :])

# Slicing along the first dimension (equivalent to tensor[0])
print("\nSlice along the first dimension (first matrix) tensor[0, :, :] :\n", tensor[0, :, :])

# Slicing along the second dimension (first row of each matrix)
print("\nSlice along the second dimension (first row of each matrix) tensor[:, 0, :] :\n", tensor[:, 0, :])

# Slicing along the third dimension (first column of each matrix)
print("\nSlice along the third dimension (first column of each matrix) tensor[:, :, 0] :\n", tensor[:, :, 0])

# Slicing a sub-tensor (2x3x4 sub-tensor)
print("\nSub-tensor (first 2 matrices, first 3 rows, first 4 columns) tensor[:2, :3, :4] :\n", tensor[:2, :3, :4])

# Slicing with a step (every second row and column in the first matrix)
print("\nStep slicing (every second row and column in the first matrix) tensor[0, ::2, ::2] :\n", tensor[0, ::2, ::2])

# Slicing a sub-tensor with step (2x3x5, skipping every other element in rows and columns)
print("\nSub-tensor with step tensor[::2, ::1, ::2] :\n", tensor[::2, ::1, ::2])

# Slicing every second matrix, every second row, and every third column
print("\nEvery second matrix, every second row, and every third column tensor[::2, ::2, ::3] :\n", tensor[::2, ::2, ::3])

# Slicing with specific start, end, and step values for each dimension
print("\nSub-tensor with start, end, and step tensor[1:3, 1:4:2, 0:5:2] :\n", tensor[1:3, 1:4:2, 0:5:2])

# Extracting every element in the second and third rows and columns from the second matrix
print("\nElements from the second and third rows and columns of the second matrix tensor[1, 1:3, 1:3] :\n", tensor[1, 1:3, 1:3])

# Slicing specific rows and columns from the first and last matrices
print("\nSpecific rows and columns from the first and last matrices tensor[[0, -1], :, [1, 3]] :\n", tensor[[0, -1], :, [1, 3]])
