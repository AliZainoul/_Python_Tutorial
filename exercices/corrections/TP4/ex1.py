class Hello:
    def __init__(self, name=  "World !"):
        self.name = name

    def __str__(self):
        return f"Hello {self.name}"


h1 = Hello()
print(str(h1))
#print(h1.__str__())

h2 = Hello(input("Please enter your name ? \n"))
print(str(h2))
#print(h2.__str__())