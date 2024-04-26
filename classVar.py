class MyClass:
    class_variable = 999
    
    def __init__(self, instance_variable):
        self.instance_variable = instance_variable

    @classmethod
    def print_class_variable(cls):
        print("cls.class_variable:", cls.class_variable)

    def print_instance_variable(self):
        print("object.instance_variable:", self.instance_variable)

    @staticmethod
    def print_separator():
        print("-" * 69)

    @staticmethod
    def print_all_info(obj1, obj2):
        MyClass.print_class_variable()      
        obj1.print_instance_variable()      
        obj1.print_class_variable()         
        obj2.print_instance_variable()      
        obj2.print_class_variable()        
        MyClass.print_separator()

# Instantiation and usage
MyClass.print_separator()

print("Before Instantiation:")
MyClass.print_class_variable()
MyClass.print_separator()

obj1 = MyClass(20)
obj2 = MyClass(30)
print("After Instantiation:")
MyClass.print_all_info(obj1, obj2)

# Modifying the class variable
MyClass.class_variable = 69
print("After Modification of class_variable:")
MyClass.print_all_info(obj1, obj2)

# Modifying the class variable from instances
obj1.class_variable = 369
print("After Modification of class_variable via obj1:")
MyClass.print_all_info(obj1, obj2)


'''
# OUTPUT:
---------------------------------------------------------------------
Before Instantiation:
cls.class_variable: 999
---------------------------------------------------------------------
After Instantiation:
cls.class_variable: 999
object.instance_variable: 20
cls.class_variable: 999
object.instance_variable: 30
cls.class_variable: 999
---------------------------------------------------------------------
After Modification of class_variable:
cls.class_variable: 69
object.instance_variable: 20
cls.class_variable: 69
object.instance_variable: 30
cls.class_variable: 69
---------------------------------------------------------------------
After Modification of class_variable via obj1:
cls.class_variable: 69
object.instance_variable: 20
cls.class_variable: 69
object.instance_variable: 30
cls.class_variable: 69
---------------------------------------------------------------------
'''