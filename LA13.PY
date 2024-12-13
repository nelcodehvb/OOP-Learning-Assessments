class Animal():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describeAnimal(self):
        print(f"This {self.name} fish is {self.type}.")

class Fish(Animal):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.can_swim = True

tilapia = Fish("Tilapia", "fish")
print(tilapia.can_swim)
