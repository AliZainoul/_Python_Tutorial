class MyClass:
    def __init__(self):
        self.__private_attr = 42

    def __private_method(self):
        print("This is a private method")

# Création d'une instance de la classe
obj = MyClass()

# Accès à l'attribut privé à l'extérieur de la classe
# print(obj.__private_attr)  # Cela lèvera une AttributeError

# Appel à la méthode privée à l'extérieur de la classe
# obj.__private_method()  # Cela lèvera également une AttributeError

# Accès à l'attribut privé en utilisant le name mangling
print(obj._MyClass__private_attr)  # Cela affichera 42

# Appel à la méthode privée en utilisant le name mangling
obj._MyClass__private_method()  # Cela affichera "This is a private method"
