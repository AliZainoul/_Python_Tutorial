def printline():
    print("___" * 16)

# IMMUTABLES: 
printline()
x_int = 10
y_int = 10
print(x_int == y_int)
print(x_int is y_int)
printline()

x_float = 10.9
y_float = 10.9
print(x_float == y_float)
print(x_float is y_float)
printline()

x1_float = 10.9
y1_float = 10.90
print(x1_float == y1_float)
print(x1_float is y1_float)
printline()

x2_float = 10.9
y2_float = 10.9000000000000007
print(x2_float == y2_float)
print(x2_float is y2_float)
printline()

x_str = "Hello"
y_str = 'Hello'
print(x_str == y_str)
print(x_str  is y_str)
printline()

x_tuple = (1,2,3)
y_tuple = (1,2,3)
print(x_tuple == y_tuple)
print(x_tuple  is y_tuple)
printline()

# MUTABLES:

x_list = [1,2,3]
y_list = [1,2,3]
print(x_list == y_list)
print(x_list  is y_list)
printline()

l1 = [1,2,3]
l2 = l1
print(l1 == l2)
print(l1 is l2)
printline()