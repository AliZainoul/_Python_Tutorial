import copy

# Création d'un dictionnaire original
original_dict = {'a': 1, 'b': [2, 3], 'c': 4}

# Assignation d'un dictionnaire pointant vers la même adresse mémoire
assigning_copy = original_dict

# Copies superficielles du dictionnaire original
shallow_copy = original_dict.copy()

# Copie en profondeur du dictionnaire original
deep_copy = copy.deepcopy(original_dict)

# Affichage des IDs des objets
print("ID original_dict: ", id(original_dict))
print("ID assigning_copy: ", id(assigning_copy))
print("ID shallow_copy: ", id(shallow_copy))
print("ID deep_copy: ", id(deep_copy))

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
