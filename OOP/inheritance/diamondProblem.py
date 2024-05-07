def printText(s):
    print("\n" + "--"*16 + s + "--"*16 +"\n")

# Example that exhibits the Diamond Problem
printText("Original Diamond Problem")

class A:
    def my_method(self):
        print("my_method called from class A")   
     
class B(A):
    def my_method(self):
        print("my_method called from class B")
        A.my_method(self)
 
class C(A):
    def my_method(self):
        print("my_method called from class C")
        A.my_method(self)   
      
class D(C, B):
    def my_method(self):
        print("my_method called from class D") 
        C.my_method(self)
        B.my_method(self)
      
instance_of_class_D = D()
instance_of_class_D.my_method()
print(D.mro())

# OUTPUT: 
'''
my_method called from class D
my_method called from class C
my_method called from class A
my_method called from class B
my_method called from class A
[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
'''


# WHY IT IS A PROBLEM:
'''
The output of the above code has a problem: 
the method my_method of A is called twice. 
This issue arises due to the way method resolution is handled in Python 
    when using explicit calls to methods of base classes.
'''

# SOLUTION:
printText("Solution to the Diamond Problem")

class A:
    def my_method(self):
        print("my_method called from class A")
 
class B(A):
    def my_method(self):
        print("my_method called from class B")
        super().my_method()
 
class C(A):
    def my_method(self):
        print("my_method called from class C")
        super().my_method()
 
class D(C, B):
    def my_method(self):
        print("my_method called from class D")   
        super().my_method()
      
instance_of_class_D = D()
instance_of_class_D.my_method()
print(D.mro())

# OUTPUT:
'''
my_method called from class D
my_method called from class C
my_method called from class B
my_method called from class A
[<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
'''

# EXPLANATION:
'''
The Diamond Problem occurs when multiple inheritance is used 
    and a method of a base class is overridden by subclasses
    along the inheritance path. 
In such cases, the method of the base class is called multiple times, 
    leading to unexpected behavior.

Python's solution to the Diamond Problem involves using the super() function. 
The super() function determines which method to call 
    by following the Method Resolution Order (MRO) of the classes involved. 
By using super(), the method of the base class is called only once, 
    avoiding the issue of duplicate method calls.
'''


'''
It's normal behavior that the MRO returns the same results for mro method 
    before and after using the super() function in the context of the 
    Diamond Problem. The difference lies in how the method resolution 
    is handled when calling methods of base classes.

In the original Diamond Problem example, explicit calls to the 
    base class methods (A.my_method(self)) lead to the method of class A 
    being called twice. This occurs because the method resolution follows 
    the inheritance hierarchy specified in the class definitions (D(B, C)), 
    resulting in my_method of class A being invoked multiple times along 
    the inheritance path.

In the solution using super(), the super() function determines the method 
    to call based on the MRO of the classes involved. 
    This ensures that the method of the base class (A) is called only once, 
    preventing the issue of duplicate method calls.

Although the MRO remains the same, the behavior of method resolution changes 
    due to the use of super(), resulting in the desired outcome of 
    calling the base class method only once.
'''