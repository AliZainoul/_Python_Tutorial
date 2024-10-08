# def print_line():
#     print("---"*16)

# def create_person(**kwargs):
#     person = dict()
#     for key, value in kwargs.items():
#         person[key] = value 
#     return person

# def print_person_info(*args): 
#     print(" Printing person information : ")
#     for person in args:
#         print("Name:", person["name"]) 
#         print("Age:", person["age"])
#         print_line()
                
# # Creating persons using **kwargs
# person1 = create_person(name="Alice" , age=30, city="New York" , occupation="Engineer") 
# person2 = create_person(name="Bob" , age=25, city="Los Angeles" , occupation="Artist") 
# person3 = create_person(name="Charlie" , age=35, city="Chicago")

# # Printing person information 
# print_person_info (person1 , person2 , person3)

def print_line():
    print("---"*16)

def print_person_info(**kwargs): 
    print(" Printing person information : ")
    print_line()
    for key, value in kwargs.items():
        print(f"The key is {key}: associated with value: {value}. \n")
    print_line()
                
# Printing person information using **kwargs 
print_person_info(name="Ali")
print_person_info(name="Alice" , age=30) 
print_person_info(name="Charlie" , age=35, city="Chicago")
print_person_info(name="Bob" , age=25, city="Los Angeles" , occupation="Artist") 

