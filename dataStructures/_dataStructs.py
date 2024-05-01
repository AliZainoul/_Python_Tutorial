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

printLine("# Example of a string")
my_string = "hello"
# Test for the line: String & No & Yes & Yes & No & Yes
print("Assignable:", hasattr(my_string, '__setitem__'))     # Output: False
print("Subscriptable:", hasattr(my_string, '__getitem__'))  # Output: True
print("Ordered:", hasattr(my_string, '__getitem__'))        # Output: True
print("Mutable:", is_mutable(my_string))                    # Output: False
print("Hashable:", not is_mutable(my_string))               # Output: True
print("Copiable:", hasattr(my_string, 'copy'))              # Output: False


printLine("# Example of a tuple")
my_tuple = (1, 2, 3)
# Test for the line: Tuple & No & Yes & Yes & No & Yes
print("Assignable:", hasattr(my_tuple, '__setitem__'))      # Output: False
print("Subscriptable:", hasattr(my_tuple, '__getitem__'))   # Output: True
print("Ordered:", hasattr(my_tuple, '__getitem__'))         # Output: True
print("Mutable:", is_mutable(my_tuple))                     # Output: False
print("Hashable:", not is_mutable(my_tuple))                # Output: True
print("Copiable:", hasattr(my_tuple, 'copy'))               # Output: False

printLine("# Example of a list")
my_list = [1, 2, 3]
# Test for the line: List & Yes & Yes & Yes & Yes & No
print("Assignable:", hasattr(my_list, '__setitem__'))       # Output: True
print("Subscriptable:", hasattr(my_list, '__getitem__'))    # Output: True
print("Ordered:", hasattr(my_tuple, '__getitem__'))         # Output: True
print("Mutable:", is_mutable(my_list))                      # Output: True
print("Hashable:", not is_mutable(my_list))                 # Output: False
print("Copiable:", hasattr(my_list, 'copy'))                # Output: True

printLine("# Example of a set")
my_set = {1, 2, 3}
# Test for the line: Set & No & No & No & Yes & No
print("Assignable:", hasattr(my_set, '__setitem__'))        # Output: False
print("Subscriptable:", hasattr(my_set, '__getitem__'))     # Output: False
print("Ordered:", hasattr(my_set, '__getitem__'))           # Output: False
print("Mutable:", is_mutable(my_set))                       # Output: True
print("Hashable:", not is_mutable(my_set))                  # Output: False
print("Copiable:", hasattr(my_set, 'copy'))                 # Output: True

printLine("# Example of a frozenset")
my_frznset = frozenset([1, 2, 3])
# Test for the line: FrozenSet & No & No & No & No & Yes
print("Assignable:", hasattr(my_frznset, '__setitem__'))    # Output: False
print("Subscriptable:", hasattr(my_frznset, '__getitem__')) # Output: False
print("Ordered:", hasattr(my_frznset, '__getitem__'))       # Output: False
print("Mutable:", is_mutable(my_frznset))                   # Output: False
print("Hashable:", not is_mutable(my_frznset))              # Output: True
print("Copiable:", hasattr(my_frznset, 'copy'))             # Output: True

printLine("# Example of a dictionary")
my_dict = {'a': 1, 'b': 2, 'c': 3}
# Test for the line: Dict & Yes & Yes & Yes 3.7/No & Yes & No
print("Assignable:", hasattr(my_dict, '__setitem__'))       # Output: True
print("Subscriptable:", hasattr(my_dict, '__getitem__'))    # Output: True
print("Ordered:", hasattr(my_dict, '__getitem__'))          # Output: True if version >= 3.7 else False
print("Mutable:", is_mutable(my_dict))                      # Output: True
print("Hashable:", not is_mutable(my_dict))                 # Output: False
print("Copiable:", hasattr(my_dict, 'copy'))                # Output: True