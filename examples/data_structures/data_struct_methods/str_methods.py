# Create a string
my_string = "hello"

# capitalize(): Returns a copy of the string with the first character capitalized
capitalized_string = my_string.capitalize()
print("Capitalized string:", capitalized_string)

# lower(): Returns a copy of the string converted to lowercase
lowercase_string = my_string.lower()
print("Lowercase string:", lowercase_string)

# upper(): Returns a copy of the string converted to uppercase
uppercase_string = my_string.upper()
print("Uppercase string:", uppercase_string)

# title(): Returns a copy of the string with the first character of each word capitalized
titlecased_string = my_string.title()
print("Titlecased string:", titlecased_string)

# strip(): Returns a copy of the string with leading and trailing whitespace removed
stripped_string = my_string.strip()
print("Stripped string:", stripped_string)

# isalnum(): Returns True if all characters in the string are alphanumeric
print("Is 'hello123' alphanumeric?", "hello123".isalnum())

# isalpha(): Returns True if all characters in the string are alphabetic
print("Is 'hello' alphabetic?", "hello".isalpha())

# isnumeric(): Returns True if all characters in the string are numeric
print("Is '123' numeric?", "123".isnumeric())

# islower(): Returns True if all characters in the string are lowercase
print("Is 'hello' lowercase?", "hello".islower())

# isupper(): Returns True if all characters in the string are uppercase
print("Is 'HELLO' uppercase?", "HELLO".isupper())

# startswith(): Returns True if the string starts with the specified prefix
print("Does 'hello' start with 'he'?", "hello".startswith("he"))

# endswith(): Returns True if the string ends with the specified suffix
print("Does 'hello' end with 'lo'?", "hello".endswith("lo"))

# find(): Returns the lowest index of the substring if found in the string; otherwise returns -1
print("Index of 'lo' in 'hello':", "hello".find("lo"))

# replace(): Returns a copy of the string with all occurrences of a substring replaced with another substring
replaced_string = my_string.replace("hello", "world")
print("Replaced string:", replaced_string)

# split(): Splits the string into a list of substrings based on a delimiter
splitted_string = "hello world".split(" ")
print("Splitted string:", splitted_string)

# join(): Joins the elements of an iterable into a string using the specified separator
joined_string = "-".join(["hello", "world"])
print("Joined string:", joined_string)

# __len__(): Returns the length of the string
print("__len__ method:", my_string.__len__())
# Equivalent to : print("__len__ method:", len(my_string))

# __getitem__(): Returns the character at the specified index
print("__getitem__ method:", my_string.__getitem__(2))
# Equivalent to : print("__getitem__ method:", my_string[2])

# __repr__(): Returns a string representation of the string
print("String representation of the string:", my_string.__repr__())
# Equivalent to : print("__repr__ method:", repr(my_string))

# __hash__(): Returns the hash value of the string
print("Hash value of the string:", my_string.__hash__())
# Equivalent to : print("__hash__ method:", hash(my_string))

# __str__(): Returns a string representation of the string
print("String representation of the string:", my_string.__str__())
# Equivalent to : print("__str__ method:", str(my_string))

# __eq__(): Compares the string with another string for equality
print("Equality comparison with another string:", my_string.__eq__("hello"))
# Equivalent to : print("__eq__ method:", my_string == "hello")

# __ne__(): Compares the string with another string for not equality
print("Not equality comparison with another string:", my_string.__ne__("world"))
# Equivalent to : print("__ne__ method:", my_string != "hello")

# __lt__(): Compares the string with another string for less than
print("Less than comparison with another string:", my_string.__lt__("world"))
# Equivalent to : print("__lt__ method:", my_string < "hello")

# __le__(): Compares the string with another string for less than or equal to
print("Less than or equal to comparison with another string:", my_string.__le__("hello"))
# Equivalent to : print("__le__ method:", my_string <= "hello")

# __gt__(): Compares the string with another string for greater than
print("Greater than comparison with another string:", my_string.__gt__("hello"))
# Equivalent to : print("__gt__ method:", my_string > "hello")

# __ge__(): Compares the string with another string for greater than or equal to
print("Greater than or equal to comparison with another string:", my_string.__ge__("hello"))
# Equivalent to : print("__ge__ method:", my_string >= "hello")

# __iter__(): Returns an iterator over the characters of the string
iterator = my_string.__iter__()
# Equivalent to : iterator = iter(my_string)

print("Characters of the string using iterator:")
for char in iterator:
    print(char)

# __contains__(): Checks if a substring is present in the string
print("Is 'lo' present in 'hello'?", my_string.__contains__("lo"))
# Equivalent to : print("Is 'lo' present in 'hello'?", "lo" in my_string)
