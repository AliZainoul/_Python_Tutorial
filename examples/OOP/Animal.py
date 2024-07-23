class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass
    
    def animal_sounds(self):
        self.make_sound()


class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")



dog = Dog("Rufus")
cat = Cat("Whiskers")

dog.make_sound()
cat.make_sound()
dog.animal_sounds()
cat.animal_sounds()