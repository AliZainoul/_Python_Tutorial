class TestClass:
    def __init__(self):
        self.__private_attr = "I am private"
    def __private_method(self):
        return "Private Method"
    def access_private_in_A(self):
        return self.__private_method(), self.__private_attr

