# binary search

pos = -1 # global variable

def BinarySearch(list, n):

    l = 0
    u = len(list) - 1

    while l <= u:
        m = (l + u) // 2

        if list[m] == n:
            globals()['pos'] = m
            return True
        else:
            if list[m] < n:
                l = m + 1
            else:
                u = m - 1
    return False
list = [4, 7, 8, 12, 45, 99, 111, 186, 200, 500] # we need a sorted list

n = int(input('Enter a number '))

if BinarySearch(list, n):
    print('We found number',n ,'in the list at position', pos + 1)
else:
    print('We did not find number', n,'in the list')