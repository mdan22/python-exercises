#Klassen und Objekte

class Car:
    def __init__(self):
        self.car_brand = None
        self.horse_power = None
        self.color = None
        self.x_position = 5
        self.y_position = 5

    def drive(self, x, y):
        self.x_position += x
        self.y_position += y


car1 = Car()
print(car1.x_position)
print(car1.y_position)
car1.drive(5,10)
print(car1.x_position)
print(car1.y_position)