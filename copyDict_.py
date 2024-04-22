import copy

# Création d'un dictionnaire original
d1 = {'a': 1, 'b': 2, 'c': 3}

# Copies du dictionnaire original
d2 = d1
d3 = d1.copy()
d4 = copy.deepcopy(d1)

# Avant modification de d1
print("# Avant modification de d1")
for el in [d1, d2, d3, d4]:
    print(el)

# Modification de d1
d1['a'] = 10

# Après modification de d1
print("# Après modification de d1")
for el in [d1, d2, d3, d4]:
    print(el)

'''
# Affichage de tous les dictionnaires
print("Dictionnaire original:", d1)  # Output: Dictionnaire original: {'a': 10, 'b': 2, 'c': 3}
print("Copie superficielle (d2):", d2)  # Output: Copie superficielle (d2): {'a': 10, 'b': 2, 'c': 3}
print("Copie superficielle (d3):", d3)  # Output: Copie superficielle (d3): {'a': 1, 'b': 2, 'c': 3}
print("Copie en profondeur (d4):", d4)  # Output: Copie en profondeur (d4): {'a': 1, 'b': 2, 'c': 3}
'''
