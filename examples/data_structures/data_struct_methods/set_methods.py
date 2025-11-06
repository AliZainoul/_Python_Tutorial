# Create a set
my_set : set = {1, 2, 3, 4, 5}

# add(): Adds an element to the set
my_set.add(6)
print("Set after add:", my_set)

# update(): Updates the set by adding elements from another iterable
my_set.update({7, 8})
print("Set after update:", my_set)

# remove(): Removes the specified element from the set
my_set.remove(6)
print("Set after remove:", my_set)

# discard(): Removes the specified element from the set if present
my_set.discard(8)
print("Set after discard:", my_set)

# pop(): Removes and returns an arbitrary element from the set
popped_item = my_set.pop()
print("Popped item:", popped_item)
print("Set after pop:", my_set)

# clear(): Removes all elements from the set
my_set.clear()
print("Set after clear:", my_set)

# copy(): Returns a shallow copy of the set
new_set = {1, 2, 3, 4, 5}
copied_set = new_set.copy()
print("Copied set:", copied_set)

# difference(): Returns a set containing the difference between two or more sets
difference_set = {1, 2, 3} - {3, 4, 5}
print("Difference set:", difference_set)

# intersection(): Returns a set containing the intersection of two or more sets
intersection_set = {1, 2, 3} & {3, 4, 5}
print("Intersection set:", intersection_set)

# union(): Returns a set containing the union of sets
union_set = {1, 2, 3} | {3, 4, 5}
print("Union set:", union_set)

# symmetric_difference(): Returns a set with the symmetric differences of two sets
symmetric_difference_set = {1, 2, 3} ^ {3, 4, 5}
print("Symmetric difference set:", symmetric_difference_set)

# isdisjoint(): Checks if two sets have no elements in common
print("Are {1, 2} and {3, 4} disjoint?", {1, 2}.isdisjoint({3, 4}))

# issubset(): Checks if all elements of one set are present in another set
print("{1, 2} is a subset of {1, 2, 3}?", {1, 2}.issubset({1, 2, 3}))

# issuperset(): Checks if a set contains all elements of another set
print("{1, 2, 3} is a superset of {1, 2}?", {1, 2, 3}.issuperset({1, 2}))

# __len__(): Returns the number of elements in the set
print("__len__ method:", new_set.__len__())

# __iter__(): Returns an iterator over the elements of the set
iterator = new_set.__iter__()
print("Elements of the set using iterator:")
for item in iterator:
    print(item)

# __contains__(): Checks if a value is present in the set
print("Is 3 present in the set?", new_set.__contains__(3))