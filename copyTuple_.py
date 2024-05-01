import copy

# Creating an original Tuple
t1 = (1, 2, 3)

# Copies of the original Tuple
t2 = t1
t3 = t1[:]
# t4 = t1.copy() # tuple objects does not have copy method
t5 = copy.deepcopy(t1)
tuples = [t1, t2, t3, t5]

def print_tuples():
    for tuple in tuples:
        print(tuple)

# Before modification of t1
print("# Before modification of t1")
print_tuples()

"""
Tuple objects are: 
    subscriptable, but not assignable 
    and no methods are allowing to modify them
    hence they are immutable (not modifiable)
"""