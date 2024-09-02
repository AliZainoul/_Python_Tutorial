import numpy as np

def basic_broadcasting_example():
    """
    Demonstrates basic broadcasting with 1D and 2D arrays.
    
    Broadcasting rules:
    1. Arrays are compatible when they have the same shape or one of them is 1 along any dimension.
    2. Broadcasting replicates the smaller array along the mismatched dimension.
    
    Example: Broadcasting a 1D array (3,) to a 2D array (2,3).
    """
    arr_1d = np.array([1, 2, 3])  # 1D array of shape (3,)
    arr_2d = np.array([[4, 5, 6], [7, 8, 9]])  # 2D array of shape (2, 3)
    
    # Broadcasting arr_1d to match arr_2d's shape and adding them
    result = arr_2d + arr_1d
    
    print("1D (3,) + 2D (2,3):\n", result)

def broadcasting_with_scalars():
    """
    Demonstrates broadcasting with scalars.
    
    Scalars can be broadcasted to any shape of array. The scalar value 
    is applied to every element in the array.
    
    Example: Adding a scalar to a 2D array.
    """
    arr_2d = np.array([[10, 20, 30], [40, 50, 60]])  # 2D array of shape (2, 3)
    scalar = 5  # Scalar value
    
    # Broadcasting scalar to each element of arr_2d
    result = arr_2d + scalar
    
    print("2D (2,3) + scalar (5):\n", result)

def broadcasting_with_2d_and_3d():
    """
    Demonstrates broadcasting with 2D and 3D arrays.
    
    Example: Broadcasting a 2D array (4,3) to a 3D array (2,4,3).
    The 2D array is broadcasted across the first dimension.
    """
    arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])  # Shape (4, 3)
    arr_3d = np.ones((2, 4, 3))  # Shape (2, 4, 3)
    
    # Broadcasting arr_2d across the first dimension of arr_3d
    result = arr_3d * arr_2d
    
    print("3D (2,4,3) * 2D (4,3):\n", result)

def broadcasting_with_higher_dimensions():
    """
    Demonstrates broadcasting with higher dimensions (7D and 8D arrays).
    
    Example: Broadcasting a 7D array to match an 8D array.
    The smaller array is broadcasted across dimensions with size 1.
    """
    arr_7d = np.ones((1, 2, 1, 3, 1, 4, 1))  # Shape (1, 2, 1, 3, 1, 4, 1)
    arr_8d = np.ones((5, 1, 2, 1, 3, 1, 1, 6))  # Shape (5, 1, 2, 1, 3, 1, 1, 6)
    
    # Broadcasting arr_7d to match arr_8d
    result = arr_7d + arr_8d
    
    print("7D (1,2,1,3,1,4,1) + 8D (5,1,2,1,3,1,1,6):\n", result.shape)

def broadcasting_with_incompatible_shapes():
    """
    Demonstrates broadcasting with incompatible shapes that raise an error.
    
    Example: Attempting to broadcast arrays with incompatible dimensions.
    """
    arr_2d = np.ones((2, 3))  # Shape (2, 3)
    arr_3d = np.ones((3, 2, 4))  # Shape (3, 2, 4)
    
    try:
        # Attempt to broadcast incompatible shapes
        result = arr_3d + arr_2d
    except ValueError as e:
        print("Error broadcasting incompatible shapes:\n", e)

def complex_broadcasting_operations():
    """
    Demonstrates complex broadcasting operations including chaining broadcasts.
    
    Example: Performing multiple operations that involve broadcasting.
    """
    arr_3d = np.random.rand(4, 1, 3)  # Shape (4, 1, 3)
    arr_4d = np.random.rand(2, 4, 1, 3)  # Shape (2, 4, 1, 3)
    
    # Broadcasting arr_3d to match arr_4d's shape and multiplying
    result = arr_4d * arr_3d
    
    print("Chained broadcasting (3D to 4D):\n", result.shape)
    
    arr_5d = np.random.rand(2, 1, 4, 3, 1)  # Shape (2, 1, 4, 3, 1)
    
    # Further broadcasting arr_4d and arr_5d and adding them
    result_final = result + arr_5d
    
    print("Chained broadcasting (4D to 5D):\n", result_final.shape)

def broadcasting_with_transpose():
    """
    Demonstrates the use of transpose in conjunction with broadcasting.
    
    Example: Transposing an array before performing a broadcasting operation.
    """
    arr_2d = np.random.rand(3, 4)  # Shape (3, 4)
    arr_1d = np.random.rand(3)  # Shape (3,3)
    
    # Transposing arr_2d to shape (4, 3) and broadcasting with arr_1d
    result = np.transpose(arr_2d) * (arr_1d)
    
    print("Transposing and broadcasting (2D (3,4) transposed with 1D (4,)):\n", result)

def final_project_broadcasting():
    """
    Final project: Combining multiple broadcasting techniques in a practical example.
    
    Task:
    1. Create a 3D tensor representing image data (batch_size, height, width).
    2. Create a 4D filter tensor representing convolutional filters (num_filters, filter_height, filter_width, channels).
    3. Broadcast the 3D tensor to match the filter tensor and perform an element-wise multiplication.
    """
    batch_size, height, width = 10, 5, 5  # Example image dimensions
    num_filters, filter_height, filter_width, channels = 6, 5, 5, 3  # Example filter dimensions
    
    # 3D tensor for image data (batch_size, height, width)
    images = np.random.rand(batch_size, height, width, 3)
    
    # 4D tensor for filters (num_filters, filter_height, filter_width, channels)
    filters = np.random.rand(num_filters, filter_height, filter_width, channels)
    
    # Broadcasting images to match filters (this simulates the initial stage of convolution)
    result = images[:, None, :, :, :] * filters[None, :, :, :, :]
    
    print("Final project - Broadcasting images (4D) with filters (5D):\n", result.shape)

if __name__ == "__main__":
    # Step-by-step examples
    basic_broadcasting_example()         # Easy: 1D with 2D
    broadcasting_with_scalars()          # Scalar broadcasting
    broadcasting_with_2d_and_3d()        # Medium: 2D with 3D
    broadcasting_with_higher_dimensions()# Complex: 7D with 8D
    broadcasting_with_incompatible_shapes() # Error case: incompatible shapes
    complex_broadcasting_operations()    # Complex chaining operations
    broadcasting_with_transpose()        # Using transpose with broadcasting
    final_project_broadcasting()         # Final project combining multiple concepts
