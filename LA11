class Phone():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describePhone(self):
        print(f"This {self.brand} has a {self.model} brand.")

class Android(Phone):
    def __init__(self, brand, model):
        Phone.__init__(self, brand, model)

realme = Android("Realme", "5 Pro")
realme.describePhone()