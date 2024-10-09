from faker import Faker

N = 100
f = Faker()
l : list[str] = [ f.first_name() for _ in range(N) ]
print(len(l))
res = list(filter(lambda el : len(el) > 3, l))
# FILTER STRINGS THAT HAVE MORE THAN 3 CHARS
print(len(res))
print(res)