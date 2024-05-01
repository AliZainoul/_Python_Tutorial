def printLine(s):
    print("-"*32 + s + "-"*32)

def is_mutable(obj):
    dict_mutable = {
    'str':          False, 
    'tuple':        False, 
    'list':         True, 
    'set':          True,  
    'frozenset':    False, 
    'dict':         True,
    }
    return dict_mutable[type(obj).__name__]

def printStructInfos(struct):
    print("Assignable:",    hasattr(struct, '__setitem__'))     
    print("Subscriptable:", hasattr(struct, '__getitem__'))  
    print("Ordered:",       hasattr(struct, '__getitem__'))        
    print("Mutable:",       is_mutable(struct))                    
    print("Hashable:",      not is_mutable(struct))               
    print("Copiable:",      hasattr(struct, 'copy'))              

printLine("# Example of a string")
my_string = "hello"
printStructInfos(my_string)
# Output: False, True, True, False, True, False

printLine("# Example of a tuple")
my_tuple = (1, 2, 3)
printStructInfos(my_tuple)
# Output: False, True, True, False, True, False

printLine("# Example of a list")
my_list = [1, 2, 3]
printStructInfos(my_list)
# Output: True, True, True, True, False, True

printLine("# Example of a set")
my_set = {1, 2, 3}
printStructInfos(my_set)
# Output: False, False, False, True, False, True

printLine("# Example of a frozenset")
my_frznset = frozenset([1, 2, 3])
printStructInfos(my_frznset)
# Output: False, False, False, False, True, True

printLine("# Example of a dictionary")
my_dict = {'a': 1, 'b': 2, 'c': 3}
printStructInfos(my_dict)
# Output: True, True, True, True, False, True