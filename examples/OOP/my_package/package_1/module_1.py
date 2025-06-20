class MyClass :
    def __init__(self) :
        self.public_attribute       =   42 
        self._protected_attribute   =   "protected" 
        self.__private_attribute    =   "private"

    def access_attributes(self) :
        print("Public attribute:",      self.public_attribute) 
        print("Protected attribute:",   self._protected_attribute) 
        print("Private attribute:",     self.__private_attribute)

    def _protected_method(self):
        return "Protected method"
