
class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def show(self):
        print('Name:', self.name, 'RollNo:', self.rollno)

    class Laptop:

        def __init__(self):
            self.brand = 'DELL'
            self.cpu = 'i7'
            self.ram = 16

        def show(self):
            print('Brand:', self.brand, 'cpu:', self.cpu, 'RAM', self.ram)

s1 = Student('cts', 27)

print(s1.show())

lap = Student.Laptop()

print(lap.show())

