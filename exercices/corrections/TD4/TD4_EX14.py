code = f"""
tuple([float(el) for el in input("Please enter two numbers a and b :").split()])
"""
a,b = eval(code)
print(f'a = {a} ; b = {b}')


# TODO:
# perform_operations = f""" tup = (a+b, a-b, a*b, a/b) """
# perform_operations = f"""dict({"ADD": a+b, "SUB" : a-b, "MULT": a*b, "DIV" : a/b})"""

perform_operations = f""" (a+b, a-b, a*b, a/b) """
res = eval(perform_operations)
print(type(res))
print(f'res = {res}')
