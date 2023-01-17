class Computer:

        def __init__(self):
            self.name = 'CTS'
        def config(self):
            print('UWM020794 i5 8GB 256GB')

c1 = Computer()
c2 = Computer()

print(c1.name)
print(c2.name)

class NewC:
    def __init__(self):
        print('Hi,new comp')
c1 = NewC()