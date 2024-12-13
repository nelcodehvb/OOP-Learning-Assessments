class Dog:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Bark!")

class Cat:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Meow")

class Bird:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: Chirp")

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name}: ...")

dog = Dog("Jefferson")
cat = Cat("Micha")
bird = Bird("Tweety")
fish = Fish("Nemo")

def animal_sounds(animals):
    animal.speak()

animals = [dog, cat, bird, fish]
for animal in animals:
    animal.speak()