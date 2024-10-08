class Hello:
    def __init__(self, msg : str = "Hello", name: str = ""):
        self.msg = msg
        self.name = name

    def greet(self, _name : str = "World !"):
        if (_name != "World !"):
            self.set_name(_name)
        return f"{self.msg} {self.name}."
    
    def set_name(self, _name: str) -> None:
        self.name = _name


h1 = Hello()
print(h1.greet())
print(h1.greet(input("Please enter your name ? \n")))