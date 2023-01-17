class Car:

    wheels = 4

    def __init__(self):
        self.mil = 10
        self.com = 'CTS'

c1 = Car()
c2 = Car()

c1.mil = 8

Car.wheels = 16

print(c1.mil, c1.com,'Wheels are: ', c1.wheels)
