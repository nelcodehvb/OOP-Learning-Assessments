class AnimeCharacter:
    def __init__(self, name, ability):
        self.__name = name
        self.ability = ability
    def introduce(self, function_name):
        def initial_function(*args, **kwargs):
            print("Introducing...")
            function_name(*args, **kwargs)
            print(f"This character is amazing!")
        return initial_function

char = AnimeCharacter("Natsu", "Fire Dragon")

@char.introduce
def character_intro(name, ability):
    print(f"I am {name} and I can use {ability}.")

character_intro("Grey", "Ice-Make")