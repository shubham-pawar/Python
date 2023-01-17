
class A:

    def fea1(self):
        print('Feature 1 parent')

    def fea2(self):
        print('Feature 2 parent')

class B(A):

    def fea3(self):
        print('Feature 1 child')

    def fea4(self):
        print('Feature 2 child')

a1 = A()
print('From Parent')
a1.fea1()
a1.fea2()

b1 = B()
print('\nFrom child class')
b1.fea1()
b1.fea3()
b1.fea4()