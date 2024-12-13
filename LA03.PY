class MobileHero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def describe(self):
        return f"{self.name} is a/an {self.role} hero."

fighter = MobileHero("Guinevere", "fighter")
mage = MobileHero("Kagura", "mage")

print(fighter.name)
print(fighter.role)
print(fighter.describe())
print(mage.name)
print(mage.role)
print(mage.describe())