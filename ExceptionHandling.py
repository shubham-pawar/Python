
a = int(input("Enter a 1st number "))

b = int(input("Enter a 2nd number "))

try:
    print('Resource open!')
    print(a/b)
    k = int(input('Enter a integer '))
    print('Number is ', k)
except ZeroDivisionError as e:
    print("You can't divide a number by zero. ", e)
except ValueError as e:
    print('Invalid input')
except Exception as e:
    print('Error 404')
finally:
    print('Resource closed!')