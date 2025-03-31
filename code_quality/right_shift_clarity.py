
# sum (de k commençant à 0 jusqu'à 7) 2^k * b_k = N

# Représentation binaire de N = 6 (en décimal) en 8 bits (1 octet = 1 byte) 
#     0000                  0110
#  2^7 2^6 2^5 2^4     2^3 2^2 2^1 2^0
# sum (de k commençant à 0 jusqu'à 7) 2^k * b_k = 6 
# 6 = 4+2 = (2^2) * (1)  + (2^1) * (1)

# 6 >> 2 (>> : décalage à droite)

#     0000                  0110
#     00 0000                  0110 (décalage à droite, je rajoute deux zéros au début)
#     00 0000                  01  (10 est à supprimer)
#     00 0000                  01
#     0000                  0001 (ce qui représente 1 en décimal)


# Représentation binaire de N = 23 (en décimal) en 8 bits (1 octet = 1 byte) 
#     0001                  0111
#  2^7 2^6 2^5 2^4     2^3 2^2 2^1 2^0
# 23 = 16+4+2+1 = (2^4) * (1) + (2^2) * (1) + (2^1) * (1) + (2^0) * (1)

# 23 >> 2 (>> : décalage à droite)

#     0001                  0111
#     00 0001                  0111 (décalage à droite, je rajoute deux zéros au début)
#     00 0001                  01  (11 est à supprimer)
#     00 0001                  01
#     0000                  0101 (ce qui représente 5 en décimal)


# Example of code where clarity is missing

def right_shift_binary(num : int, bits: int) -> int:
    """
    Perform a RIGHT (>>) shift operation on a binary representation of a number.
    
    :param num: The number to be shifted.
    :param bits: The number of bits to shift.
    :return: The result of the right shift operation.
    """
    return num >> bits


def main() -> None:
    """ main entry """
    result = right_shift_binary(25, 3)
    print(result)

if __name__ == "__main__":
    main()