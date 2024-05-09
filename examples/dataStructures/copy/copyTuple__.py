"""
Tuple objects are: 
    subscriptable, but not assignable 
    and no methods are allowing to modify them
    hence they are immutable (not modifiable)
"""

import copy # for deepcopy function

# Creating original list object
l = [2,3]
original_tuple = (1, l, 4)

# Object assigning_copy points to the same memory address of original_tuple
# Therefore: each modification impacting original_tuple will impact assigning_copy and vice versa
assigning_copy = original_tuple 
# CLEAR

# Objects operator_copy and shallow_copy are superficial copies of original_tuple
# Therefore:    each modification done to the TOP LEVEL of original_tuple objects will *NOT* impact 
#               operator_copy and shallow_copy and vice versa
# Whereas:      each modification done to the NESTED LEVELS of original_tuple objects will impact 
#               operator_copy and shallow_copy and vice versa
operator_copy = original_tuple[:] # a whole copy of original_tuple
# shallow_copy = original_tuple.copy() # a whole copy of original_tuple
# CLEAR

# Object deep_copy is a deep copy of original_tuple, deep_copy is totally independant of original_tuple
# Therefore: each modification done to original_tuple will *NOT* impact deep_copy and vice versa
deep_copy = copy.deepcopy(original_tuple) # a whole copy of original_tuple
# CLEAR

def test_tuple_copy():
    print("id(original_tuple) == id(assigning_copy)", id(original_tuple) == id(assigning_copy))
    print("id(original_tuple) == id(operator_copy)", id(original_tuple) == id(operator_copy))
    # print("id(original_tuple) == id(shallow_copy)", id(original_tuple) == id(shallow_copy))
    print("id(original_tuple) == id(deep_copy)", id(original_tuple) == id(deep_copy))


def test_nested_tuple_copy():
    print("id(original_tuple[1]) == id(assigning_copy[1])", id(original_tuple[1]) == id(assigning_copy[1]))
    print("id(original_tuple[1]) == id(operator_copy[1])", id(original_tuple[1]) == id(operator_copy[1]))
    # print("id(original_tuple[1]) == id(shallow_copy[1])", id(original_tuple[1]) == id(shallow_copy[1]))
    print("id(original_tuple[1]) == id(deep_copy[1])", id(original_tuple[1]) == id(deep_copy[1]))


def test_references_tuple():
    print("ID original_tuple: ", id(original_tuple))
    print("ID assigning_copy: ", id(assigning_copy))
    print("ID operator_copy: ", id(operator_copy))
    # print("ID shallow_copy: ", id(shallow_copy))
    print("ID deep_copy: ", id(deep_copy))

def test_nested_references_tuple():
    print("ID original_tuple[1]: ", id(original_tuple[1]))
    print("ID assigning_copy[1]: ", id(assigning_copy[1]))
    print("ID operator_copy[1]: ", id(operator_copy[1]))
    # print("ID shallow_copy[1]: ", id(shallow_copy[1]))
    print("ID deep_copy[1]: ", id(deep_copy[1]))

def printLine():
    print("------------------------------------------------------")

def tuple_tests():
    print('\n')
    print("---------------------------Launching tuple Tests---------------------------")
    test_tuple_copy()
    printLine()
    test_nested_tuple_copy()
    printLine()
    test_references_tuple()
    printLine()
    test_nested_references_tuple()
    print("---------------------------End tuple Tests---------------------------")
    print('\n')

tuple_tests()

print("---------------------------------------------------------------------------------------------------")
print("# Original tuple | # Assigning Copy     | # Operator Copy | # Shallow Copy |  # Deep Copy |")
print("---------------------------------------------------------------------------------------------------")
print("# Before modification original_tuple[1][0] = 69")
print(original_tuple, " | ", assigning_copy, " | ", operator_copy, " | NOT CONCERNED | ", deep_copy, " | ")
original_tuple[1][0] = 69
print("---------------------------------------------------------------------------------------------------")
print("# After modification original_tuple[1][0] = 69")
print(original_tuple, " | ", assigning_copy, " | ", operator_copy, " | NOT CONCERNED | ", deep_copy, " | ")
print("---------------------------------------------------------------------------------------------------")

'''
# OUTPUT:

---------------------------------------------------------------------------------------------------
# Original tuple | # Assigning Copy     | # Operator Copy | # Shallow Copy |  # Deep Copy |
---------------------------------------------------------------------------------------------------
# Before modification original_tuple[1][0] = 69
(1, [2, 3], 4)  |  (1, [2, 3], 4)  |  (1, [2, 3], 4)  | NOT CONCERNED |  (1, [2, 3], 4)  | 
---------------------------------------------------------------------------------------------------
# After modification original_tuple[1][0] = 69
(1, [69, 3], 4)  |  (1, [69, 3], 4)  |  (1, [69, 3], 4)  | NOT CONCERNED |  (1, [2, 3], 4)  | 
---------------------------------------------------------------------------------------------------
'''


'''
En résumé, les copies superficielles ne dupliquent pas les objets imbriqués, 
de sorte que les modifications apportées aux objets imbriqués seront reflétées 
dans toutes les copies, mais les modifications apportées aux objets de plus haut niveau 
(comme les éléments du tuple) ne le seront pas.

Ici on modifie la liste tout simplement !
'''