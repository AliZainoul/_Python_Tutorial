def add_all(*args):
    return float(sum(args))

def inputs_to_list_floats() -> list[float]:
    list_of_strs : list[str] = input("Please enter as many args (floats) do you want: \n").split()
    list_of_floats : list[float] = [float(el) for el in list_of_strs]

    return list_of_floats

def validate_inputs(args) -> bool:
    return all(isinstance(arg,float) for arg in args)

lf : list[float] = inputs_to_list_floats()
if (validate_inputs(lf)):
    print(add_all(*lf))