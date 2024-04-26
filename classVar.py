# BEGIN CLASS
class MyClass:
    class_variable = 999999
    
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def print_class_variable(cls):
        print("cls.class_variable: ", cls.class_variable)

    def print_instance_variable(self):
        print("object.instance_variable: ", self.instance_variable)

    def print_object_class_variable(self):
        print("object.class_variable: ", self.class_variable)
# END CLASS

# UTILITY FUNCTION
def printLine():
    print("--------------------------------")

printLine()
print("Before Instanciation: ")
# Accès à la variable de classe
MyClass.print_class_variable()      # Output: 999999
printLine()

# Instanciation d'objets
obj1 = MyClass(20)
obj2 = MyClass(30)

print("After Instanciation: ")
# Accès à la variable de classe à partir des instances
MyClass.print_class_variable()      # Output: 999999
obj1.print_instance_variable()      # Output: 20
obj1.print_object_class_variable()  # Output: 999999
obj2.print_instance_variable()      # Output: 30
obj2.print_object_class_variable()  # Output: 999999
printLine()

# Modification de la variable de classe
MyClass.class_variable = 69

print("After Modification of class_variable: ")
# Accès à la variable de classe à partir des instances
MyClass.print_class_variable()      # Output: 69
obj1.print_instance_variable()      # Output: 20
obj1.print_object_class_variable()  # Output: 69
obj2.print_instance_variable()      # Output: 30
obj2.print_object_class_variable()  # Output: 69
printLine()

# Modification de la variable de classe à partir des instances
obj1.class_variable = 369
print("After Modification of class_variable via obj1: ")
MyClass.print_class_variable()      # Output: 69
obj1.print_instance_variable()      # Output: 20
obj1.print_object_class_variable()  # Output: 369
obj2.print_instance_variable()      # Output: 30
obj2.print_object_class_variable()  # Output: 69
printLine()
