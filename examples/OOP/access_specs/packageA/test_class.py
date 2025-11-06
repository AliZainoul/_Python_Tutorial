class TestClass:
    def __init__(self):
        self._protected_attr = "I am protected"
        self.__private_attr = "I am private"
    
    def _protected_method(self):
        return "Protected Method"
    
    def __private_method(self):
        return "Private Method"
    
    def access_private_in_A(self):
        return self.__private_method(), self.__private_attr
