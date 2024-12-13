class MobileHero():
    def __init__(self, name, role):
        self.name = name
        self.role = role

fighter = MobileHero("Guinevere", "fighter")
mage = MobileHero("Kagura", "mage")

print(fighter.name)
print(fighter.role)
print(mage.name)
print(mage.role)