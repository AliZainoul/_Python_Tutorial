def add_all(*numbers):
    return sum(numbers)

args = [int(s) for s in input().split()]

print(add_all(*args))
