"""
Set objects are: 
    not subscriptable and not assignable 
    but there is methods allowing to modify them
    hence they are mutable (modifiable)

    BUT: NO NESTED LEVELS are allowed so we cannot do something like:
        t = (2,[3,4])
        original_set = {1, t}
        print(original_set)
        '''
            TypeError: unhashable type: 'list'
        '''
        # l = [2,3]
        # original_set = {1, l, 4}
        '''
            TypeError: unhashable type: 'list'
        '''

        # s = {2,3}
        # original_set = {1, s, 4}
        '''
            TypeError: unhashable type: 'set'
        '''

        # d = {'a': 2, 'b': 3}
        # original_set = {1, d, 4}
        '''
            TypeError: unhashable type: 'dict'
        '''
    HOWEVER: we can have nested sets:
"""


"""
In Python, sets require their elements to be hashable. 
Hashable types are those that can be converted to a hash value, such as integers, strings, and tuples 
    containing only hashable elements. 
Mutable types like lists, sets, and dictionaries are not hashable because their values can change after they're added to a set.

TypeError: unhashable type: 'list': 
    Occurs when trying to create a set with a list as an element. 
    Lists are mutable, so they cannot be hashed, leading to this error.
TypeError: unhashable type: 'set': 
    Happens when attempting to include a set as an element in a set. 
    Similar to lists, sets are mutable and cannot be hashed.
TypeError: unhashable type: 'dict': 
    Occurs when trying to add a dictionary as an element in a set. 
    Dictionaries are also mutable and not hashable.
TypeError: unhashable type: 'list': 
    This error occurs when trying to add a tuple containing a list as an element to a set. 
    Although tuples are generally hashable, this tuple contains an unhashable list, causing the error.
"""