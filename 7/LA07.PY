class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car = Car("BMW", "Purple")
car.brand = "Ferrari"
car.color = "Pink"

print(car.brand)
print(car.color)

cars = Car("Lamborgini", "Yellow")

print(cars.brand)
print(cars.color)
