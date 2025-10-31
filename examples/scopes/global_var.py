# Example of global variable with global

global_var = 0
print("Global Scope *before* calling foo() and bar(): global_var = ", global_var)
# Output : Global Scope *before* calling foo(): global_var =  0
def foo():
    global_var = 1
    print("Inside foo()'s Local Scope: global_var = ", global_var)

foo()
# Output : Inside foo()'s Local Scope: global_var =  1
print("Global Scope *after* calling foo(): global_var = ", global_var)
# Output : Global Scope *after* calling foo(): global_var =  0

def bar():
    global global_var
    global_var = 2
    print("Inside bar()'s Local Scope: global_var = ", global_var)

bar()
# Output : Inside bar()'s Local Scope: global_var =  2

print("Global Scope *after* calling bar(): global_var = ", global_var)
# Output : Global Scope *after* calling bar(): global_var =  2

global_var = 3
print("Global Scope *after* modifying: global_var = ", global_var)
# Output : Global Scope *after* calling bar(): global_var =  3