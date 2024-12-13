class BdayParty:
    def __init__(self, theme, food):
        self.theme = theme
        self.food = food

    def foods(self):
        print("Cake, Spaghetti, Pancit...")
        self.__secret_dish()

    def __secret_dish(self):
        print(f"Ang theme ay {self.theme}.")
        print(f"Ang secret dish ay {self.food}.\n")


theme1 = BdayParty("Halloween", "Barbeque")
theme2 = BdayParty("Mafia", "Carbonara")
theme3 = BdayParty("Vegas", "Menudo")


theme1.foods()
theme2.foods()
theme3.foods()