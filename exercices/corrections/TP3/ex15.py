from typing import Set, Tuple

def print_string(s) -> None:
    print('----' * 9 + s + '----' * 9 + "\n")

def get_set_inputs() -> Tuple[Set, Set]:
    set1 = {int(el) for el in set(input("Please  enter the elements of the first set: ").split())}
    set2 = {int(el) for el in set(input("Please  enter the elements of the second set: ").split())}
    return (set1, set2)

def apply_operations_on_sets(first_set: Set, second_set: Set) -> None:
    # UNION |
    print_string("UNION |")
    print(f"The union of {first_set} and {second_set} is : {first_set | second_set}.")
    # Equivalent to: print(first_set.union(second_set))

    # INTERSECTION &
    print_string("INTERSECTION &")
    print(f"The intersection of {first_set} and {second_set} is : {first_set & second_set}.")
    # Equivalent to: print(first_set.intersection(second_set))

    # DIFFERENCE -
    print_string("DIFFERENCE -")
    print(f"The difference of {first_set} and {second_set} is : {first_set - second_set}.")
    # Equivalent to: print(first_set.difference(second_set))

    # SYMMETRICAL DIFFERENCE ^
    print_string("SYMMETRICAL DIFFERENCE ^")
    print(f"The symmetrical difference of {first_set} and {second_set} is : {first_set ^ second_set}.")
    # Equivalent to: print(first_set.symmetric_difference(second_set))

first_set, second_set = get_set_inputs()
apply_operations_on_sets(first_set, second_set)