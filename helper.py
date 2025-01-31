def hello():
    print('Hello, have a nice one!')
def Bye():
    print('Dont forget to support me')

class Car:

    wheels = 4

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print('This '+self.model+' is driving')

    def stop(self):
        print('This car is stopped')