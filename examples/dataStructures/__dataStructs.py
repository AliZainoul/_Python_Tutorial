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

def printStructInfos(containter):
    # print("Assignable                 :",    hasattr(containter, '__setitem__'))
    print("Assignable                   :",    '__setitem__' in dir(containter))
    # print("Subscriptable or Ordered   :", hasattr(containter, '__getitem__'))  
    print(f"Subscriptable or Ordered    :    {'__getitem__' in dir(containter)}")
    print(f"Mutable                     :       {is_mutable(containter)}")                    
    print(f"Hashable                    :      {not is_mutable(containter)}")               
    print(f"Copiable                    :      {'copy' in dir(containter)}")              
    # print(f"Copiable                  :      {hasattr(containter, 'copy')}")              

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