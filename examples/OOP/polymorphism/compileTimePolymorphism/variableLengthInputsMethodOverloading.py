'''
class MathOperations: 
    @classmethod
    def add(cls, a, b): 
        return a + b 
    
    @classmethod
    def add(cls, a, b, c): 
        return a + b + c 

    @classmethod
    def add(cls, a, b, c, d): 
        return a + b + c + d 

# print(MathOperations.add(1,2))        # Will cause error
# print(MathOperations.add(1,2,3))      # Will cause error
print(MathOperations.add(1,2,3,4))
'''

'''
class MathOperations:
    @classmethod
    def add(cls, a, b, c=None, d=None): 
        if c is None and d is None:
            return a + b
        elif d is None:
            return a + b + c
        else:
            return a + b + c + d

print(MathOperations.add(1, 2))        # Output: 3
print(MathOperations.add(1, 2, 3))     # Output: 6
print(MathOperations.add(1, 2, 3, 4))  # Output: 10
'''

'''
class MathOperations:
    @classmethod
    # Function to take multiple arguments
    def add(cls, *args):
        # Traverse through the arguments
        answer = 0
        for x in args:
            # This will do addition if the
            # arguments are int. Or concatenation
            # if the arguments are str
            answer += x
        return answer

print(MathOperations.add(1, 2))        # Output: 3
print(MathOperations.add(1, 2, 3))     # Output: 6
print(MathOperations.add(1, 2, 3, 4))  # Output: 10
'''



"""
all these examples are equivalent to :

'''
class MathOperations: 
    @staticmethod
    def add(a, b): 
        return a + b 
    
    @staticmethod
    def add(a, b, c): 
        return a + b + c 

    @staticmethod
    def add(a, b, c, d): 
        return a + b + c + d 

# print(MathOperations.add(1,2))        # Will cause error
# print(MathOperations.add(1,2,3))      # Will cause error
print(MathOperations.add(1,2,3,4))
'''

'''
class MathOperations:
    @staticmethod
    def add(a, b, c=None, d=None): 
        if c is None and d is None:
            return a + b
        elif d is None:
            return a + b + c
        else:
            return a + b + c + d

print(MathOperations.add(1, 2))        # Output: 3
print(MathOperations.add(1, 2, 3))     # Output: 6
print(MathOperations.add(1, 2, 3, 4))  # Output: 10
'''


"""
class MathOperations:
    @staticmethod
    # Function to take multiple arguments
    def add(*args):
        answer = 0
        # Traverse through the arguments
        for x in args:
            # This will do addition if the
            # arguments are int. Or concatenation
            # if the arguments are str
            answer += x
        return answer

print(MathOperations.add(1, 2))        # Output: 3
print(MathOperations.add(1, 2, 3))     # Output: 6
print(MathOperations.add(1, 2, 3, 4))  # Output: 10

# https://www.geeksforgeeks.org/python-method-overloading/