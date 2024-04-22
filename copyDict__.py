import copy

# Creating original dict object
original_dict = {'a': 1, 'b': [2, 3], 'c': 4}

# Object assigning_copy points to the same memory address of original_dict
# Therefore: each modification impacting original_dict will impact assigning_copy and vice versa
assigning_copy = original_dict
# CLEAR

# Object shallow_copy is a superficial copy of original_dict
# Therefore:    each modification done to the TOP LEVEL of original_dict objects will *NOT* impact 
#               shallow_copy and vice versa
# Whereas:      each modification done to the NESTED LEVELS of original_dict objects will impact 
#               shallow_copy and vice versa
shallow_copy = original_dict.copy() # a whole copy of original_dict
# CLEAR

# Object deep_copy is a deep copy of original_dict, deep_copy is totally independant of original_dict
# Therefore: each modification done to original_dict will *NOT* impact deep_copy and vice versa
deep_copy = copy.deepcopy(original_dict) # a whole copy of original_dict
# CLEAR

def test_dict_copy():
    print("id(original_dict) == id(assigning_copy)", id(original_dict) == id(assigning_copy))
    print("id(original_dict) == id(shallow_copy)", id(original_dict) == id(shallow_copy))
    print("id(original_dict) == id(deep_copy)", id(original_dict) == id(deep_copy))


def test_nested_dict_copy():
    print("id(original_dict['b']) == id(assigning_copy['b'])", id(original_dict['b']) == id(assigning_copy['b']))
    print("id(original_dict['b']) == id(shallow_copy['b'])", id(original_dict['b']) == id(shallow_copy['b']))
    print("id(original_dict['b']) == id(deep_copy['b'])", id(original_dict['b']) == id(deep_copy['b']))


def test_references_dict():
    print("ID original_dict: ", id(original_dict))
    print("ID assigning_copy: ", id(assigning_copy))
    print("ID shallow_copy: ", id(shallow_copy))
    print("ID deep_copy: ", id(deep_copy))

def test_nested_references_dict():
    print("ID original_dict['b']: ", id(original_dict['b']))
    print("ID assigning_copy['b']: ", id(assigning_copy['b']))
    print("ID shallow_copy['b']: ", id(shallow_copy['b']))
    print("ID deep_copy['b']: ", id(deep_copy['b']))

def printLine():
    print("------------------------------------------------------")

def dict_tests():
    print('\n')
    print("---------------------------Launching Dict Tests---------------------------")
    test_dict_copy()
    printLine()
    test_nested_dict_copy()
    printLine()
    test_references_dict()
    printLine()
    test_nested_references_dict()
    print("---------------------------End Dict Tests---------------------------")
    print('\n')

dict_tests()


# Avant modification de original_dict
print("---------------------------------------------------------------------------------------------------")
print("# Original Dict | # Assigning Copy | # Shallow Copy | # Deep Copy |")
print("---------------------------------------------------------------------------------------------------")
print("# Avant modification original_dict['a'] = 5")
print(original_dict, " | ", assigning_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
original_dict['a'] = 5

# Après modification de original_dict
print("---------------------------------------------------------------------------------------------------")
print("# Après modification original_dict['a'] = 5")
print(original_dict, " | ", assigning_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
print("---------------------------------------------------------------------------------------------------")
print("# Avant modification original_dict['b'][0] = 69")
print(original_dict, " | ", assigning_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
original_dict['b'][0] = 69

# Après modification de original_dict
print("---------------------------------------------------------------------------------------------------")
print("# Après modification original_dict['b'][0] = 69")
print(original_dict, " | ", assigning_copy, " | ", shallow_copy, " | ", deep_copy, " | ")
print("---------------------------------------------------------------------------------------------------")
