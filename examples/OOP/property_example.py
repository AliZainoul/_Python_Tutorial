# BEGIN CLASS
class Person:
    def __init__(self, n):
        self.__name = n # __name private member.

    def get_name(self):
        return self.__name
    
    def set_name(self , n):
        self.__name = n

    name = property(get_name, set_name)
# END CLASS


#________________________________________ MAIN ________________________________________#

p = Person("Ali")

# print(p.__name) # private member __name !!! 
# throws : AttributeError: 'Person' object has no attribute '__name'
# throws : AttributeError: 'Person' object has no attribute '__name'. Did you mean: 'name'?

# p.__name = "Alexandre" 
# * DOES NOT MODIFY THE PRIVATE MEMBER __name, HOWEVER IT DOES NOT THROW AN EXCEPTION ! 
# Do not throw an exception at runtime ?! WHY ??

print(f"With getter method get_name : {p.get_name()}")
print(f"With property getter : {p.name}\n") # Calls the getter get_name inside property (name)  !!! 

p.set_name("Alexandre") 
print(f"With getter method get_name : {p.get_name()}")
print(f"With property getter : {p.name}\n") # Calls the getter get_name inside property (name)  !!! 

p.name = "Ali" # Calls the setter set_name inside property (name)  !!! 
print(f"With getter method get_name : {p.get_name()}")
print(f"With property getter : {p.name}\n") # Calls the getter get_name inside property (name)  !!! 

print(type(p.name)) # OUTPUT: <class 'str'> ; prints class str why ? 
# Because of the fact that it calls get_name and the latter returns a string object
print(type(Person.name)) # OUTPUT: <class 'property'> ; prints class property why?
# Because of the fact that "name" is a CLASS VARIABLE of type: object of class "property"