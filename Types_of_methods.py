
class Student:

    school = 'UWM'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_val(self):
        return self.m1

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a student class')

s1 = Student(1, 2, 3)
s2 = Student(20, 40, 80)

print(s1.avg())
print(s2.avg())
print('Mark: ', s1.get_val())

print('SCHOOL NAME: ', Student.getSchool())

Student.info()