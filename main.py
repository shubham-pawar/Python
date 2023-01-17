def print_hi(a, b):

        print("sum of two numbers are", a + b)  # Press Ctrl+F8 to toggle the breakpoint.

        print("END")

if __name__ == '__main__':
    try:
        a = int(input("Enter a first number "))
        b = int(input("Enter a second number "))
    except NameError:
         print('An exception flew by!')

    print_hi(a, b)
