#!/usr/bin/env python3

def decimal_to_binary(num: int, bits: int = 8) -> str:
    """
    Convert a decimal number to its binary representation with specified number of bits.
    
    :param num: The decimal number to convert
    :param bits: Number of bits for representation (default 8)
    :return: Binary representation as a string with spaces every 4 bits
    """
    binary = format(num, f'0{bits}b')
    # Insert space every 4 bits for readability
    return ' '.join(binary[i:i+4] for i in range(0, len(binary), 4))

def decimal_to_octal(num: int) -> str:
    """
    Convert a decimal number to its octal representation.
    
    :param num: The decimal number to convert
    :return: Octal representation as a string
    """
    return format(num, 'o')

def decimal_to_hexadecimal(num: int) -> str:
    """
    Convert a decimal number to its hexadecimal representation.
    
    :param num: The decimal number to convert
    :return: Hexadecimal representation as a string
    """
    return format(num, 'x')

def right_shift_with_explanation(num: int, shift: int, bits: int = 8) -> tuple:
    """
    Perform a right shift operation with detailed explanation of the process.
    
    :param num: The number to shift
    :param shift: Number of positions to shift right
    :param bits: Number of bits for representation (default 8)
    :return: Tuple of (result, original_binary, shifted_binary)
    """
    original_binary = decimal_to_binary(num, bits)
    result = num >> shift
    shifted_binary = decimal_to_binary(result, bits)
    
    return result, original_binary, shifted_binary

def left_shift_with_explanation(num: int, shift: int, bits: int = 8) -> tuple:
    """
    Perform a left shift operation with detailed explanation of the process.
    
    :param num: The number to shift
    :param shift: Number of positions to shift left
    :param bits: Number of bits for representation (default 8)
    :return: Tuple of (result, original_binary, shifted_binary)
    """
    original_binary = decimal_to_binary(num, bits)
    result = num << shift
    shifted_binary = decimal_to_binary(result, bits)
    
    return result, original_binary, shifted_binary

def power_of_two_decomposition(num: int) -> list:
    """
    Decompose a number into sum of powers of 2.
    
    :param num: The number to decompose
    :return: List of powers of 2 that sum to the number
    """
    powers = []
    i = 0
    while num:
        if num & 1:
            powers.append(2 ** i)
        num >>= 1
        i += 1
    return powers

def print_number_info(num: int) -> None:
    """
    Print comprehensive information about a number including all its representations.
    
    :param num: The number to analyze
    """
    print(f"\nNumber Analysis for {num}:")
    print("-" * 50)
    print(f"Decimal: {num}")
    print(f"Binary:  {decimal_to_binary(num)}")
    print(f"Octal:   {decimal_to_octal(num)}")
    print(f"Hex:     0x{decimal_to_hexadecimal(num)}")
    
    # Power of 2 decomposition
    powers = power_of_two_decomposition(num)
    decomposition = " + ".join([str(p) for p in powers])
    print(f"Powers of 2 decomposition: {num} = {decomposition}")

def demonstrate_shift_operations(num: int, shift: int) -> None:
    """
    Demonstrate both left and right shift operations on a number.
    
    :param num: The number to perform shifts on
    :param shift: Number of positions to shift
    """
    print(f"\nShift Operations on {num}:")
    print("-" * 50)
    
    # Right shift
    right_result, right_orig, right_shifted = right_shift_with_explanation(num, shift)
    print(f"Right shift >> {shift}:")
    print(f"Original:  {right_orig}")
    print(f"Shifted:   {right_shifted}")
    print(f"Result:    {right_result}")
    
    # Left shift
    left_result, left_orig, left_shifted = left_shift_with_explanation(num, shift)
    print(f"\nLeft shift << {shift}:")
    print(f"Original:  {left_orig}")
    print(f"Shifted:   {left_shifted}")
    print(f"Result:    {left_result}")

def main() -> None:
    """Main function to demonstrate all operations."""
    # Example numbers from your cases
    test_numbers = [6, 23, 25]
    
    # Demonstrate all representations and operations for each number
    for num in test_numbers:
        print_number_info(num)
        demonstrate_shift_operations(num, 2)  # Demonstrate with shift of 2
    
if __name__ == "__main__":
    main()