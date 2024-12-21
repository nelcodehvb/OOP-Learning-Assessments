class Car:
    def __init__ (self, brand, color):
        self.brand = brand
        self.color = color
    def __str__(self):
        return f"The {self.brand} car has a {self.color} color."
    
car = Car("BMW", "Purple")

print(car)
del car
print(car)
