class MyIterable:
    def __init__(self, max):
        self.max = max
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration
        

# Using the iterable
my_iterable = MyIterable(5)
# next(my_iterable)
# my_iterable.__next__()
for element in my_iterable:
    print(element)