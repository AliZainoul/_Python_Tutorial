class myClass:
    def __init__(self, a=0, b=1,c=2):
        # self.a is a PUBLIC member of class A
        self.a = a
        # self._b is a PROTECTED member of class A
        self._b = b        
        # self.__c is a PRIVATE member of class A
        self.__c = c

    # Because the method display_infos is inside the class myClass, it has the access to private member __c
    def display_infos(self):
        return f"Public member a = {self.a}; Protected member b = {self._b}; Private member c = {self.__c}"
