class MyClass:
    def __init__(self):
        self.public_attribute       = "Public Attribute"
        self._protected_attribute   = "Protected Attribute"
        self.__private_attribute    = "Private Attribute"

    def public_display_infos(self):
        return f"INSIDE PUBLIC METHOD: public_display_infos                     \n      \
            (   Access to public_attribute      = {self.public_attribute},      \n      \
                Access to _protected_attribute  = {self._protected_attribute},  \n      \
                Access to __private_attribute   = {self.__private_attribute})   \n" 
    
    def _protected_display_infos(self):
        return f"INSIDE PROTECTED METHOD: _protected_display_infos              \n      \
            (   Access to public_attribute      = {self.public_attribute},      \n      \
                Access to _protected_attribute  = {self._protected_attribute},  \n      \
                Access to __private_attribute   = {self.__private_attribute})   \n"
    
    def __private_display_infos(self):
        return f"INSIDE PRIVATE METHOD: __private_display_infos                 \n      \
            (   Access to public_attribute      = {self.public_attribute},      \n      \
                Access to _protected_attribute  = {self._protected_attribute},  \n      \
                Access to __private_attribute   = {self.__private_attribute})   \n"

    def _indirect_access_to__private_display_infos(self):
        return    "INSIDE PROTECTED METHOD: _indirect_access_to__private_display_infos \n" \
                + "INDIRECT ACCESS TO PRIVATE METHOD: \n" \
                + self.__private_display_infos()
