t1 : tuple = (1,2,4,453,53,54,53,5,4,54,46,54,54,544,5,4,54,5,45,54,54)
t2 : tuple = (1,2,4,453,53,54,53,5,4,54,46,54,54,544,5,4,54,5,45,54,54)

print(f"{(t1 == t2) =}")
print(f"{(t1 is t2) =}")

print(id(t1))
print(id(t2))

print(hex(id(t1)))
print(hex(id(t2)))

print(hash(t1))
print(hash(t2))


# EXAMPLE: [Address: 4546928832, Value: (1,2,3)]
# Both t1 and t2 points to [Address: 4546928832, Value: (1,2,3)]

"""
(t1 == t2) =True
(t1 is t2) =True
4546928832
4546928832
-6981140160864087567
-6981140160864087567
"""