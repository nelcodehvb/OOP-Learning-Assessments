class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        target.health -= self.attack_power
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage!")
        print(f"{target.name} deals {self.name} damage.")
        print(f"{target.name} now has only {target.health} health.")
       
    def heal(self, amount):
        self.health += amount
       
guin = Player("Guinevere", 100, 10)
silvanna = Player("Silvanna", 100, 20)

while guin.health > 0 and silvanna.health > 0:
   
    guin.attack(silvanna)
    if silvanna.health <= 0:
        print(f"{guin.name} wins!")
        break
   
    silvanna.attack(guin)
    if guin.health <= 0:
        print(f"{silvanna.name} wins!\n")
        break
       

guin.heal(100)
print("------------------------------------------------")
print(f"{guin.name} restores health and now has {guin.health} again.")
