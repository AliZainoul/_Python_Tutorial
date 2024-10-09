def gen(N : int):
    for i in range(N):
        yield i 


# my_gen = gen(11)
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))


for _ in gen(11):
    print(_)