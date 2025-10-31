# Identity Operator

l1 = [10,20]
l2 = l1

print(f"l1 is l2: {l1 is l2}") 
# True if l1 and l2 reference the same object

def print_line():
    print("----"*10)

print_line()

print("BEFORE MODIFICATION")
print(f"l1 is {l1}")
print(f"l2 is {l2}")
print(f"ref of l1 is {id(l1)}")
print(f"ref of l2 is {id(l2)}")
print_line()

l1.append(69)

print("AFTER MODIFICATION")
print(f"l1 is {l1}")
print(f"l2 is {l2}")
print(f"ref of l1 is {id(l1)}")
print(f"ref of l2 is {id(l2)}")
print_line()

"""
----------------------------------------
l1 is l2: True
BEFORE MODIFICATION
l1 is [10, 20]
l2 is [10, 20]
ref of l1 is 4426758400
ref of l2 is 4426758400
----------------------------------------
AFTER MODIFICATION
l1 is [10, 20, 69]
l2 is [10, 20, 69]
ref of l1 is 4426758400
ref of l2 is 4426758400
----------------------------------------
"""
