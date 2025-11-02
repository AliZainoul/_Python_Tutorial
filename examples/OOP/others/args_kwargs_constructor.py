class MyClass :
    def __init__(self, *args, **kwargs):
        self.member_list = []
        self.member_dict = {}
        for arg in args :
            print("Arg:", arg)
            self.member_list.append(arg)

        for key , value in kwargs.items () :
            print("Keyword arg − {}: {}".format(key, value))
            self.member_dict[key] = value

    def __str__(self):
        return f"MyClass with list: {self.member_list} and dict: {self.member_dict}"


def main()-> None:
    """ Main function to demonstrate the class MyClass """
    print("Instantiating MyClass with various arguments...\n")

    # Instanciation de l 'objet avec différents types d'arguments
    obj1 = MyClass(1, 2, 3, name="Alice", age=30) 
    obj2 = MyClass("Hello" , name="Bob" , age=25)

    # Affichage des objets
    print(obj1)
    print(obj2)


if __name__ == "__main__":
    main()