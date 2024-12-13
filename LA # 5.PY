class MobileHero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        print(f"{self.name} is a/an {self.role} hero.")

fighter = MobileHero("Guinevere", "fighter")
mage = MobileHero("Kagura", "mage")

fighter.describe()
mage.describe()