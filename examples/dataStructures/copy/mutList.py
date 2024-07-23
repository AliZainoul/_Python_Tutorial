# Identity Operator
l1 = [10,20]
l2 = l1

print(f"l1 is l2: {l1 is l2}") 
# True if l1 and l2 reference the same object

def printline():
    print("----"*10)

printline()

print("BEFORE MODIFICATION")
print(f"l1 is {l1}")
print(f"l2 is {l2}")
print(f"ref of l1 is {id(l1)}")
print(f"ref of l2 is {id(l2)}")
printline()

l1 = [13,20]

print("AFTER MODIFICATION")
print(f"l1 is {l1}")
print(f"l2 is {l2}")
print(f"ref of l1 is {id(l1)}")
print(f"ref of l2 is {id(l2)}")
printline()

"""
----------------------------------------
l1 is l2: True
BEFORE MODIFICATION
l1 is [10, 20]
l2 is [10, 20]
ref of l1 is 4416514368
ref of l2 is 4416514368
----------------------------------------
AFTER MODIFICATION
l1 is [13, 20]
l2 is [10, 20]
ref of l1 is 4416514240
ref of l2 is 4416514368
----------------------------------------
"""
