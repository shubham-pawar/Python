import math

class Computer:
    def config(self, CN, Pr, RAM, S):
        print('Computer name is', CN, "and config are", Pr,'',RAM,'GB','',St,'GB' )

CN =  input("Welcome! Please enter your computer name ")
Pr = input("Enter processor ")
RAM = input("Enter RAM ")
St = input("Enter storage ")

com = Computer()

try:
        com.config(CN, Pr, RAM, St)
except:
    print('wrong input')


