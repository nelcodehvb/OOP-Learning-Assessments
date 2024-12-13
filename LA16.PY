class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def operate(self):
        print("Operating!")

    def info(self):
        print(f"This {self.brand} has a {self.model} model.")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Heating food!")

machine = WashingMachine("LG", "Load Washer")
ref = Refrigerator("Midea", "Two-Door")
micro = Microwave("Hanabishi", "RG5678")

appliances = [machine, ref, micro]

for appliance in appliances:
	appliance.operate()
	appliance.info()