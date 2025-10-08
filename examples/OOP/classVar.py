def print_separator():
    print("-" * 69)

class MyClass:
    # Class Variable
    class_variable = 999
    
    # Constructor
    def __init__(self, value: int):
        self.instance_variable = value

    # Regular Methods
    def print_instance_variable(self):
        print("object.instance_variable:", self.instance_variable)

    def print_class_variable_of_obj(self):
        print("self.class_variable:", self.class_variable)


    # Static Methods
    @staticmethod
    def print_all_info(obj1: 'MyClass', obj2: 'MyClass'):
        MyClass.print_class_variable()      
        obj1.print_instance_variable()      
        obj1.print_class_variable_of_obj()         
        obj2.print_instance_variable()      
        obj2.print_class_variable_of_obj()   
        print(id(MyClass.class_variable))
        print(id(obj1.class_variable))  
        print(id(obj2.class_variable))  
        print_separator()

    # Class Methods
    @classmethod
    def print_class_variable(cls):
        print("cls.class_variable:", cls.class_variable)



def main():
    print_separator()

    # Instantiation and usage
    print("Before Instantiation:")
    MyClass.print_class_variable()
    print_separator()

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

if __name__ == "__main__":
    main()


'''
# OUTPUT:
---------------------------------------------------------------------
Before Instantiation:
cls.class_variable: 999
---------------------------------------------------------------------
After Instantiation:
cls.class_variable: 999
object.instance_variable: 20
self.class_variable: 999
object.instance_variable: 30
self.class_variable: 999
4502575152
4502575152
4502575152
---------------------------------------------------------------------
After Modification of class_variable:
cls.class_variable: 69
object.instance_variable: 20
self.class_variable: 69
object.instance_variable: 30
self.class_variable: 69
4513681536
4513681536
4513681536
---------------------------------------------------------------------
After Modification of class_variable via obj1:
cls.class_variable: 69
object.instance_variable: 20
self.class_variable: 369
object.instance_variable: 30
self.class_variable: 69
4513681536
4502583088
4513681536
'''