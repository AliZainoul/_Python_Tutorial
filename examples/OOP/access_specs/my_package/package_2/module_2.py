from package_1.module_1 import MyClass

class B:
    def try_access_protected(self):
        obj = MyClass()
        print("Tentative d'accès à un attribut protégé :", obj._protected_attribute)
        print("Tentative d'appel à une méthode protégée :", obj._protected_method())


# ici l'on est dans le package__2, et l'on veut accéder à des membres de l'objet obj 
# qui est une instance de la classe MyClass du package__1. 

# comme la méthode access_attributes() de MyClass est publique, d'une part, et d'autre part c'est 
# que l'on accede indirectement à l'ensemble des attributs de l'objet obj, privés, protected et public
# et ce indirectement grâce à la méthode publique access_attributes(). 


# QUID du fait que l'on veuille accéder à des attributs d'une manière directe ? 

# Exemple : est-ce que d'ici l'on peut accéder à obj.public_attribute ? La réponse est oui, car
# public_attribute est un attribut public de MyClass, et donc accessible depuis n'importe où.

# Exemple : est-ce que d'ici l'on peut accéder à obj._protected_attribute ? La réponse est non, car
# _protected_attribute est un attribut protégé de MyClass, et donc accessible uniquement 
# depuis le package package__1 où se trouve notre classe MyClass. 


# Exemple : est-ce que d'ici l'on peut accéder à obj.__private_attribute ? La réponse est non, car
# __private_attribute est un attribut privé de MyClass, et donc accessible uniquement
# depuis la classe MyClass elle-même, et non pas depuis l'extérieur de la classe.