class Toy():
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describeToy(self):
        print(f"This {self.name} toy is {self.price} pesos.")

class Car(Toy):
    def __init__(self, name, price):
        super().__init__(name, price)

laruan = Toy("Mc Queen", 500)
laruan.describeToy()