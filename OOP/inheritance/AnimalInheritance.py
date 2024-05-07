class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Labrador(Dog):
    def speak(self):
        return "Labrador barks"

# Utilisation de issubclass()
print(issubclass(Dog, Animal))  # Output: True

# Utilisation de super()
labrador = Labrador()
print(super(Labrador, labrador).speak())  # Output: Dog barks

# Utilisation de mro()
print(Labrador.mro())  # Output: [Labrador, Dog, Animal, object]
