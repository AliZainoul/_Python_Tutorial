from typing import List

def get_inputs() -> List[str]:
    total_number : int = int(input("How many strings do you want to enter ? "))
    return [input(f"Please enter your {index+1} string : \n") for index in range(total_number)]

def join_strings(*args: List[str]) -> str:
    return str(" ".join(args))

def add_strings(*args: List[str]) -> str:
    result  = str()
    for arg in args:
        result += arg + " "
    return result

list_of_strs : List[str] = get_inputs()

result_join_strings = join_strings(*list_of_strs)
print(result_join_strings)

result_add_strings = add_strings(*list_of_strs)
print(result_add_strings)

"""
# Solution for operator + using generators:

from typing import List, Generator

def get_inputs() -> List[str]:
    total_number : int = int(input("How many strings do you want to enter ? "))
    return [input(f"Please enter your {index+1} string : \n") for index in range(total_number)]

def join_strings(*args: List[str]) -> str:
    return str(" ".join(args))

def add_strings(*args: List[str]) -> Generator:
    return ((f"{arg}") for arg in args)

list_of_strs : List[str] = get_inputs()
result_join_strings = join_strings(*list_of_strs)
print(result_join_strings)

result_add_strings = add_strings(*list_of_strs)
print(*result_add_strings)

# Please note the usage of the starred operator in the last line !
"""