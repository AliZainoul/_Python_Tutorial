from faker import Faker

N = 100
f = Faker()

list_of_strings : list[str] = [ f.first_name() for _ in range(N) ]
list_of_sizes = list(map(lambda el: len(el), list_of_strings))

print("Starred zip list : ", *zip(list_of_strings, list_of_sizes))

# TODO: why the starred operator is not accepted inside an fstring ?
print(list(filter(lambda el : (el) > 5, list_of_sizes)))