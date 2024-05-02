# nameMangling and Method Overriding example
class Parent:  
    def __init__(self):  
        self.__method()
          
    # Public method of class Parent
    def method(self):  
        print("In parent class")  
    
    # Private copy of original method()  
    __method = method
    
    # Or make method directly private: def __method(self) ...
class Child(Parent):  
    # Public method of class Child
    def method(self):          
        print("In Child class") 
    # Provides new signature for method() but does not break __init__()

          
# Driver's code 
childObject = Child() 
childObject.method() 