class Person :
    def __init__(self, name): 
        self.__name = name

    def get_name(self):
        return self.__name

def main():
    p = Person("Ali")
    print(p.get_name())
    print(p.__dict__)  # Shows that __name is still the original, and a new __name attribute exists
    # print(p.__name)  # This will raise an AttributeError
    p.__name = "Veli"  # This creates a new attribute, does not modify the original
    print(p.__dict__)  # Shows that __name is still the original, and a new __name attribute exists
    print(p.get_name())  # Still prints "Ali"


if __name__ == "__main__":
    main()
