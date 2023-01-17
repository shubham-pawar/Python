# odd or even number
try:
    x = int(input("Enter a number "))
    r = x%2
except:
    print('Wrong input')

if r==0:
    print('Even number')

else:
    print('Odd number')

print('END')

