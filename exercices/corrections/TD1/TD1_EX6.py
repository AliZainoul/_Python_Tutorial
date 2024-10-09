def stats_of_list_of_strings(list_of_strings):
    for s in list_of_strings:
        print(f"The string {s}, has type {type(s)}, and it's length is {len(s)}.")
        # Equivalent to:
        # print("The string",s, "has type " ,type(s), "and it's length is " ,len(s), ".")

ls = input("Please enter a list of strings separated by a space : \n").split(" ")
stats_of_list_of_strings(ls)