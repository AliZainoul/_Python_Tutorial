import copy # for deepcopy function

# Creating original list object
original_list = [1, [2, 3], 4]

# Object assigning_copy points to the same memory address of original_list
# Therefore: each modification impacting original_list will impact assigning_copy and vice versa
assigning_copy = original_list 
# CLEAR

# Objects operator_copy and shallow_copy are superficial copies of original_list
# Therefore:    each modification done to the TOP LEVEL of original_list objects will *NOT* impact 
#               operator_copy and shallow_copy and vice versa
# Whereas:      each modification done to the NESTED LEVELS of original_list objects will impact 
#               operator_copy and shallow_copy and vice versa
operator_copy = original_list[:] # a whole copy of original_list
shallow_copy = original_list.copy() # a whole copy of original_list
# CLEAR

# Object deep_copy is a deep copy of original_list, deep_copy is totally independant of original_list
# Therefore: each modification done to original_list will *NOT* impact deep_copy and vice versa
deep_copy = copy.deepcopy(original_list) # a whole copy of original_list
# CLEAR

def test_list_copy():
    print("id(original_list) == id(assigning_copy)", id(original_list) == id(assigning_copy))
    print("id(original_list) == id(operator_copy)", id(original_list) == id(operator_copy))
    print("id(original_list) == id(shallow_copy)", id(original_list) == id(shallow_copy))
    print("id(original_list) == id(deep_copy)", id(original_list) == id(deep_copy))


def test_nested_list_copy():
    print("id(original_list[1]) == id(assigning_copy[1])", id(original_list[1]) == id(assigning_copy[1]))
    print("id(original_list[1]) == id(operator_copy[1])", id(original_list[1]) == id(operator_copy[1]))
    print("id(original_list[1]) == id(shallow_copy[1])", id(original_list[1]) == id(shallow_copy[1]))
    print("id(original_list[1]) == id(deep_copy[1])", id(original_list[1]) == id(deep_copy[1]))


def test_references_list():
    print("ID original_list: ", id(original_list))
    print("ID assigning_copy: ", id(assigning_copy))
    print("ID operator_copy: ", id(operator_copy))
    print("ID shallow_copy: ", id(shallow_copy))
    print("ID deep_copy: ", id(deep_copy))

def test_nested_references_list():
    print("ID original_list[1]: ", id(original_list[1]))
    print("ID assigning_copy[1]: ", id(assigning_copy[1]))
    print("ID operator_copy[1]: ", id(operator_copy[1]))
    print("ID shallow_copy[1]: ", id(shallow_copy[1]))
    print("ID deep_copy[1]: ", id(deep_copy[1]))

def printLine():
    print("------------------------------------------------------")

def list_tests():
    print('\n')
    print("---------------------------Launching list Tests---------------------------")
    test_list_copy()
    printLine()
    test_nested_list_copy()
    printLine()
    test_references_list()
    printLine()
    test_nested_references_list()
    print("---------------------------End list Tests---------------------------")
    print('\n')

list_tests()

print("---------------------------------------------------------------------------------------------------")
print("# Original list | # Assigning Copy     | # Operator Copy | # Shallow Copy |  # Deep Copy |")
print("---------------------------------------------------------------------------------------------------")
print("# Before modification original_list[0] = 5")
print(original_list, " | ", assigning_copy, " | ", operator_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
original_list[0] = 5
print("---------------------------------------------------------------------------------------------------")
print("# After modification original_list[0] = 5")
print(original_list, " | ", assigning_copy, " | ", operator_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
print("---------------------------------------------------------------------------------------------------")
print("# Before modification original_list[1][0] = 69")
print(original_list, " | ", assigning_copy, " | ", operator_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
original_list[1][0] = 69
print("---------------------------------------------------------------------------------------------------")
print("# After modification original_list[1][0] = 69")
print(original_list, " | ", assigning_copy, " | ", operator_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
print("---------------------------------------------------------------------------------------------------")


'''
# OUTPUT:

---------------------------------------------------------------------------------------------------
# Original list | # Assigning Copy     | # Operator Copy | # Shallow Copy |  # Deep Copy |
---------------------------------------------------------------------------------------------------
# Before modification original_list[0] = 5
[1, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  | 
---------------------------------------------------------------------------------------------------
# After modification original_list[0] = 5
[5, [2, 3], 4]  |  [5, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  | 
---------------------------------------------------------------------------------------------------
# Before modification original_list[1][0] = 69
[5, [2, 3], 4]  |  [5, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  |  [1, [2, 3], 4]  | 
---------------------------------------------------------------------------------------------------
# After modification original_list[1][0] = 69
[5, [69, 3], 4]  |  [5, [69, 3], 4]  |  [1, [69, 3], 4]  |  [1, [69, 3], 4]  |  [1, [2, 3], 4]  | 
---------------------------------------------------------------------------------------------------
'''


'''
En résumé, les copies superficielles ne dupliquent pas les objets imbriqués, 
de sorte que les modifications apportées aux objets imbriqués seront reflétées 
dans toutes les copies, mais les modifications apportées aux objets de plus haut niveau 
(comme les éléments de la liste) ne le seront pas.
'''