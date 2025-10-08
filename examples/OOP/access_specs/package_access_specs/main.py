from access_specs_methods import MyClass

o = MyClass()

print(o.public_attribute)
print(o.public_display_infos())

# Because of the fact that we are in the same package a.k.a : package_access_specs
# so the access to PROTECTED members and methods is *GRANTED* !
print(o._protected_attribute)
print(o._protected_display_infos())

# ALL PRIVATE MEMBERS AND METHODS ARE *NOT ACCESSIBLE* from outside the class !
# print(o.__private_attribute) # Error because the member is private
# o.__private_display_infos() # Error because the method is private

print(o._indirect_access_to__private_display_infos())

# BECAUSE OF THE FACT THAT WE ARE IN THE SAME PACKAGE *AND* 
# THE FACT THAT WE'RE USING A NAME MANGLING DIRECT ACCESS: 
# THE ACCESS TO PRIVATE MEMBERS AND METHODS IS *GRANTED*
print(o._MyClass__private_attribute)
print(o._MyClass__private_display_infos())






















# from access_specs import myClass

# o = myClass()
# print(o.display_infos())

# # Access to public member a is OK outside the class. 
# print(o.a)

# # Access to protected member _b is OK outside the class (same package !). 
# print(o._b)

# # Because the fact of self.__c is a private member of class myClass, 
# # I cannot access directly to private member __c
# # print(o.__c) 
