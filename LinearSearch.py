# fina a number in a list

pos = -1

def search(list, n):
    i = 0
    for i in range(len(list)):
        if list[i] == n:
            globals()['pos'] = i  #global veriable
            return True
    return False

list = [5,6,8,1,9,2]

n = 5

if search(list, n):
    print('We found number',n ,'in the list at position', pos)
else:
    print('We did not find number', n,'in the list')