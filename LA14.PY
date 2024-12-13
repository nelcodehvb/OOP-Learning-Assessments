class Spiderman:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describeSpiderman(self):
        print(f"This guy named {self.name} is {self.age} years old.")

class Tobey(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Andrew(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

class Tom(Spiderman):
    def __init__(self, name, age, movieTitle):
        super().__init__(name, age)
        self.movieTitle = movieTitle

tobey = Tobey("Tobey Maguire", 49, "Spiderman 1")
andrew = Andrew("Andrew Garfield", 41, "The Amazing Spiderman")
tom = Tom("Tom Holland", 28, "No Way Home")

print(f"The guy named {tobey.name.upper()} is the main lead in {tobey.movieTitle}.")
print(f"The guy named {andrew.name.upper()} is the main lead in {andrew.movieTitle}.")
print(f"The guy named {tom.name.upper()} is the main lead in {tom.movieTitle}.")