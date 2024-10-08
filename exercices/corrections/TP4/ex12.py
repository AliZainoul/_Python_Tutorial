from math import prod

def inputs_to_list_floats() -> list[float]:
    list_of_strs : list[str] = input("Please enter as many args (floats) do you want: \n").split()
    list_of_floats : list[float] = [float(el) for el in list_of_strs]
    return list_of_floats

def validate_operation (operation : str):
    if (    operation != "ADD" 
        and operation != "SUB" 
        and operation != "PROD" 
        and operation != "DIV"
        and operation != "EDIV"
        and operation != "MOD"):
        print("Invalid operation, please try again !")
        return False
    return True
    
def validate_inputs(*args):
    return all(isinstance(arg, float) for arg in args)

operator = input(
        "Please enter one of the following operations: \n \
        ADD | SUB | PROD : \n")
lf = inputs_to_list_floats()


def perform_operation(operation : str, *args) -> float:
    if(not validate_operation(operation)):
        print("Please enter a valid operation and/or a valid inputs. ")
        return -1
    
    if (not validate_inputs(*args)):
        print("Please enter a valid operation and/or a valid inputs. ")
        return -1
    else:
        dict_opts = {
            "ADD" : sum(args), 
            "SUB" : -sum(args), 
            "PROD": prod(args)  
        }
        return dict_opts[operation]

    
print(operator)
print(lf)
print(perform_operation(operator, *lf))